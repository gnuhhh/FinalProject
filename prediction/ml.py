# prediction/ml.py
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
import warnings

warnings.filterwarnings("ignore")

RANDOM_STATE = 42

def _create_feature_matrix_for_quota(years, scores):
    """
    X: features to predict quota
    - year (numeric)
    - score (benchmark_score)
    """
    X = np.hstack([years.reshape(-1, 1), scores.reshape(-1, 1)])
    return X

def _create_feature_matrix_for_score(years, quotas):
    """
    X: features to predict score
    - year (numeric)
    - quota
    """
    X = np.hstack([years.reshape(-1, 1), quotas.reshape(-1, 1)])
    return X

def _get_models():
    models = {
        'linear': Pipeline([
            ('scaler', StandardScaler()),
            ('linear', LinearRegression())
        ]),
        'poly2': Pipeline([
            ('scaler', StandardScaler()),
            ('poly', PolynomialFeatures(degree=2, include_bias=False)),
            ('linear', LinearRegression())
        ]),
        'rf': RandomForestRegressor(n_estimators=100, max_depth=4, random_state=RANDOM_STATE)
    }
    return models

def _cross_val_mse(model, X, y):
    n = len(y)
    if n <= 3:
        # LOOCV for very small data
        preds = []
        trues = []
        for i in range(n):
            mask = np.ones(n, dtype=bool)
            mask[i] = False
            X_tr, X_te = X[mask], X[~mask]
            y_tr, y_te = y[mask], y[~mask]
            try:
                if len(X_tr) > 0:
                    model.fit(X_tr, y_tr)
                    p = model.predict(X_te.reshape(1, -1))[0]
                else:
                    p = np.mean(y_tr) if len(y_tr) > 0 else 0
            except Exception:
                p = np.mean(y_tr) if len(y_tr) > 0 else 0
            preds.append(p)
            trues.append(y_te[0] if len(y_te) > 0 else 0)
        mse = mean_squared_error(trues, preds) if len(trues) > 0 else float('inf')
        return mse
    else:
        # KFold for larger data
        kf = KFold(n_splits=min(3, n), shuffle=False)
        mses = []
        for tr_idx, te_idx in kf.split(X):
            X_tr, X_te = X[tr_idx], X[te_idx]
            y_tr, y_te = y[tr_idx], y[te_idx]
            try:
                model.fit(X_tr, y_tr)
                p = model.predict(X_te)
            except Exception:
                p = np.repeat(np.mean(y_tr), len(y_te))
            mses.append(mean_squared_error(y_te, p))
        return float(np.mean(mses))

def _fit_models_and_evaluate(X, y):
    models = _get_models()
    results = {}
    for name, model in models.items():
        try:
            mse = _cross_val_mse(model, X, y)
            # fit on full data for prediction later
            if len(X) > 0:
                model.fit(X, y)
                results[name] = {
                    'model': model,
                    'mse': float(mse),
                    'pred_full': None
                }
            else:
                results[name] = {
                    'model': None,
                    'mse': float('inf'),
                    'error': 'No data',
                    'pred_full': None
                }
        except Exception as e:
            results[name] = {
                'model': None,
                'mse': float('inf'),
                'error': str(e),
                'pred_full': None
            }
    return results

def _weighted_ensemble_prediction(results, X_pred):
    """
    Weighted average of model predictions using weights = 1 / mse.
    If mse is inf or zero, handle safely.
    """
    preds = []
    weights = []
    for name, r in results.items():
        model = r.get('model')
        mse = r.get('mse', float('inf'))
        if model is None or not np.isfinite(mse) or mse == 0:
            continue
        try:
            p = model.predict(np.atleast_2d(X_pred))[0]
            preds.append(float(p))
            # small epsilon to avoid division by zero
            weights.append(1.0 / (mse + 1e-8))
        except Exception:
            continue
    
    if not preds:
        return None
    
    weights = np.array(weights)
    if weights.sum() == 0:
        return float(np.mean(preds))
    
    weights = weights / weights.sum()
    preds = np.array(preds)
    return float((preds * weights).sum())

def predict_quota_and_score_ml(criteria_sorted, predict_year):
    """
    Main function to call from views.
    Input:
      - criteria_sorted: list of AdmissionCriteria-like objects sorted by year ascending
      - predict_year: int (e.g., 2025)
    Output:
      dict with detailed results and final chosen predictions
    """
    n = len(criteria_sorted)
    years = np.array([c.year for c in criteria_sorted], dtype=float)
    quotas = np.array([c.quota for c in criteria_sorted], dtype=float)
    scores = np.array([c.benchmark_score for c in criteria_sorted], dtype=float)

    print(f"🤖 ML Model: Processing {n} data points, years: {years}")

    # Fallback for very small data
    if n == 0:
        return {
            'predicted_quota': 0,
            'predicted_score': 0,
            'quota_trend': 'unknown',
            'score_trend': 'unknown',
            'confidence': 'none',
            'algorithm': 'fallback_no_data'
        }
    
    if n == 1:
        last_quota = int(quotas[-1])
        last_score = float(scores[-1])
        print(f"🤖 ML Model: Single data point fallback - quota: {last_quota}, score: {last_score}")
        return {
            'predicted_quota': last_quota,
            'predicted_score': last_score,
            'quota_trend': 'stable',
            'score_trend': 'stable',
            'confidence': 'low',
            'algorithm': 'fallback_single'
        }

    # ----------------
    # Predict score for predict_year first (so we can use it as feature for quota)
    # ----------------
    X_score = _create_feature_matrix_for_score(years, quotas)
    y_score = scores

    print(f"🎯 Score Prediction: X_shape={X_score.shape}, y_mean={np.mean(y_score):.2f}")

    score_results = _fit_models_and_evaluate(X_score, y_score)

    # Create X_pred for score (predict_year, last_quota) - using last quota as proxy
    X_score_pred = np.array([predict_year, quotas[-1]])
    
    # Weighted ensemble for score
    score_ensemble = _weighted_ensemble_prediction(score_results, X_score_pred)
    
    # Also keep best single model (lowest mse)
    valid_score_models = {k: v for k, v in score_results.items() if v.get('model') is not None and np.isfinite(v.get('mse', float('inf')))}
    if valid_score_models:
        best_score_model_name = min(valid_score_models.keys(), key=lambda k: valid_score_models[k]['mse'])
        best_score_mse = valid_score_models[best_score_model_name]['mse']
        best_score_pred = None
        try:
            best_score_pred = float(valid_score_models[best_score_model_name]['model'].predict(X_score_pred.reshape(1, -1))[0])
        except Exception:
            best_score_pred = float(np.mean(y_score))
    else:
        best_score_pred = float(np.mean(y_score))
        best_score_mse = float('inf')

    # Choose final score prediction
    if score_ensemble is None:
        predicted_score = best_score_pred
        print(f"🎯 Score: Using best model - {best_score_pred:.2f}")
    else:
        # if ensemble disagrees hugely with best model, trust best model if its mse << others
        if abs(score_ensemble - best_score_pred) / (abs(best_score_pred) + 1e-6) > 0.25:
            predicted_score = 0.6 * best_score_pred + 0.4 * score_ensemble
            print(f"🎯 Score: Combined ensemble & best - {predicted_score:.2f}")
        else:
            predicted_score = score_ensemble
            print(f"🎯 Score: Using ensemble - {predicted_score:.2f}")

    # clamp predicted score to realistic range of historical +/- 3 std dev
    score_std = np.std(y_score) if len(y_score) > 1 else 1.0
    score_mean = np.mean(y_score)
    max_dev = max(3 * score_std, 2.0)  # at least 2 points
    predicted_score = float(np.clip(predicted_score, score_mean - max_dev, score_mean + max_dev))

    # Determine score trend
    score_trend = 'increasing' if predicted_score > scores[-1] else 'decreasing' if predicted_score < scores[-1] else 'stable'

    print(f"🎯 Final Score: {predicted_score:.2f}, Trend: {score_trend}")

    # ----------------
    # Predict quota using year + predicted_score
    # ----------------
    X_quota = _create_feature_matrix_for_quota(years, scores)
    y_quota = quotas

    print(f"📊 Quota Prediction: X_shape={X_quota.shape}, y_mean={np.mean(y_quota):.2f}")

    quota_results = _fit_models_and_evaluate(X_quota, y_quota)

    X_quota_pred = np.array([predict_year, predicted_score])

    quota_ensemble = _weighted_ensemble_prediction(quota_results, X_quota_pred)

    # Best single model for quota
    valid_quota_models = {k: v for k, v in quota_results.items() if v.get('model') is not None and np.isfinite(v.get('mse', float('inf')))}
    if valid_quota_models:
        best_quota_model_name = min(valid_quota_models.keys(), key=lambda k: valid_quota_models[k]['mse'])
        best_quota_mse = valid_quota_models[best_quota_model_name]['mse']
        best_quota_pred = None
        try:
            best_quota_pred = float(valid_quota_models[best_quota_model_name]['model'].predict(X_quota_pred.reshape(1, -1))[0])
        except Exception:
            best_quota_pred = float(np.mean(y_quota))
    else:
        best_quota_pred = float(np.mean(y_quota))
        best_quota_mse = float('inf')

    # Choose final quota prediction
    if quota_ensemble is None:
        predicted_quota = best_quota_pred
        print(f"📊 Quota: Using best model - {best_quota_pred:.2f}")
    else:
        if abs(quota_ensemble - best_quota_pred) / (abs(best_quota_pred) + 1e-6) > 0.25:
            predicted_quota = 0.6 * best_quota_pred + 0.4 * quota_ensemble
            print(f"📊 Quota: Combined ensemble & best - {predicted_quota:.2f}")
        else:
            predicted_quota = quota_ensemble
            print(f"📊 Quota: Using ensemble - {predicted_quota:.2f}")

    # Smooth/clamp final quota relative to last year's quota (±25%)
    last_quota = quotas[-1]
    lower = last_quota * 0.75
    upper = last_quota * 1.25
    predicted_quota = float(np.clip(predicted_quota, lower, upper))

    # Round and minimum
    predicted_quota = int(round(max(predicted_quota, 10)))  # Minimum 10
    predicted_score = round(float(predicted_score), 2)

    # Ensure score is in reasonable range
    predicted_score = max(15.0, min(30.0, predicted_score))

    # Confidence: based on mse magnitude and model agreement
    valid_quota_mses = [v['mse'] for v in quota_results.values() if np.isfinite(v.get('mse', float('inf')))]
    valid_score_mses = [v['mse'] for v in score_results.values() if np.isfinite(v.get('mse', float('inf')))]
    
    avg_quota_mse = np.mean(valid_quota_mses) if valid_quota_mses else float('inf')
    avg_score_mse = np.mean(valid_score_mses) if valid_score_mses else float('inf')

    confidence = 'low'
    if avg_quota_mse < 200 and avg_score_mse < 1.5:
        confidence = 'high'
    elif avg_quota_mse < 800 and avg_score_mse < 3.0:
        confidence = 'medium'

    print(f"✅ Final Results: Quota={predicted_quota}, Score={predicted_score}, Confidence={confidence}")

    result = {
        'predicted_quota': predicted_quota,
        'predicted_score': predicted_score,
        'quota_trend': 'increasing' if predicted_quota > last_quota else 'decreasing' if predicted_quota < last_quota else 'stable',
        'score_trend': score_trend,
        'confidence': confidence,
        'algorithm': 'ensemble_ml',
        'models': {
            'quota_models': {k: {'mse': v.get('mse', 'inf')} for k, v in quota_results.items()},
            'score_models': {k: {'mse': v.get('mse', 'inf')} for k, v in score_results.items()},
        },
        'notes': {
            'last_quota': int(last_quota),
            'last_score': float(scores[-1]),
            'data_points': n
        }
    }

    return result

# Test function để debug
if __name__ == "__main__":
    # Tạo dữ liệu test
    class MockCriteria:
        def __init__(self, year, quota, score):
            self.year = year
            self.quota = quota
            self.benchmark_score = score
            self.combination = "A00"
    
    # Test data
    test_data = [
        MockCriteria(2022, 100, 24.5),
        MockCriteria(2023, 120, 24.0),
        MockCriteria(2024, 130, 23.5)
    ]
    
    result = predict_quota_and_score_ml(test_data, 2025)
    print("\n🧪 TEST RESULTS:")
    print(f"Quota: {result['predicted_quota']}")
    print(f"Score: {result['predicted_score']}")
    print(f"Confidence: {result['confidence']}")
    print(f"Algorithm: {result['algorithm']}")
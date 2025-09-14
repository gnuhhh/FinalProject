import random
import pandas as pd

# Danh sách 20 ngành học
majors = [
    "Khoa học dữ liệu", "Thiết kế đồ họa", "Kỹ thuật xây dựng", "Kinh tế", "Y học",
    "Công nghệ thông tin", "Kiến trúc", "Tâm lý học", "Quản trị kinh doanh", "Kỹ thuật cơ khí",
    "Báo chí", "Giáo dục", "Luật", "Sinh học", "Hóa học", "Marketing", "Nông nghiệp",
    "Du lịch", "Ngôn ngữ học", "Kỹ thuật điện"
]

# Hàm chọn ngành học dựa trên đáp án
def choose_major(answers):
    if answers[0] >= 2 and answers[6] >= 2 and answers[10] >= 2:
        return "Khoa học dữ liệu"
    elif answers[1] >= 2 and answers[8] >= 2:
        return "Thiết kế đồ họa"
    elif answers[3] >= 2 and answers[12] >= 2:
        return "Kỹ thuật xây dựng"
    elif answers[9] >= 2 and answers[11] >= 2 and answers[18] >= 2:
        return "Quản trị kinh doanh"
    elif answers[7] >= 2:
        return "Y học"
    elif answers[0] >= 2 and answers[10] >= 2:
        return "Công nghệ thông tin"
    elif answers[3] >= 2 and answers[12] >= 2:
        return "Kiến trúc"
    elif answers[4] >= 2 and answers[13] >= 2:
        return "Tâm lý học"
    elif answers[2] >= 2 and answers[3] <= 1:
        return "Kỹ thuật cơ khí"
    elif answers[8] >= 2 and answers[16] >= 2:
        return "Báo chí"
    elif answers[4] >= 2 and answers[14] >= 2:
        return "Giáo dục"
    elif answers[15] >= 2 and answers[11] >= 2:
        return "Luật"
    elif answers[5] >= 2 and answers[17] <= 1:
        return "Sinh học"
    elif answers[5] >= 2 and answers[0] >= 2:
        return "Hóa học"
    elif answers[11] >= 2 and answers[15] >= 2:
        return "Marketing"
    elif answers[17] >= 2 and answers[3] >= 2:
        return "Nông nghiệp"
    elif answers[17] >= 2 and answers[11] >= 2:
        return "Du lịch"
    elif answers[8] >= 2 and answers[16] >= 2:
        return "Ngôn ngữ học"
    elif answers[2] >= 2 and answers[0] >= 2:
        return "Kỹ thuật điện"
    return random.choice(majors)  # Trường hợp không rõ ràng

# Tạo dữ liệu
data = []
for _ in range(5000):
    answers = [random.randint(0, 3) for _ in range(20)]  # 20 đáp án ngẫu nhiên
    major = choose_major(answers)
    data.append(answers + [major])

# Tạo DataFrame
columns = [f"Q{i+1}" for i in range(20)] + ["Ngành học"]
df = pd.DataFrame(data, columns=columns)

# Xuất ra file CSV
df.to_csv("dataset_500_rows_extended.csv", index=False)
print("Đã xuất file CSV")
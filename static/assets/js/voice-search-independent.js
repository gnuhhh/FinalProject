// static/js/voice-search-independent.js - ĐÃ SỬA ENDPOINT
(function () {
    'use strict';

    console.log('🔒 Loading Independent Voice Search - ĐÃ SỬA ENDPOINT MỚI');

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initVoiceSearch);
    } else {
        setTimeout(initVoiceSearch, 1000);
    }

    function initVoiceSearch() {
        try {
            if (window.voiceSearchInitialized) {
                console.log('ℹ️ Voice search already initialized');
                return;
            }

            console.log('🚀 Initializing Independent Voice Search - ĐÃ SỬA ENDPOINT');
            window.voiceSearchInitialized = true;

            createVoiceButton();
            setupEventListeners();

        } catch (error) {
            console.error('❌ Safe voice search init error:', error);
        }
    }

    function createVoiceButton() {
        if (document.getElementById('safe-voice-btn')) return;

        const btn = document.createElement('button');
        btn.id = 'safe-voice-btn';
        btn.innerHTML = '🎤';
        btn.title = 'Tìm kiếm bằng giọng nói - Hỗ trợ nhiều lệnh';
        btn.style.cssText = `
            position: fixed;
            bottom: 100px;
            right: 20px;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border: 3px solid white;
            color: white;
            font-size: 24px;
            cursor: pointer;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
            z-index: 9999;
            transition: all 0.3s ease;
        `;

        document.body.appendChild(btn);
        console.log('✅ Created safe voice button - ĐÃ SỬA ENDPOINT');
    }

    function setupEventListeners() {
        const btn = document.getElementById('safe-voice-btn');
        if (!btn) return;

        btn.addEventListener('click', handleVoiceClick);

        btn.addEventListener('mouseenter', () => {
            btn.style.transform = 'scale(1.1)';
            btn.style.boxShadow = '0 6px 25px rgba(0,0,0,0.4)';
        });

        btn.addEventListener('mouseleave', () => {
            if (!btn.classList.contains('listening')) {
                btn.style.transform = 'scale(1)';
                btn.style.boxShadow = '0 4px 20px rgba(0,0,0,0.3)';
            }
        });
    }

    async function handleVoiceClick() {
        const btn = document.getElementById('safe-voice-btn');
        if (!btn) return;

        if (btn.classList.contains('listening')) {
            await stopVoiceListening();
            return;
        }

        await startSmartVoiceListening();
    }

    async function startSmartVoiceListening() {
        const btn = document.getElementById('safe-voice-btn');
        if (!btn) return;

        try {
            console.log('🎤 Starting SMART voice listening với endpoint mới...');

            btn.classList.add('listening');
            btn.style.background = 'linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%)';
            btn.style.transform = 'scale(1.2)';
            btn.innerHTML = '🔴';

            showStatus('🎤 Đang nghe... Hãy nói lệnh của bạn', 'info');

            await startSpeechRecognition();

        } catch (error) {
            console.error('❌ Smart voice listening error:', error);
            showStatus('Lỗi khởi động voice. Vui lòng thử lại.', 'error');
            resetButton();
        }
    }

    function startSpeechRecognition() {
        return new Promise((resolve, reject) => {
            if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
                showStatus('Trình duyệt không hỗ trợ nhận diện giọng nói', 'error');
                reject(new Error('Browser not supported'));
                return;
            }

            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            const recognition = new SpeechRecognition();

            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = 'vi-VN';

            recognition.onstart = () => {
                console.log('🎤 Speech recognition started');
                showStatus('🎤 Đang nghe... Hãy nói lệnh của bạn', 'info');
            };

            recognition.onresult = async (event) => {
                const transcript = event.results[0][0].transcript;
                console.log('🎯 Nhận diện được:', transcript);

                await processSmartVoiceCommand(transcript);
                resolve(transcript);
            };

            recognition.onerror = (event) => {
                console.error('❌ Speech recognition error:', event.error);

                let errorMessage = 'Lỗi nhận diện giọng nói';
                if (event.error === 'not-allowed') {
                    errorMessage = 'Vui lòng cho phép sử dụng microphone';
                } else if (event.error === 'no-speech') {
                    errorMessage = 'Không phát hiện giọng nói';
                }

                showStatus(errorMessage, 'error');
                reject(new Error(event.error));
                resetButton();
            };

            recognition.onend = () => {
                console.log('⏹️ Speech recognition ended');
                resetButton();
            };

            recognition.start();
        });
    }

    async function processSmartVoiceCommand(transcript) {
        try {
            console.log(`🔄 Xử lý voice command thông minh: "${transcript}"`);

            showStatus(`🔍 Đang xử lý: "${transcript}"`, 'info');

            const response = await fetch('/Voice/api/voice-search/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken(),
                },
                body: JSON.stringify({
                    query: transcript,
                    search_type: 'general',
                    filters: {}
                })
            });

            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            const data = await response.json();
            console.log('🎯 Kết quả xử lý thông minh:', data);

            if (data.status === 'success' && data.redirect) {
                showStatus(`📍 ${data.message}`, 'success');

                resetButton();

                setTimeout(() => {
                    console.log(`🔄 Chuyển hướng đến: ${data.redirect_url}`);
                    window.location.href = data.redirect_url;
                }, 1500);

            } else {
                showStatus(`🔍 Tìm kiếm: "${transcript}"`, 'info');
                performNormalSearch(transcript);
                resetButton();
            }

        } catch (error) {
            console.error('❌ Lỗi xử lý voice command:', error);
            showStatus('Lỗi xử lý lệnh thoại', 'error');
            resetButton();
        }
    }

    function performNormalSearch(query) {
        console.log(`🔍 Thực hiện tìm kiếm thông thường: "${query}"`);

        const searchInput = document.querySelector('input[type="search"], input[name="q"]');
        if (searchInput) {
            searchInput.value = query;
            searchInput.focus();
        }
    }

    async function stopVoiceListening() {
        console.log('⏹️ Stopping safe voice listening...');

        try {
            await fetch('/Voice/api/voice-search/stop/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken(),
                }
            });
        } catch (error) {
            console.error('❌ Stop listening error:', error);
        } finally {
            resetButton();
        }
    }

    function resetButton() {
        const btn = document.getElementById('safe-voice-btn');
        if (!btn) return;

        btn.classList.remove('listening');
        btn.style.background = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
        btn.style.transform = 'scale(1)';
        btn.innerHTML = '🎤';
    }

    function showStatus(message, type = 'info') {
        console.log(`📢 Status [${type}]: ${message}`);

        let statusDiv = document.getElementById('safe-voice-status');
        if (!statusDiv) {
            statusDiv = document.createElement('div');
            statusDiv.id = 'safe-voice-status';
            statusDiv.style.cssText = `
                position: fixed;
                bottom: 170px;
                right: 20px;
                background: white;
                color: #333;
                padding: 12px 18px;
                border-radius: 8px;
                font-size: 14px;
                font-family: Arial, sans-serif;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                border-left: 4px solid #007bff;
                z-index: 9998;
                max-width: 300px;
                display: none;
            `;
            document.body.appendChild(statusDiv);
        }

        const colors = {
            'success': '#28a745',
            'error': '#dc3545',
            'warning': '#ffc107',
            'info': '#17a2b8',
            'processing': '#007bff'
        };

        statusDiv.style.borderLeftColor = colors[type] || '#007bff';
        statusDiv.textContent = message;
        statusDiv.style.display = 'block';

        setTimeout(() => {
            statusDiv.style.display = 'none';
        }, 4000);
    }

    function getCSRFToken() {
        try {
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]');
            if (csrfToken) {
                return csrfToken.value;
            }

            const cookieValue = document.cookie
                .split('; ')
                .find(row => row.startsWith('csrftoken='))
                ?.split('=')[1];

            return cookieValue || '';
        } catch (error) {
            console.error('❌ Lỗi lấy CSRF token:', error);
            return '';
        }
    }

    window.testSmartVoiceSearch = function (command = "trang chủ") {
        console.log('🧪 TEST Smart Voice Search với endpoint mới, lệnh:', command);
        processSmartVoiceCommand(command);
    };

    console.log('✅ Independent Voice Search - ĐÃ SỬA ENDPOINT loaded safely');
    console.log('🔧 Gõ testSmartVoiceSearch("trang chủ") để test endpoint mới');
})();
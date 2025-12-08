// static/assets/js/voice-search.js - PHIÊN BẢN ĐÃ SỬA ENDPOINT
class VoiceSearch {
    constructor() {
        this.isListening = false;
        this.debug = true;

        console.log('🎯 VOICE-SEARCH.JS - ĐÃ SỬA ENDPOINT MỚI');

        this.init();
    }

    log(message, data = null) {
        if (this.debug) {
            console.log(`🎤 VoiceSearch: ${message}`, data || '');
        }
    }

    error(message, error = null) {
        console.error(`❌ VoiceSearch: ${message}`, error || '');
    }

    init() {
        try {
            this.log('Đang khởi tạo voice search với endpoint mới...');
            this.createVoiceSearchUI();
            this.bindEvents();
        } catch (error) {
            this.error('Lỗi khởi tạo:', error);
        }
    }

    createVoiceSearchUI() {
        try {
            if (!document.getElementById('voice-search-btn')) {
                this.log('Đang tạo UI...');

                const voiceBtn = document.createElement('button');
                voiceBtn.id = 'voice-search-btn';
                voiceBtn.innerHTML = '🎤';
                voiceBtn.title = 'Tìm kiếm bằng giọng nói - Hỗ trợ nhiều lệnh';
                voiceBtn.style.cssText = `
                    position: fixed;
                    bottom: 20px;
                    right: 20px;
                    width: 60px;
                    height: 60px;
                    border-radius: 50%;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    border: none;
                    color: white;
                    font-size: 24px;
                    cursor: pointer;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                    z-index: 1000;
                    transition: all 0.3s ease;
                `;

                document.body.appendChild(voiceBtn);
                this.log('UI đã được tạo');
            }
        } catch (error) {
            this.error('Lỗi tạo UI:', error);
        }
    }

    bindEvents() {
        try {
            const voiceBtn = document.getElementById('voice-search-btn');
            if (!voiceBtn) {
                this.error('Không tìm thấy voice button');
                return;
            }

            voiceBtn.addEventListener('click', () => {
                this.log('Button clicked, isListening:', this.isListening);

                if (this.isListening) {
                    this.stopListening();
                } else {
                    this.startSmartVoiceSearch();
                }
            });

            this.log('Events bound successfully');
        } catch (error) {
            this.error('Lỗi bind events:', error);
        }
    }

    async startSmartVoiceSearch() {
        try {
            this.log('=== BẮT ĐẦU SMART VOICE SEARCH VỚI ENDPOINT MỚI ===');

            if (this.isListening) {
                this.log('Đang nghe rồi, bỏ qua');
                return;
            }

            this.isListening = true;
            this.updateButtonState(true);

            this.showNotification('🎤 Đang nghe... Hãy nói lệnh của bạn', 'info');

            await this.startSpeechRecognition();

        } catch (error) {
            console.error('❌ Lỗi smart voice search:', error);
            this.showNotification('Lỗi khởi động voice. Vui lòng thử lại.', 'error');
            this.stopListening();
        }
    }

    startSpeechRecognition() {
        return new Promise((resolve, reject) => {
            if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
                this.showNotification('Trình duyệt không hỗ trợ nhận diện giọng nói', 'error');
                reject(new Error('Browser not supported'));
                return;
            }

            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            this.recognition = new SpeechRecognition();

            this.recognition.continuous = false;
            this.recognition.interimResults = false;
            this.recognition.lang = 'vi-VN';

            this.recognition.onstart = () => {
                this.log('Speech recognition started');
                this.showNotification('🎤 Đang nghe... Hãy nói lệnh của bạn', 'info');
            };

            this.recognition.onresult = async (event) => {
                const transcript = event.results[0][0].transcript;
                this.log('Nhận diện được:', transcript);

                await this.processSmartVoiceCommand(transcript);
                resolve(transcript);
            };

            this.recognition.onerror = (event) => {
                this.error('Speech recognition error:', event.error);

                let errorMessage = 'Lỗi nhận diện giọng nói';
                if (event.error === 'not-allowed') {
                    errorMessage = 'Vui lòng cho phép sử dụng microphone';
                } else if (event.error === 'no-speech') {
                    errorMessage = 'Không phát hiện giọng nói';
                }

                this.showNotification(errorMessage, 'error');
                reject(new Error(event.error));
                this.stopListening();
            };

            this.recognition.onend = () => {
                this.log('Speech recognition ended');
                this.stopListening();
            };

            this.recognition.start();
        });
    }

    async processSmartVoiceCommand(transcript) {
        try {
            this.log(`🔄 Xử lý voice command thông minh: "${transcript}"`);

            this.showNotification(`🔍 Đang xử lý: "${transcript}"`, 'info');

            const response = await fetch('/Voice/api/voice-search/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.getCSRFToken(),
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
            this.log('Kết quả xử lý thông minh:', data);

            if (data.status === 'success' && data.redirect) {
                this.showNotification(`📍 ${data.message}`, 'success');

                this.stopListening();

                setTimeout(() => {
                    this.log(`🔄 Chuyển hướng đến: ${data.redirect_url}`);
                    window.location.href = data.redirect_url;
                }, 1500);

            } else {
                this.showNotification(`🔍 Tìm kiếm: "${transcript}"`, 'info');
                this.performNormalSearch(transcript);
                this.stopListening();
            }

        } catch (error) {
            this.error('Lỗi xử lý voice command:', error);
            this.showNotification('Lỗi xử lý lệnh thoại', 'error');
            this.stopListening();
        }
    }

    performNormalSearch(query) {
        this.log(`Thực hiện tìm kiếm thông thường: "${query}"`);

        const searchInput = document.querySelector('input[type="search"], input[name="q"]');
        if (searchInput) {
            searchInput.value = query;
            searchInput.focus();
        }
    }

    stopListening() {
        try {
            this.log('⏹️ Dừng voice search...');

            this.isListening = false;
            this.updateButtonState(false);

            if (this.recognition) {
                this.recognition.stop();
            }

        } catch (error) {
            console.error('Lỗi trong stopListening:', error);
        }
    }

    updateButtonState(listening) {
        try {
            const voiceBtn = document.getElementById('voice-search-btn');
            if (voiceBtn) {
                if (listening) {
                    voiceBtn.style.background = 'linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%)';
                    voiceBtn.style.transform = 'scale(1.1)';
                    voiceBtn.innerHTML = '🔴';
                } else {
                    voiceBtn.style.background = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
                    voiceBtn.style.transform = 'scale(1)';
                    voiceBtn.innerHTML = '🎤';
                }
            }
        } catch (error) {
            console.error('Lỗi update button:', error);
        }
    }

    showNotification(message, type = 'info') {
        try {
            const oldNotification = document.getElementById('voice-notification');
            if (oldNotification) {
                oldNotification.remove();
            }

            const notification = document.createElement('div');
            notification.id = 'voice-notification';
            notification.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                background: white;
                padding: 15px 20px;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                z-index: 1001;
                max-width: 350px;
                border-left: 4px solid #007bff;
                animation: slideInRight 0.3s ease-out;
                font-family: Arial, sans-serif;
            `;

            const colors = {
                'success': '#28a745',
                'error': '#dc3545',
                'warning': '#ffc107',
                'info': '#17a2b8'
            };

            notification.style.borderLeftColor = colors[type] || '#007bff';

            const icons = {
                'success': '✅',
                'error': '❌',
                'warning': '⚠️',
                'info': '🎤'
            };

            notification.innerHTML = `
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 18px;">${icons[type] || 'ℹ️'}</span>
                    <span style="color: #333; font-size: 14px; line-height: 1.4;">${message}</span>
                </div>
            `;

            document.body.appendChild(notification);

            setTimeout(() => {
                if (notification.parentElement) {
                    notification.remove();
                }
            }, 4000);

        } catch (error) {
            console.error('Lỗi hiển thị notification:', error);
            alert(message);
        }
    }

    getCSRFToken() {
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
            console.error('Lỗi lấy CSRF token:', error);
            return '';
        }
    }
}

if (!document.getElementById('voice-search-styles')) {
    const style = document.createElement('style');
    style.id = 'voice-search-styles';
    style.textContent = `
        @keyframes slideInRight {
            from {
                transform: translateX(100%);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
    `;
    document.head.appendChild(style);
}

document.addEventListener('DOMContentLoaded', function () {
    try {
        console.log('🚀 Đang khởi tạo VoiceSearch - ĐÃ SỬA ENDPOINT');
        window.voiceSearch = new VoiceSearch();
        console.log('✅ VoiceSearch với endpoint mới đã sẵn sàng!');

    } catch (error) {
        console.error('❌ Lỗi khởi tạo VoiceSearch:', error);
    }
});

function startVoiceSearch() {
    if (window.voiceSearch) {
        window.voiceSearch.startSmartVoiceSearch();
    } else {
        console.error('VoiceSearch chưa được khởi tạo');
    }
}
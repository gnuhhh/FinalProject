# Voice/voice_search.py
import speech_recognition as sr
import json
import time
import threading
from datetime import datetime

class VoiceSearch:
    def __init__(self):
        try:
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
            print("✅ Đã khởi tạo microphone và recognizer")
        except Exception as e:
            print(f"❌ Lỗi khởi tạo voice search: {e}")
            self.recognizer = None
            self.microphone = None
        
        self.is_listening = False
        self.callbacks = {
            'on_start': None,
            'on_result': None,
            'on_error': None,
            'on_stop': None
        }
        
        # Điều chỉnh microphone nếu khả dụng
        if self.microphone:
            self._adjust_microphone()
        
        # Từ khóa tìm kiếm cho hệ thống tuyển sinh
        self.search_keywords = {
            'majors': [
                'công nghệ thông tin', 'kỹ thuật điện tử', 'y khoa', 'quản trị kinh doanh',
                'kế toán', 'luật', 'sư phạm', 'kiến trúc', 'xây dựng', 'cơ khí',
                'điện tử viễn thông', 'công nghệ sinh học', 'du lịch', 'marketing',
                'tài chính ngân hàng', 'quan hệ quốc tế', 'báo chí', 'truyền thông',
                'y học', 'dược học', 'điều dưỡng', 'nha khoa', 'vật lý trị liệu'
            ],
            'universities': [
                'bách khoa hà nội', 'công nghệ', 'fpt', 'y hà nội', 
                'kinh tế quốc dân', 'luật hà nội', 'xây dựng', 'kiến trúc',
                'sư phạm hà nội', 'thương mại', 'ngoại thương', 'giao thông vận tải',
                'nông nghiệp', 'y dược', 'bách khoa đà nẵng', 'bách khoa tphcm',
                'khoa học tự nhiên', 'khoa học xã hội nhân văn', 'quốc gia hà nội'
            ],
            'blocks': ['a00', 'a01', 'b00', 'c00', 'd01', 'd07', 'd14', 'd15'],
            'regions': ['miền bắc', 'miền trung', 'miền nam', 'hà nội', 'tphcm', 'đà nẵng', 'cần thơ']
        }

    def _adjust_microphone(self):
        """Điều chỉnh microphone cho môi trường"""
        try:
            if not self.microphone:
                return
                
            print("🎤 Đang điều chỉnh microphone...")
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("✅ Microphone đã sẵn sàng!")
        except Exception as e:
            print(f"❌ Lỗi điều chỉnh microphone: {e}")

    def set_callback(self, event, callback):
        """Thiết lập callback function"""
        if event in self.callbacks:
            self.callbacks[event] = callback

    def start_listening(self):
        """Bắt đầu lắng nghe giọng nói"""
        if not self.microphone or not self.recognizer:
            self._trigger_callback('on_error', 'Microphone không khả dụng')
            return False

        if self.is_listening:
            self._trigger_callback('on_error', 'Hệ thống đang nghe...')
            return False

        try:
            self.is_listening = True
            self._trigger_callback('on_start', None)
            
            # Chạy nhận diện trong thread riêng
            thread = threading.Thread(target=self._recognize_speech)
            thread.daemon = True
            thread.start()
            
            return True
            
        except Exception as e:
            self.is_listening = False
            self._trigger_callback('on_error', f'Lỗi khởi động: {str(e)}')
            return False

    def stop_listening(self):
        """Dừng lắng nghe"""
        self.is_listening = False
        self._trigger_callback('on_stop', None)

    def _recognize_speech(self):
        """Nhận diện giọng nói (chạy trong thread riêng)"""
        if not self.microphone or not self.recognizer:
            self._trigger_callback('on_error', 'Microphone không khả dụng')
            self.is_listening = False
            return

        try:
            with self.microphone as source:
                print("🎤 Đang nghe... (nói trong 8 giây)")
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=8)
            
            print("🔍 Đang nhận diện giọng nói...")
            transcript = self.recognizer.recognize_google(audio, language='vi-VN')
            
            if transcript:
                print(f"📝 Đã nhận diện: {transcript}")
                # Phân tích và xử lý kết quả
                result = self._analyze_transcript(transcript)
                self._trigger_callback('on_result', result)
                
        except sr.WaitTimeoutError:
            self._trigger_callback('on_error', 'Không phát hiện giọng nói. Vui lòng thử lại.')
        except sr.UnknownValueError:
            self._trigger_callback('on_error', 'Không thể nhận diện giọng nói. Vui lòng nói rõ hơn.')
        except sr.RequestError as e:
            self._trigger_callback('on_error', f'Lỗi kết nối dịch vụ nhận diện: {e}')
        except Exception as e:
            self._trigger_callback('on_error', f'Lỗi không xác định: {e}')
        finally:
            self.is_listening = False

    def _analyze_transcript(self, transcript):
        """
        Phân tích transcript và trích xuất thông tin tìm kiếm
        """
        transcript_lower = transcript.lower()
        
        result = {
            'transcript': transcript,
            'filters': {},
            'search_type': 'general',
            'confidence': 0.8,
            'timestamp': datetime.now().isoformat(),
            'actions': [],
            'search_term': transcript
        }

        # Phát hiện loại tìm kiếm
        search_type = self._detect_search_type(transcript_lower)
        result['search_type'] = search_type
        
        # Trích xuất thông tin dựa trên loại tìm kiếm
        if search_type == 'major':
            major = self._extract_major(transcript_lower)
            if major:
                result['filters']['major'] = major
                result['search_term'] = major
                result['actions'].append('filter_major')
                
        elif search_type == 'university':
            university = self._extract_university(transcript_lower)
            if university:
                result['filters']['university'] = university
                result['search_term'] = university
                result['actions'].append('filter_university')
                
        elif search_type == 'block':
            block = self._extract_block(transcript_lower)
            if block:
                result['filters']['block'] = block
                result['actions'].append('filter_block')
                
        elif search_type == 'region':
            region = self._extract_region(transcript_lower)
            if region:
                result['filters']['region'] = region
                result['actions'].append('filter_region')
                
        else:  # general search
            result['actions'].append('general_search')

        return result

    def _detect_search_type(self, transcript):
        """Phát hiện loại tìm kiếm từ transcript"""
        # Tìm kiếm ngành học
        major_keywords = ['ngành', 'chuyên ngành', 'học ngành', 'ngành học', 'ngành nào', 'học gì']
        if any(keyword in transcript for keyword in major_keywords):
            return 'major'
        
        # Tìm kiếm trường học
        uni_keywords = ['trường', 'đại học', 'học viện', 'trường đại học', 'trường nào', 'học ở đâu']
        if any(keyword in transcript for keyword in uni_keywords):
            return 'university'
        
        # Tìm kiếm khối thi
        block_keywords = ['khối', 'tổ hợp', 'khối thi', 'môn thi', 'thi khối']
        if any(keyword in transcript for keyword in block_keywords):
            return 'block'
        
        # Tìm kiếm vùng miền
        region_keywords = ['vùng', 'miền', 'khu vực', 'ở đâu', 'tại']
        if any(keyword in transcript for keyword in region_keywords):
            return 'region'
        
        return 'general'

    def _extract_major(self, transcript):
        """Trích xuất tên ngành học từ transcript"""
        for major in self.search_keywords['majors']:
            if major in transcript:
                return major.title()
        
        # Tìm kiếm gần đúng
        for major in self.search_keywords['majors']:
            major_words = major.split()
            if any(word in transcript for word in major_words):
                return major.title()
        
        return None

    def _extract_university(self, transcript):
        """Trích xuất tên trường học từ transcript - PHÙ HỢP VỚI MODEL THỰC TẾ"""
        university_map = {
            'bách khoa hà nội': 'Bách Khoa Hà Nội',
            'bách khoa hn': 'Bách Khoa Hà Nội',
            'đại học bách khoa': 'Bách Khoa',
            'bách khoa': 'Bách Khoa',
            'đại học công nghiệp': 'Công Nghiệp',
            'công nghiệp': 'Công Nghiệp',
            'fpt': 'FPT',
            'đại học fpt': 'FPT',
            'y hà nội': 'Y Hà Nội',
            'đại học y': 'Y',
            'kinh tế quốc dân': 'Kinh Tế Quốc Dân',
            'luật hà nội': 'Luật Hà Nội',
            'đại học luật': 'Luật',
            'xây dựng': 'Xây Dựng',
            'kiến trúc': 'Kiến Trúc',
            'sư phạm hà nội': 'Sư Phạm Hà Nội',
            'thương mại': 'Thương Mại',
            'ngoại thương': 'Ngoại Thương',
            'giao thông vận tải': 'Giao Thông Vận Tải',
            'nông nghiệp': 'Nông Nghiệp',
            'y dược': 'Y Dược'
        }
        
        for key, value in university_map.items():
            if key in transcript:
                return value
        
        # Tìm kiếm gần đúng
        for uni in self.search_keywords['universities']:
            uni_words = uni.split()
            if any(word in transcript for word in uni_words):
                return university_map.get(uni, uni)
        
        return None

    def _extract_block(self, transcript):
        """Trích xuất khối thi từ transcript"""
        for block in self.search_keywords['blocks']:
            if block in transcript:
                return block.upper()
        
        # Ánh xạ tên khối
        block_map = {
            'a': 'A00', 'a0': 'A00', 'toán lý hóa': 'A00',
            'a1': 'A01', 'toán lý anh': 'A01',
            'b': 'B00', 'toán hóa sinh': 'B00',
            'c': 'C00', 'văn sử địa': 'C00',
            'd': 'D01', 'toán văn anh': 'D01',
            'd7': 'D07', 'toán hóa anh': 'D07'
        }
        
        for key, value in block_map.items():
            if key in transcript:
                return value
        
        return None

    def _extract_region(self, transcript):
        """Trích xuất vùng miền từ transcript"""
        region_map = {
            'bắc': 'Miền Bắc', 'miền bắc': 'Miền Bắc', 'hà nội': 'Miền Bắc', 'hn': 'Miền Bắc',
            'trung': 'Miền Trung', 'miền trung': 'Miền Trung', 'huế': 'Miền Trung', 'đà nẵng': 'Miền Trung',
            'nam': 'Miền Nam', 'miền nam': 'Miền Nam', 'sài gòn': 'Miền Nam', 'hồ chí minh': 'Miền Nam', 
            'tphcm': 'Miền Nam', 'tp hcm': 'Miền Nam', 'cần thơ': 'Miền Nam'
        }
        
        for key, value in region_map.items():
            if key in transcript:
                return value
        
        return None

    def _trigger_callback(self, event, data):
        """Kích hoạt callback function"""
        if self.callbacks[event]:
            try:
                self.callbacks[event](data)
            except Exception as e:
                print(f"❌ Lỗi callback {event}: {e}")

    def get_suggestions(self, query):
        """Lấy gợi ý tìm kiếm dựa trên query"""
        if not query:
            return []
            
        query_lower = query.lower()
        suggestions = []
        
        # Tìm trong ngành học
        for major in self.search_keywords['majors']:
            if query_lower in major:
                suggestions.append({
                    'type': 'major',
                    'value': major.title(),
                    'display': f'🎓 {major.title()}',
                    'action': 'filter_major'
                })
        
        # Tìm trong trường học
        university_map = {
            'bách khoa hà nội': 'Đại học Bách Khoa Hà Nội',
            'công nghệ': 'Đại học Công nghệ',
            'fpt': 'Đại học FPT',
            'y hà nội': 'Đại học Y Hà Nội',
            'kinh tế quốc dân': 'Đại học Kinh tế Quốc dân',
            'luật hà nội': 'Đại học Luật Hà Nội',
            'xây dựng': 'Đại học Xây dựng',
            'kiến trúc': 'Đại học Kiến trúc'
        }
        
        for uni_key, uni_name in university_map.items():
            if query_lower in uni_key:
                suggestions.append({
                    'type': 'university',
                    'value': uni_name,
                    'display': f'🏫 {uni_name}',
                    'action': 'filter_university'
                })
        
        # Tìm trong khối thi
        for block in self.search_keywords['blocks']:
            if query_lower in block:
                suggestions.append({
                    'type': 'block',
                    'value': block.upper(),
                    'display': f'📚 Khối {block.upper()}',
                    'action': 'filter_block'
                })
        
        return suggestions[:5]  # Giới hạn 5 gợi ý

    def is_available(self):
        """Kiểm tra tính khả dụng của voice search"""
        try:
            if not self.microphone or not self.recognizer:
                return False
                
            # Kiểm tra microphone
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.1)
            return True
        except Exception as e:
            print(f"❌ Microphone không khả dụng: {e}")
            return False

    def process_text_command(self, text):
        """Xử lý lệnh văn bản (dùng cho testing)"""
        if not text:
            return {
                'transcript': '',
                'filters': {},
                'search_type': 'general',
                'confidence': 0.0,
                'timestamp': datetime.now().isoformat(),
                'actions': [],
                'search_term': ''
            }
        return self._analyze_transcript(text)

# Tạo instance toàn cục để sử dụng
voice_search_instance = VoiceSearch()
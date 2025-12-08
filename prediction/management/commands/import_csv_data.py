# prediction/management/commands/import_csv_data.py
import os
import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from prediction.models import Region, University, MajorGroup, Major, AdmissionCriteria

class Command(BaseCommand):
    help = 'Import dữ liệu từ CSV files vào database'
    
    def add_arguments(self, parser):
        parser.add_argument('--universities', type=str, default='project/data/universities.csv')
        parser.add_argument('--majors', type=str, default='project/data/majors.csv') 
        parser.add_argument('--targets', type=str, default='project/data/targets.csv')

    def handle(self, *args, **options):
        self.stdout.write('🚀 Bắt đầu import dữ liệu từ CSV...')
        
        try:
            with transaction.atomic():
                self.import_universities(options['universities'])
                self.import_majors(options['majors'])
                self.import_admission_criteria(options['targets'])
            
            self.stdout.write(
                self.style.SUCCESS('✅ Import dữ liệu thành công!')
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Lỗi khi import dữ liệu: {str(e)}')
            )

    def import_universities(self, file_path):
        """Import dữ liệu universities"""
        self.stdout.write(f'📁 Đang import universities từ: {file_path}')
        
        # Kiểm tra file tồn tại
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f'❌ File không tồn tại: {file_path}'))
            return
        
        df = pd.read_csv(file_path)
        created_count = 0
        updated_count = 0
        
        # Tạo mapping cho region name -> code
        region_mapping = {
            'Bắc': 'MB',  # Miền Bắc
            'Nam': 'MN',  # Miền Nam  
            'Trung': 'MT' # Miền Trung
        }
        
        for _, row in df.iterrows():
            region_name = row['region']
            
            # Sử dụng mapping thay vì tự động tạo code
            region_code = region_mapping.get(region_name, region_name[:2].upper())
            
            region, _ = Region.objects.get_or_create(
                name=f"Miền {region_name}",  # Đảm bảo tên đầy đủ
                defaults={'code': region_code}
            )
            
            university, created = University.objects.update_or_create(
                code=row['code'],
                defaults={
                    'name': row['name'],
                    'region': region,
                }
            )
            if created:
                created_count += 1
            else:
                updated_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'✅ Universities: {created_count} created, {updated_count} updated')
        )

    def import_majors(self, file_path):
        """Import dữ liệu majors"""
        self.stdout.write(f'📁 Đang import majors từ: {file_path}')
        
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f'❌ File không tồn tại: {file_path}'))
            return
        
        df = pd.read_csv(file_path)
        created_count = 0
        updated_count = 0
        errors = 0
        
        for _, row in df.iterrows():
            try:
                university = University.objects.get(code=row['university_code'])
            except University.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'⚠️ Không tìm thấy trường: {row["university_code"]}')
                )
                errors += 1
                continue
            
            major_group, _ = MajorGroup.objects.get_or_create(
                name=row['field'],
                defaults={'code': row['field'][:3].upper()}
            )
            
            major, created = Major.objects.update_or_create(
                code=row['major_code'],
                university=university,
                defaults={
                    'name': row['major_name'],
                    'major_group': major_group
                }
            )
            if created:
                created_count += 1
            else:
                updated_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'✅ Majors: {created_count} created, {updated_count} updated, {errors} errors')
        )

    def import_admission_criteria(self, file_path):
        """Import dữ liệu admission criteria"""
        self.stdout.write(f'📁 Đang import admission criteria từ: {file_path}')
        
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f'❌ File không tồn tại: {file_path}'))
            return
        
        df = pd.read_csv(file_path)
        created_count = 0
        updated_count = 0
        errors = 0
        
        for index, row in df.iterrows():
            try:
                major_code = row['major_code']
                year = int(row['year'])
                
                # Tìm tất cả các major có code này
                majors = Major.objects.filter(code=major_code)
                
                if not majors.exists():
                    self.stdout.write(
                        self.style.WARNING(f'⚠️ Không tìm thấy ngành: {major_code}')
                    )
                    errors += 1
                    continue
                
                # Với mỗi major, tạo/cập nhật admission criteria
                for major in majors:
                    criteria, created = AdmissionCriteria.objects.update_or_create(
                        major=major,
                        year=year,
                        defaults={
                            'quota': int(row['quota']),
                            'benchmark_score': float(row['score']),
                            'combination': row['combinations']
                        }
                    )
                    if created:
                        created_count += 1
                    else:
                        updated_count += 1
                        
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'❌ Lỗi khi xử lý dòng {index + 2}: {e}')
                )
                errors += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'✅ Admission Criteria: {created_count} created, {updated_count} updated, {errors} errors')
        )
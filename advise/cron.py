# from datetime import datetime
# from django.utils.timezone import now
# from .models import Appointment

# def auto_update_appointment_status():   
#     current_time = now().time()
#     current_date = now().date()
#     appointments = Appointment.objects.filter(
#         status = 'N', 
#         work_schedule__date = current_date, 
#         work_schedule__work_shift__start_time__lte = current_time, 
#         work_schedule__work_shift__endtime__gte = current_time)
#     for appointment in appointments:
#         if appointment.status != 'P':
#             appointment.status = 'P'
#             appointment.save()
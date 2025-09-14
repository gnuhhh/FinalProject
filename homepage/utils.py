from .models import Expert

def generate_experts():
    experts = [
        {
            "expert_first_name": "Nguyễn Văn",
            "expert_last_name": "An",
            "expert_description": "Chuyên gia tư vấn tuyển sinh đại học khối kỹ thuật, hơn 10 năm kinh nghiệm."
        },
        {
            "expert_first_name": "Trần Thị",
            "expert_last_name": "Lan",
            "expert_description": "Tư vấn viên giàu kinh nghiệm trong lĩnh vực tuyển sinh ngành kinh tế và quản trị."
        },
        {
            "expert_first_name": "Lê Minh",
            "expert_last_name": "Tuấn",
            "expert_description": "Hỗ trợ học sinh chọn ngành phù hợp theo năng lực và sở thích cá nhân."
        },
        {
            "expert_first_name": "Phạm Thị",
            "expert_last_name": "Hồng",
            "expert_description": "Đã tư vấn thành công cho hàng trăm học sinh vào các trường top đầu."
        },
        {
            "expert_first_name": "Đỗ Đức",
            "expert_last_name": "Dũng",
            "expert_description": "Am hiểu xu hướng tuyển sinh và thị trường lao động hiện nay."
        },
    ]
    for expert in experts:
        Expert.objects.create(**expert)
    print(f'Tạo thành công {len(experts)} chuyên gia')
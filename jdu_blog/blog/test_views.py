import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_post_list_view_status_code(client):
    # Ro'yxat ko'rinishi login talab qilishi mumkin, shuning uchun test foydalanuvchisi yaratib kiramiz:
    user = User.objects.create_user(username='testuser', password='password123')
    client.login(username='testuser', password='password123')

    # Postlar ro'yxati URL manziliga GET so'rovi yuboramiz
    url = reverse('post_list')
    response = client.get(url)

    # 5-topshiriq talabi: status_code 200 ekanini tekshirish
    assert response.status_code == 200
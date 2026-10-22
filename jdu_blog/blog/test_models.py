import pytest
from blog.models import Post

@pytest.mark.django_db
def test_post_creation():
    # 1. Post obyektini yaratamiz
    post = Post.objects.create(
        title="Pytest bilan birinchi test",
        content="Django modellarini avtomatik testlash juda qulay."
    )

    # 2. Maydonlarini assert yordamida tekshiramiz
    assert post.pk is not None
    assert post.title == "Pytest bilan birinchi test"
    assert post.content == "Django modellarini avtomatik testlash juda qulay."
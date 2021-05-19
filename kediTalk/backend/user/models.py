from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# user의 모델을 username, password 등으로 정의한 model은 찾아볼 수 없다 !
# 이는 user의 모델의 경우
# from django.contrib.auth.models import User
# 즉 django의 내장 auth model로 부터 정의된 User를 Import 시켰기 때문에 따로 작성안해준 이유이다 !
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_pk = models.IntegerField(blank=True)
    email = models.EmailField(max_length=500, blank=True)
    mygit = models.CharField(max_length=50, blank=True)
    nickname = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to="profile/image", default='red.jpg')
    myInfo = models.CharField(max_length=150, blank=True)
    # ko
    # firstname = models.CharField(max_length=50, blank=True)
    # lastname = models.CharField(max_length=50, blank=True)
    # country = models.CharField(max_length=50, blank=True)
    # language = models.CharField(max_length=50, blank=True)
#장고 모델 필드_Django Model Fields정리
#https://donis-note.medium.com/%EC%9E%A5%EA%B3%A0-%EB%AA%A8%EB%8D%B8-%ED%95%84%EB%93%9C-django-model-fields-%EC%A0%95%EB%A6%AC-4297d1bad65b

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, user_pk=instance.id)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
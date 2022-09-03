from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


# Create your models here.
class User(AbstractBaseUser):
    """
        유저 프로파일 사진
        유저 닉네임          -> 화면에 표기되는 이름
        유저 아이디          -> 실제 사용자 이름
        유저 이메일 주소      -> 회원가입할 때 사용하는 아이다
        유저 비밀번호         -> 디폴트를 쓰자 !
    """

    profile_image = models.TextField()
    nickname = models.CharField(max_length=24, unique=True)
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'nickname'

    class Meta:
        db_table = "User"

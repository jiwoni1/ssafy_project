from django.db import models
from django.contrib.auth.models import AbstractUser
# 추가.Adapter 커스터 마이징
from allauth.account.adapter import DefaultAccountAdapter

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    financial_products = models.TextField(blank=True, null=True)


# 추가.Adapter 커스터 마이징
class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        # Saves a new `User` instance using information provided in the
        # signup form.
        from allauth.account.utils import user_email, user_field, user_username
        # 기존 코드를 참고하여 새로운 필드들을 작성해줍니다.
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        nickname = data.get("nickname")
        age = data.get("age")
        money = data.get("money")
        salary = data.get("salary")
        financial_product = data.get("financial_products")

        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname:
            user_field(user, "nickname", nickname)
        if age:
            user.age = age
        if money:
            user.money = money
        if salary:
            user.salary = salary
        # financial_products 의 경우 문자열 입력을 받아 리스트 형태로 저장을 해야 되기 때문에, 저장하기 전에 리스트로 바꿔주는 작업을 추가해줍니다.
        if financial_product:
            financial_products = user.financial_products.split(',')
            financial_products.append(financial_product)
            if len(financial_products) > 1:
                financial_products = ','.join(financial_products)
            user_field(user, "financial_products", financial_products)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user

        # 회원 가입 시 사용하는 allauth.account.adapter.DefaultAccountAdapter 를 위에서 구현한 adapter 로 설정해주어야 합니다.
        # settings.py 에 아래 내용을 추가한다.
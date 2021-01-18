from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from . import models


class LoginForm(forms.Form):
    user_id = forms.CharField(label="이메일ID")
    user_pw = forms.CharField(widget=forms.PasswordInput, label="비밀번호")

    # 필드 내용 검증하는 함수(반드시 접두사 clean_ 사용), 데이터 맞지않으면 지움
    def clean(self):
        # 정리된 데이터에서 키 값을 이용하여 값 찾기
        user_id = self.cleaned_data.get("user_id")
        user_pw = self.cleaned_data.get("user_pw")

        # 입력데이터 DB의 정보와 일치여부 검증
        try:
            user = models.User.objects.get(username=user_id)
            if user.check_password(user_pw):
                return self.cleaned_data
            else:
                # 해딩 필드에 에러 발생
                self.add_error("user_pw", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("user_id", forms.ValidationError("User does not exist"))


# 장고 Model Form이용하여 생성
class SignUpForm(forms.ModelForm):
    user_id = forms.CharField(label="아이디")
    user_pw = forms.CharField(widget=forms.PasswordInput, label="비밀번호")
    re_user_pw = forms.CharField(widget=forms.PasswordInput, label="비밀번호 확인")

    class Meta:
        model = models.User

        fields = (
            "user_name",
            "user_position",
            "birthdate",
            "phone_num",
            "user_addr",
            "post_num",
        )

    def clean_re_user_pw(self):
        user_pw = self.cleaned_data.get("user_pw")
        re_user_pw = self.cleaned_data.get("re_user_pw")

        if user_pw != re_user_pw:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return user_pw

    def save(self, *args, **kwargs):

        # commit=False 옵션 이용해 오브젝트는 생성하지만 DB에는 적용하지 않음
        user = super().save(commit=False)

        user_id = self.cleaned_data.get("user_id")
        user_pw = self.cleaned_data.get("user_pw")
        user_name = self.cleaned_data.get("user_name")
        user_position = self.cleaned_data.get("user_position")
        phone_num = self.cleaned_data.get("phone_num")
        birthdate = self.cleaned_data.get("birthdate")
        user_addr = self.cleaned_data.get("user_addr")
        post_num = self.cleaned_data.get("post_num")

        user.username = user_id
        user.set_password(user_pw)  # pw암호화
        user.user_name = user_name
        user.user_position = user_position
        user.phone_num = phone_num
        user.birthdate = birthdate
        user.user_addr = user_addr
        user.post_num = post_num
        user.save()  # DB에 유저 저장


class FindPasswordForm(forms.Form):
    user_id = forms.CharField(label="이메일ID")
    phone_num = forms.CharField(label="전화번호")

    # 필드 내용 검증하는 함수(반드시 접두사 clean_ 사용), 데이터 맞지않으면 지움
    def clean(self):
        # 정리된 데이터에서 키 값을 이용하여 값 찾기
        user_id = self.cleaned_data.get("user_id")
        phone_num = self.cleaned_data.get("phone_num")

        # 입력데이터 DB의 정보와 일치여부 검증
        try:
            user = models.User.objects.get(username=user_id)
            phone_num = models.User.objects.get(phone_num=phone_num)

        except models.User.DoesNotExist:
            self.add_error("user_id", forms.ValidationError("User does not exist"))

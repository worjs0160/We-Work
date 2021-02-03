from django.views import View
from django.views.generic import FormView, DetailView
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from . import forms, models


# 장고 Form View 이용하여 로그인, 로그아웃 만들기
class LoginView(FormView):

    template_name = "login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        user_id = form.cleaned_data.get("user_id")
        user_pw = form.cleaned_data.get("user_pw")

        # username과 password이용하여 로그인 검증
        user = authenticate(self.request, username=user_id, password=user_pw)

        if user is not None:
            login(self.request, user)
        # success_url로 가서 다시 작동
        return super().form_valid(form)


# 로그아웃 FBV
def log_out(request):
    logout(request)
    return redirect(reverse("core:login"))


class SignUpView(FormView):

    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:start")

    # form의 데이터 검증 후 맞으면 DB에 저장 실행
    def form_valid(self, form):
        form.save()
        """
        user_email = form.cleaned_data.get("user_email")
        user_pw = form.cleaned_data.get("user_pw")
        user = authenticate(self.request, username=user_email, password=user_pw)

        if user is not None:
            login(self.request, user)
        """
        return super().form_valid(form)


class UserInfoView(DetailView):
    template_name = "users/user_info.html"
    model = models.User


class UpdateProfile(UpdateView):
    model = models.User
    template_name = "users/update_profile.html"
    fields = [
        "phone_num",
        "user_addr",
        "post_num",
        "user_bio",
        "avatar",
    ]
    success_url = reverse_lazy("core:home")

    # form에서 로드할 객체(현재 로그인 중인) 불러오는 함수
    def get_object(self, queryset=None):
        return self.request.user


# 패스워드 변경 함수
@login_required
def update_password(request):

    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            return redirect(reverse("core:start"))

        return render(request, "users/update_password.html", {"form": form})

    else:
        form = PasswordChangeForm(request.user)
        return render(request, "users/update_password.html", {"form": form})


def find_password(request):

    if request.method == "POST":
        form = PasswordChangeForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect(reverse("core:start"))

        return render(request, "users/find_password_2.html", {"form": form})

    else:
        form = forms.FindPasswordForm()
        return render(request, "users/find_password.html", {"form": form})

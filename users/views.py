from django.views import View
from django.views.generic import FormView, DetailView
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from . import forms, models


# 장고 Form View 이용하여 로그인, 로그아웃 만들기
class LoginView(FormView):

    template_name = "start_login.html"
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


def log_out(request):
    logout(request)
    return redirect(reverse("core:start"))


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


# 정보 업데이트 하는 함수
@login_required
def update_info(request):
    if request.method == "POST":
        form = forms.CustomUserChangeForm(request.POST, instance=request.user)

        # form이 올바른 경우
        if form.is_valid():
            form.save()  # form 정보 DB에 업데이트
            return redirect("core:home")  # 메인페이지로 이동

        return render(request, "users/update_info.html", {"form": form})

    # GET방식인 경우
    else:
        form = forms.CustomUserChangeForm(instance=request.user)
        return render(request, "users/update_info.html", {"form": form})


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

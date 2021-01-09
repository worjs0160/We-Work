from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect, reverse, render
from django.views.generic import View, ListView, DetailView
from users import models as user_models
from . import models, forms

# Create your views here.


class UserView(ListView):

    model = user_models.User
    paginate_by = 12
    paginate_orphans = 5
    # ordering = "created"
    context_object_name = "users"
    template_name = "messengers/msg_list.html"


def go_msg_room(request, my_pk, your_pk):
    user_one = user_models.User.objects.get_or_none(pk=my_pk)
    user_two = user_models.User.objects.get_or_none(pk=your_pk)
    if user_one is not None and user_two is not None:
        try:
            messenger = models.MessengerUser.objects.get(
                Q(participants=user_one) & Q(participants=user_two)
            )
        except models.MessengerUser.DoesNotExist:
            messenger = models.MessengerUser.objects.create()
            messenger.participants.add(user_one, user_two)
    return redirect(reverse("messengers:detail", kwargs={"pk": messenger.pk}))


class MessengerRoomView(View):
    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        messenger = models.MessengerUser.objects.get_or_none(pk=pk)
        if not messenger:
            raise Http404()
        return render(
            self.request,
            "messengers/messengeruser_detail.html",
            {"messenger": messenger},
        )

    def post(self, *args, **kwargs):
        message = self.request.POST.get("message", None)
        pk = kwargs.get("pk")
        messenger = models.MessengerUser.objects.get_or_none(pk=pk)
        if not messenger:
            raise Http404()
        if message is not None:
            models.Message.objects.create(
                message=message, user=self.request.user, messenger=messenger
            )
        return redirect(reverse("messengers:detail", kwargs={"pk": pk}))
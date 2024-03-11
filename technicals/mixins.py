from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


class OnlyAdminMixin:
    @method_decorator(user_passes_test(lambda user: user.is_staff, login_url=reverse_lazy('only_admin')))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

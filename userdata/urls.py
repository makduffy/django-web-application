from django.urls import path
from .views import user_form, view_data_page

urlpatterns = [
    path("", user_form, name="index"),
    path("userdata/<int:instance_id>/", view_data_page, name="view_data_page")
]

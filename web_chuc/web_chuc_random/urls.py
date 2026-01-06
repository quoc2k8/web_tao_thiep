from django.urls import path
from . import views

app_name = "web_chuc_random"

urlpatterns = [
    # Khi vào trang chủ của app, nó sẽ gọi hàm random_number
    path('', views.chuc, name='chuc'),
    path("logs_chuc/", views.log_chuc, name="show_logs"),
    path("log/<int:id>/", views.log_detail, name="thu"),
    path("log/<int:id>/edit", views.log_edit, name="log_edit"),
]
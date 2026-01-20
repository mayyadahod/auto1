from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # أو اسم دالة الصفحة الرئيسية
    path('editor/', views.editor, name='editor_page'), # تأكدي من هذا السطر
]
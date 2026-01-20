from django.shortcuts import render

def home(request):
    return render(request, 'ui1/index.html')
def blueprint_editor(request):
    return render(request, 'ui1/editor.html') # تأكد أن اسم الملف editor.html
def editor(request):
    return render(request, 'ui1/editor.html') # أو اسم ملف المحرر الجديد
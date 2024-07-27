from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('a/', admin.site.urls),
    path('admin/login', views.admin_signin, name='admin-login'),
    path('student/login', views.student_signin, name='student-login'),
    path('student/add', views.add_student, name='add-student', kwargs={'message': ''}),
    path('student/add?m=<str:message>', views.add_student, name='add-student'),
    path('porter/add', views.add_porter, name='add-porter'),
    path('porter/add?m=<str:message>', views.add_porter, name='add-porter'),
    path('logout', views.logout_user, name='logout'),
    path('evaluation', views.list_evaluation, name='list-evaluation', kwargs={'message': ''}),
    path('evaluation?m=<str:message>', views.list_evaluation, name='list-evaluation'),
    path('evaluation/<int:porter_id>', views.evaluation, name='evaluation'),
    path('', views.student_signin)
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
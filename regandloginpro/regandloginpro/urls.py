from django.conf.urls import url
from django.contrib import admin
from regandloginapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^reg/',views.reg_view),
    url(r'^$',views.login_view),
    url(r'^login/',views.login_view),
]
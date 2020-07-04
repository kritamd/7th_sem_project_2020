
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from HeartPredict import settings
from accounts import views

app_name='accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('accounts/',include('accounts.urls')),
    path('predict/',include('predict.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

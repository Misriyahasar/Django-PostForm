from django.urls import path
from django.conf import settings
from myapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name=''),
    path('signup/', views.signup, name='signup'),
    path('post/', views.PostView.as_view(),name='post'),
    path('list/',views.listview,name='postlistview')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

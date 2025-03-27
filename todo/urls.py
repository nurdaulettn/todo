
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls'), name='tasks'),
    path('forum/', include('forum.urls')),
    path('shorter/', include('shorturls.urls'))


]

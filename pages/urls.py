from django.conf.urls import url
from pages import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path(r'<int:trin>g', views.visprojekter, name='firstyear'),
    path('projekter/3/Lixtal Beregner', include('LixCalc.urls')),
    path('projekter/<int:trin>/<title>', views.viewproject, name='projekter-url'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
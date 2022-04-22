from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from measurement.views import SensorView, SensorListView, MeasurementView


urlpatterns = [
    path('sensors/', SensorListView.as_view()),
    path('sensors/<int:pk>/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

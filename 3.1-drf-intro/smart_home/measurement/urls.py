from django.urls import path
from measurement.views import SensorView


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    # sensors/ POST(create sensor) RetrieveUpdate
    # sensors/<id>/ PATCH (update sensor) RetrieveUpdate
    # measurements/ POST (add measurement) CreateApiView
    # sensors/ GET (get info about sensors) ListCreate
    # sensors/<pk>/ (get sensor's info by id) RetrieveUpdate

    path('sensors/', SensorView.as_view()),

]

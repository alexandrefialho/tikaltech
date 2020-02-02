from django.urls import path
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from . import views

schema_view = get_swagger_view(title="Tikal Tech")

urlpatterns = [
    path('get-index/', views.get_index, name='index'),
    url(r'^$', schema_view)
]

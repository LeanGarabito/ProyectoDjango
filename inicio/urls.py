from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio),
    path("template/<nombre>/<apellido>/<int:edad>",views.template),
    path("template2/<nombre>/<apellido>/<int:edad>",views.template2),
    path("template3/<nombre>/<apellido>/<int:edad>",views.template3),
    path("template4/<nombre>/<apellido>/<int:edad>",views.template4),
    path("probando/",views.probando),
    path("autos/crear/<str:marca>/<str:modelo>", views.crear_auto)
]

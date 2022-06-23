from django.urls import path
from.  import views


urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('people',views.people),
    path('research_area',views.research_area),
    path('publication', views.publication),
    path('alumni', views.alumni),
    path('lab_life', views.lab_life),
    path('area_gis',views.area_gis),
    path('area_disaster',views.area_disaster),
    path('area_rs',views.area_rs),
    path('mj',views.mj),
    path('typhoon_1',views.typhoon_1),
    path('isolate_3', views.isolate_3),
    path('burstiness_1', views.burstiness_1),
    path('sink_6', views.sink_6),
    path('damage_7', views.damage_7),
    path('evacuation_8', views.evacuation_8),
    path('reallsolate_9', views.reallsolate_9),

    ]
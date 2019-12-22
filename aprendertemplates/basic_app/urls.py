from django.urls import path
from basic_app import views
# for template tagging
app_name = 'basic_app'

urlpatterns= [

path('relative', views.relative,name = 'relative'),
path('other',views.other,name = 'other'),
]

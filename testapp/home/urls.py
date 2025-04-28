from django.urls import path
from home.views import welcome, stock_analysis, alternate_medicine,upload_prescription, upload_medicine_image, side_effects, dashboard

urlpatterns = [
    path('welcome/', welcome, name='welcome'),
    path('stock_analysis/', stock_analysis, name='stock_analysis'),
    path('alternate_medicine/', alternate_medicine, name='alternate_medicine'),
    path('upload_prescription/', upload_prescription, name='upload_prescription'),
    path('upload_medicine_image/', upload_medicine_image, name='upload_medicine_image'),
     path('side_effects/', side_effects, name='side_effects'),
     path('dashboard/', dashboard, name='dashboard'),
]
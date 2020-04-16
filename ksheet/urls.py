from django.urls import path, include
from .views import *


app_name = 'ksheet'
urlpatterns = [
    path('', SheetListView.as_view(), name='sheet_list'),
    path('recruit/', RecruitTemplateView.as_view(), name='recruit'),
    path('<int:pk>/', SheetDetailView.as_view(), name='sheet_detail'),
    path('<int:pk>/trial/', TrialSheetDetailView.as_view(), name='trial_sheet_detail'),
    # ここ以下管理画面でいいや
    # path('new/', CreateSheetView.as_view(), name='create_sheet'),
    # path('update/<int:pk>/', UpdateSheetView.as_view(), name='update_sheet'),
    # path('delete/<int:pk>/', DeleteSheetView.as_view(), name='create_sheet'),
]


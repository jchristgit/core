from django.urls import path

from challengeserver import views

urlpatterns = [
    path('instance/<str:job_id>/', views.GetInstanceView.as_view(), name='get-instance'),
    path('reset/<str:job_id>/', views.ResetInstanceView.as_view(), name='request-new-instance'),
    path('jobs/', views.ListJobsView.as_view(), name='list-jobs'),
    path('restart/', views.RestartJobView.as_view(), name='restart-job'),
    path('instances/', views.ListInstancesView.as_view(), name='list-instances'),
    path('sysinfo/', views.SysinfoView.as_view(), name='view-sysinfo'),
]

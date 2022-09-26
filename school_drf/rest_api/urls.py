from django.urls import path
from .views import ExamView, ExamDetailView, TaskView, ExamTaskView, TaskDetalView, ExamTaskDetailView

urlpatterns = [
    path('exams/', ExamView.as_view(), name="exams"),
    path('exams/<int:pk>/', ExamDetailView.as_view(), name="exam"),
    path('exams/<int:pk>/tasks', ExamTaskView.as_view(), name="exam-task"),
    # path('exams/<int:pk>/tasks/<int:task_pk>/', ExamTaskDetailView.as_view(), name="exam-task"),
    path('tasks/', TaskView.as_view(), name="tasks"),
    path('tasks/<int:pk>', TaskDetalView.as_view(), name="task"),
]
from django.urls import path
from .views import (
    CourseUpdateView,
    CourseView,
    CourseListView,
    CourseCreateView,
    CourseDeleteView,
    #MyListView
    #my_fbv
)

app_name = 'course'
urlpatterns = [
    path('?', CourseView.as_view(template_name='contact.html'), name='course-list'),
    path('', CourseListView.as_view(), name='course-list'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    #path('', my_fbv, name='course-list'),
    path('<int:id>/', CourseView.as_view(), name='course-detail'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='course-delete'),
]
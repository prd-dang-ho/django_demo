from django.urls import path
from . import views

# Routers provide an easy way of automatically determining the URL conf.
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/result
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('snippets/', views.snippet_list),

    path('snippets/<int:pk>/', views.snippet_detail),
]

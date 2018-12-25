from django.urls import path

from . import views

urlpatterns = [
	 # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('hello/',views.hello),
    path('link2/',views.link2),
    path('link3/<int:num>/',views.link3),
    path('link4/<str:nome>/',views.link4),
    path('fname/<str:v_nome_2>/',views.fname),
    path('artigos/<str:nome_candango>',views.artigos),
    path('index_1/',views.principal),
    path('persons/',views.person_list, name='persons_list'),
    path('new/', views.person_new, name="person_new"),
    path('update/<int:id>',views.person_update, name="person_update"),
    path('delete/<int:id>',views.person_delete, name="person_delete")
]
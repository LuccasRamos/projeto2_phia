from django.urls import path

from .views import index
from .views import persons_list
from .views import persons_new
from .views import persons_delete
from .views import persons_update
from .views import servicelist
from .views import cesta

urlpatterns = [
    path('',index,name="index"),
    path('list/',persons_list,name="persons_list"),
    path('new/',persons_new,name="persons_new"),
    path('delete/<int:id_cliente>/',persons_delete,name="persons_delete"), 
    path('update/<int:id_cliente>/',persons_update,name="persons_update"),
    path('servicelist/',servicelist,name="servicelist"),
    path('cesta/',cesta,name="cesta"),
]
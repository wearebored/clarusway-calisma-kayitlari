from django.urls import path
from .views import *
### function based
# urlpatterns = [
#     path('',todo_list,name='todo_list' ),
#     path('add/',todo_add,name='todo_add' ),
#     path('update/<int:pk>',todo_update,name='todo_update' ),
#     path('delete/<int:pk>',todo_delete,name='todo_delete' ),
# ]

### class based
urlpatterns = [
    path('',TodoListView.as_view(),name='todo_list' ),
    path('add/',TodoCreateView.as_view(),name='todo_add' ),
    path('update/<int:pk>',TodoUpdateView.as_view(),name='todo_update' ),
    path('delete/<int:pk>',TodoDeleteView.as_view(),name='todo_delete' ),
    path('detail/<int:pk>', TodoDeleteView.as_view(), name="todo_detail"),

    

]
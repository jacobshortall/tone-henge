from django.urls import path
from . import views

urlpatterns = [
    path('add_comment/<product_id>', views.add_comment, name='add_comment'),
    path('delete_comment/<comment_id>',
         views.delete_comment, name='delete_comment'),
]

from django.urls import path
from review.views import show_review, add_review, see_book_review

app_name = 'review'

urlpatterns = [
  path('show-review/', show_review, name='show_review'),
  path('add-review/', add_review, name='add_review'),
  path('book-review/<int:id>/', see_book_review, name='book_review'),

#   path('login/', login_user, name='login'), 
#   path('logout/', logout_user, name='logout'),
]
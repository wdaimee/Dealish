from django.urls import path
from . import views

urlpatterns = [
    # Root redirect to Deals/
    path('', views.redirect_view, name='redirect'),
    # path to view a list of restaurants/deals in area
    path('deals/', views.deals_index, name='deals_index'),
    # path to view a restraurant's page
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    # create a review for a restaurant, login required
    path('restaurant/<int:restaurant_id>/review/add/', views.add_review, name='add_review'),
    # delete a review for a restaurant, only by user who created, login required
    path('restaurant/<int:restaurant>/review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    # edit a review for a restaurant, only by user who created, login required
    path('restaurant/<int:restaurant>/review/<int:review_id>/update/', views.update_review, name='update_review'),
    # Add a like to a resturant page, only one like per logged in user
    path('restaurant/<int:restaurant>/like/', views.add_like, name='add_like'),
    # Dislike a restaurant page, only one dislike per logged in user
    path('restaurant/<int:restaurant>/dislike/', views.dislike, name='dislike'),
    # view all favourite restaurants for a logged in user,
    path('user/<int:user_id>/favourites/', views.favourites_index, name='favourites_index'),
    # Add a restaurant to a user's favourites list
    path('user/<int:user_id>/add_favourite/<int:restaurant_id>/', views.add_favourite, name='add_favourite'),
    # remove a restaurant from a user's favourites list
    path('user/<int:user_id>/favourites/<int:restaurant_id>/delete/', views.delete_favourite, name='delete_favourite'),
    # add a note to a user's favourite restaurant
    path('user/<int:user_id>/favourites/<int:restaurant_id>/add_note/', views.add_note, name='add_note'),
    # Delete a note for a user's favourite restaurant
    path('user/<int:user_id>/favoutires/<int:restaurant_id/note/<int:note_id>/delete/', views.delete_note, name='delete_note'),
    # Edit a note for a user's favourite restaurant
    path('user/<int:user_id>/favourites/<int:restaurant_id>/note/<int:note_id>/update/', views.update_note, name='update_note'),
    # Sign up a new user
    path('accounts/signup/', views.signup, name='signup'),
]
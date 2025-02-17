from django.urls import path
from .views import SeatBookingView, BookSeatView, SeatListView

urlpatterns = [
    path('', SeatBookingView.as_view(), name='seat_booking'),
    path('book-seat/<int:seat_number>/', BookSeatView.as_view(), name='book_seat'),
    path('seats/', SeatListView.as_view(), name='seat_list'),
]

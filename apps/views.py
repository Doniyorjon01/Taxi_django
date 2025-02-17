from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views import View
from .models import Seat


class SeatBookingView(TemplateView):
    template_name = "space.html"  #


class BookSeatView(View):
    def post(self, request, seat_number):
        try:
            seat = Seat.objects.get(number=seat_number)
            if seat.is_booked:
                return JsonResponse({'success': False, 'message': 'O\'rindiq allaqachon band qilingan!'}, status=400)

            seat.is_booked = True
            seat.save()

            return JsonResponse({'success': True, 'message': f'{seat_number}-o\'rindiq band qilindi!'})
        except Seat.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Bunday o\'rindiq topilmadi!'}, status=404)


class SeatListView(View):
    def get(self, request):
        seats = Seat.objects.all().values('number', 'is_booked')
        return JsonResponse({'seats': list(seats)})

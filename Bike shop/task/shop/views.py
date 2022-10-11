from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.http import Http404

from . import models
from .forms import OrderForm


def bike_available(bike: models.Bike) -> bool:
    if bike.has_basket:
        if models.Basket.objects.filter(quantity__gt=0).first() is None:
            return False
    if bike.frame.quantity < 1 or bike.tire.quantity < 2 or bike.seat.quantity < 1:
        return False
    return True


class BikeListView(View):
    def get(self, request, *args, **kwargs):
        bikes = models.Bike.objects.all().values('name', 'id')
        context = {'bikes': bikes}
        return render(request, 'shop/bikeList.html', context=context)


class BikeDetailsView(TemplateView):
    template_name = 'shop/bikeDetails.html'

    def get_context_data(self, **kwargs):
        bike_id = kwargs.get('bike_id')
        try:
            bike = models.Bike.objects.get(id=bike_id)
        except models.Bike.DoesNotExist:
            raise Http404

        if bike.has_basket:
            bike.has_basket = 'yes'
        else:
            bike.has_basket = 'no'

        bike.available = bike_available(bike)

        context = super().get_context_data(**kwargs)
        context['bike'] = bike
        form = OrderForm()
        form.initial['bike'] = bike_id
        context['orderform'] = form
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = OrderForm(self.request.POST)
        if form.is_valid():
            order = form.save()

            frame = models.Frame.objects.get(id=order.bike.frame.id)
            frame.quantity -= 1
            frame.save()

            tire = models.Tire.objects.get(id=order.bike.tire.id)
            tire.quantity -= 2
            tire.save()

            seat = models.Seat.objects.get(id=order.bike.seat.id)
            seat.quantity -= 1
            seat.save()

            if order.bike.has_basket:
                basket = models.Basket.objects.filter(quantity__gt=0).first()
                basket.quantity -= 1
                basket.save()

            return redirect('order_confirmation', order.id)
        return render(request, self.template_name, {'orderform': form})


class OrderConfirmationView(DetailView):
    model = models.Order
    # template_name = 'shop/orderConfirmation.html'

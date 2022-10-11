from django.views import View
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import Http404

from . import models


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

        if (bike.has_basket == True):
            bike.has_basket = 'yes'
        else:
            bike.has_basket = 'no'

        context = super().get_context_data(**kwargs)
        context['bike'] = bike
        return context

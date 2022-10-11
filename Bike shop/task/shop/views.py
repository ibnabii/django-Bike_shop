from django.views import View
from django.shortcuts import render
from .models import Bike


class BikeListView(View):
    def get(self, request, *args, **kwargs):
        bikes = Bike.objects.all().values('name')
        context = {'bikes': bikes}
        return render(request, 'shop/bikeList.html', context=context)

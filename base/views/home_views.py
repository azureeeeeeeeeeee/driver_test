from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
from data.models import Driver, Rute, Transaksi
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
# from django.contrib.auth.decorators import login_required
from base.forms import DriverForm
from django.contrib import messages
from django.db.models import Sum, Count

def home(request):
    driver = Driver.objects.all()
    rute = Rute.objects.all()
    transaksi = Transaksi.objects.all()

    driver_telat = (
        Driver.objects.annotate(
            total_telat=Count('transaksi', filter=Q(transaksi__telat__gt=0))
        )
        .order_by('-total_telat')[:3]
    )

    cost_terbanyak = (
        Driver.objects.annotate(total_cost=Sum('transaksi__rute__total'))
        .order_by('-total_cost')[:3]
    )

    driver_terjauh = (
        Driver.objects.annotate(total_jarak=Sum('transaksi__rute__jarak'))
        .order_by('-total_jarak')[:3]
    )

    trip_per_driver = (
        Driver.objects.annotate(total_trip=Count('transaksi__id'))
        .order_by('-total_trip')
    )

    trip_labels = [d.nama for d in trip_per_driver]
    trip_data = [d.total_trip for d in trip_per_driver]

    revenue_labels = [d.nama for d in cost_terbanyak]
    revenue_data = [d.total_cost or 0 for d in cost_terbanyak]

    context = {
        'all_drivers': driver,
        'all_rute': rute,
        'all_transaksi': transaksi,
        'driver_telat': driver_telat,
        'cost_terbanyak': cost_terbanyak,
        'driver_terjauh': driver_terjauh,
        'trip_per_driver': trip_per_driver,
        'trip_labels': trip_labels,
        'trip_data': trip_data,
        'revenue_labels': revenue_labels,
        'revenue_data': revenue_data
    }

    return render(request, 'base/home.html', context)
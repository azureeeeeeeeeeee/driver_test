from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
from data.models import Driver, Rute, Transaksi
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import DriverForm, RuteForm, TransaksiForm
from django.contrib import messages

def home(request):
    # q = request.GET.get('q', '')
    drivers = Driver.objects.all()
    context = {'drivers': drivers}
    return render(request, 'base/home.html', context)

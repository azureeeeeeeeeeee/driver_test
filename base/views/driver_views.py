from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
from data.models import Driver, Rute, Transaksi
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
# from django.contrib.auth.decorators import login_required
from base.forms import DriverForm
from django.contrib import messages

def addDriver(request):
    form = DriverForm()
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Driver added successfully!')
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/driver/create_driver.html', context)

def updateDriver(request, pk):
    driver = Driver.objects.get(id=pk)
    form = DriverForm(instance=driver)
    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            messages.success(request, 'Driver updated successfully!')
            return redirect('home')
    context = {'form': form, 'driver': driver}
    return render(request, 'base/driver/update_driver.html', context)


def deleteDriver(request, pk):
    driver = Driver.objects.get(id=pk)
    driver.delete()
    messages.success(request, 'Driver deleted successfully!')
    return redirect('home')
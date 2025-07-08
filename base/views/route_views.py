from django.shortcuts import render, redirect
from data.models import Driver, Rute, Transaksi
from base.forms import RuteForm

def createRoutes(request):
    form = RuteForm()
    if request.method == 'POST':
        form = RuteForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.total = data.jarak * data.price_per_km
            data.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/rute/create_rute.html', context)

def updateRoutes(request, pk):
    rute = Rute.objects.get(id=pk)
    form = RuteForm(instance=rute)
    if request.method == 'POST':
        form = RuteForm(request.POST, instance=rute)
        if form.is_valid():
            data = form.save(commit=False)
            data.total = data.jarak * data.price_per_km
            data.save()
            return redirect('home')
    context = {'form': form, 'rute': rute}
    return render(request, 'base/rute/update_rute.html', context)

def deleteRoutes(request, pk):
    rute = Rute.objects.get(id=pk)
    rute.delete()
    return redirect('home')
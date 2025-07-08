from django.shortcuts import render, redirect
from base.forms import TransaksiForm
from data.models import Rute, Transaksi
from django.contrib import messages

def add_transaksi(request):
    if request.method == 'POST':
        form = TransaksiForm(request.POST)
        if form.is_valid():
            transaksi = form.save(commit=False)
            transaksi.telat = max(0, transaksi.waktu_asli - transaksi.rute.waktu_tempuh)
            transaksi.save()
            messages.success(request, 'Transaksi berhasil ditambahkan!')
            return redirect('home')
    else:
        form = TransaksiForm()

    return render(request, 'base/transaksi/create_transaksi.html', {'form': form})

def delete_transaksi(request, pk):
    transaksi = Transaksi.objects.get(id=pk)
    transaksi.delete()
    messages.success(request, 'Transaksi berhasil dihapus!')
    return redirect('home')
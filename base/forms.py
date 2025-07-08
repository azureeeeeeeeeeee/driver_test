from django.forms import ModelForm
from data.models import Driver, Rute, Transaksi
from django import forms


class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = ['nama', 'plat']
        labels = {
            'nama': 'Nama Driver',
            'plat': 'Plat Nomor'
        }

class RuteForm(ModelForm):
    class Meta:
        model = Rute
        fields = ['awal', 'tujuan', 'jarak', 'waktu_tempuh', 'price_per_km']
        labels = {
            'awal': 'Lokasi Awal',
            'tujuan': 'Lokasi Tujuan',
            'jarak': 'Jarak (km)',
            'waktu_tempuh': 'Waktu Tempuh (menit)',
            'price_per_km': 'Harga per km (IDR)'
        }

class TransaksiForm(forms.ModelForm):
    class Meta:
        model = Transaksi
        fields = ['driver', 'rute', 'waktu_asli']
        widgets = {
            'driver': forms.Select(attrs={'class': 'select select-bordered w-full'}),
            'rute': forms.Select(attrs={'class': 'select select-bordered w-full'}),
            'waktu_asli': forms.NumberInput(attrs={'class': 'input input-bordered w-full'}),
        }
from django.db import models

# Create your models here.
class Driver(models.Model):
    nama = models.CharField(max_length=100)
    plat = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nama} - {self.plat}"
    

class Rute(models.Model):
    awal = models.CharField(max_length=5)
    tujuan = models.CharField(max_length=5)
    jarak = models.IntegerField()
    waktu_tempuh = models.IntegerField()
    price_per_km = models.IntegerField()
    total = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.awal} to {self.tujuan} - {self.jarak} km, {self.waktu_tempuh} min, IDR {self.total}"


class Transaksi(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    rute = models.ForeignKey(Rute, on_delete=models.CASCADE)
    waktu_asli = models.PositiveIntegerField(default=0)
    telat = models.PositiveIntegerField()

    def __str__(self):
        return f"Transaksi: {self.driver} - {self.rute} at {self.waktu_asli} min, Telat: {self.telat} min"
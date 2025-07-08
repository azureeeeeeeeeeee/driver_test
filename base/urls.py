from django.urls import path
from base.views import driver_views, route_views, transaksi_views, home_views
from base.view import home

urlpatterns = [
    path('', home_views.home, name='home'),

    path('create_driver/', driver_views.addDriver, name='create_driver'),
    path('update_driver/<int:pk>/', driver_views.updateDriver, name='update_driver'),
    path('delete_driver/<int:pk>/', driver_views.deleteDriver, name='delete_driver'),

    path('create_rute/', route_views.createRoutes, name='create_rute'),
    path('update_rute/<int:pk>/', route_views.updateRoutes, name='update_rute'),
    path('delete_rute/<int:pk>/', route_views.deleteRoutes, name='delete_rute'),

    path('create_transaksi/', transaksi_views.add_transaksi, name='create_transaksi'),
    path('delete_transaksi/<int:pk>/', transaksi_views.delete_transaksi, name='delete_transaksi'),
]

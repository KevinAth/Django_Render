from django.urls import path
from . import views

# se establecen todos los urls para las vistas de la aplicacion appweb
urlpatterns = [
    path("",views.index,name="index"),
    path('ProductosCategoria/<int:categoria_id>',views.productosCategorias,name='prodxcat'),
    path('productosNombre' , views.productosNombre,name='prodxnom'),
    path('productoDetalle/<int:producto_id>',views.productodetalles,name='prodxdell'),
    path('carrito/',views.carrito,name='carrito'),
    path("carritoadd/<int:producto_id>",views.addcarrito,name='carrAdd'),
    path('carritodell/<int:producto_id>',views.delprod,name='delprod'),
    path('carritoclean',views.limpiarCarrito,name='clearCarr')
]
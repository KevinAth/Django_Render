from django.shortcuts import render, get_object_or_404,redirect
from .models import productos,Categoria
from .carrito import Cart
# Create your views here.


# vista que aparece al principio de la pagina web , renderiza el template 'index.html' y pasa todos los objetos del los modelos productos,Categortia.
def index(request):
    listprod = productos.objects.all()
    liscat = Categoria.objects.all()
    data = {
        'productos': listprod,
        'categorias': liscat
    }
    return render(request,"index.html",data)

# vista que filtra los productos segun su categoria haciendo uso de la relacion uno a muchos 
def  productosCategorias(request,categoria_id):
    objcategoria = Categoria.objects.get(pk=categoria_id)
    listprod = objcategoria.productos_set.all()
    print(listprod)
    
    listcat = Categoria.objects.all()
    
    data = {
        'productos': listprod,
        'categorias': listcat
    }
    
    return render(request, 'index.html',data)
    
# filtra los productos por el nombre en el motor de busqueda 
def productosNombre(request):
    nombre = request.POST['nombre']
    
    listprod = productos.objects.filter(nombre__contains=nombre)
    print(listprod)
    listcat = Categoria.objects.all()
    
    data = {
        'categorias': listcat,
        'productos': listprod
    }
    
    return render(request,'index.html',data)

# vistra que redirige al usuario a al template de detalles de productos: 'producto.html' y pasa los datos del modelo productos.
def productodetalles(request,producto_id):
    ##prod = productos.objects.get(pk=producto_id)
    prod = get_object_or_404(productos,pk=producto_id)
    data =  {
        'producto':prod
    }
    return render(request,'producto.html',data)
    
# renderiza el template de carrito de compras : 'carrito.html'
def carrito(request):
    return render(request,'carrito.html')

# añade productos al carrito de compras, realiza una solicitud del identificatorio del id   
def addcarrito(request,producto_id):
    
    # si el cliente hacer una solicitud con metodo post entonces la cantidad es igual al entero de la solicitud post del cliente de lo contrario la cantidad es igual a 1
    if request.method == 'POST':
        cantidad = int(request.POST['cantidad'])
    else:
        cantidad = 1  
    
    # obtiene el objeto producto del modelos productos por su id  
    objProducto = productos.objects.get(pk=producto_id)
    # crea una variable que almacena la clase Cart del modulo carrito.py
    carritoProducto = Cart(request)
    # llama al metodo add de la clase Cart y pasa los argumentos de objproducto y cantidad
    carritoProducto.add(objProducto,cantidad)
    
    if request.method == 'GET':
        return redirect('/')
    
    # renderiza el template 'carrito.html'
    return render(request,'carrito.html')
    
# Elimina el producto del carrito
def delprod(request,producto_id):
    # obtiene el objeto producto  del modelo productos por su id
    objProducto = productos.objects.get(pk=producto_id)
    # llama la clase Cart y pasa el argumento request y la guarda en la variable carritoProducto
    carritoProducto = Cart(request)
    # llama el metodo delete de la clase Cart y pasa el argumento objProducto
    carritoProducto.delete(objProducto)
    
    return render(request,'carrito.html') 

# llama al metodo clear de la clase Cart  y limpia el carrito 
def limpiarCarrito(request):
    carritoProductos = Cart(request)
    carritoProductos.clear()
    
    return render(request,'carrito.html')
    
    
    
    
    

# define una clase llamada Cart
class Cart:
    # inicializa la clase con el constructor __init__
    def __init__(self,request):
        # define una variable request con el argumento request
        self.request = request
        
        # define que session es igual a request.session
        self.session = request.session
        
        # obtiene de session (request.session) la varible cart
        cart = self.session.get("cart")
        # obtiene de session (request.session) la varible MontoTotal
        MontoTotal = self.session.get('MontoTotal')
        # si no existe cart realizar:
        if not cart:
            # si cart no exite cart es igual a self.session(request.session)['cart'] --> en la session crea una variable cart como un diccionario vacio
            cart= self.session['cart'] = {}
            print(request.session['cart'])
            # si cart no exite MontoTotal es igual a self.session(request.session)['MontoTotal'] --> en la session crea una variable cart como un entero 0
            MontoTotal = self.session['MontoTotal'] = 0
            print(request.session['MontoTotal'])
        # Define que self.cart es igual a cart
        self.cart = cart
        # Define que self.montoTotal es igual MontoTotal
        self.montoTotal = MontoTotal
    # define el metodo add que requiere 2 argumentos; producto y cantidad
    # el metodo añade productos al carrito de compras
    def add(self,producto,cantidad):
        # si el id del producto no esta en las claves del diccionario cart 
        if str(producto.id) not in self.cart.keys():
            # añade el id del producto como clave del diccionario y le da como valor un diccionario con variados datos del productos
            self.cart[producto.id] = {
                "producto_id":producto.id,
                'nombre': producto.nombre,
                'cantidad': cantidad,
                'precio':str(producto.precio),
                'imagen':producto.imagen.url,
                'categoria':producto.categoria.nombre,
                'subtotal':str(cantidad*producto.precio)
            }
        # si no se cumple la condicion if 
        else:
            # por cada clave y valor de los objectos del diccionario cart
            for key,value in self.cart.items():
                # el valor 'cantidad' es igual a la suma de la cantidad anterior con la cantidad actual
                value['cantidad'] = str(int(value['cantidad']) + cantidad)
                # el valor 'subtotal'' es igual a la cantidad por el precio del producto
                value['subtotal'] = str(float(value['cantidad']) * float(value['precio']))
                # rompe el bucle for
                break
                
        print(self.session['cart'])
        # llama al metodo save para guardar los cambios
        self.save()
        
    #  define el metodo delete que borra productos del carrito
    def delete(self,producto):
        # obitne el id del producto  como un entero
        producto_id = str(producto.id)
        # si el id del producto se encuentra en el diccionario cart
        if producto_id in self.cart:
            # si esta borrar el productos en el carrito con el id del producto dado
            del self.cart[producto_id]
            # guarda los cambios 
            self.save()
    
    # limpia el carrito combirtiendo el diccionario inicial a un diccionario vacio
    def clear(self):
        self.session['cart'] = {}
    
    # Gurarda los cambios realizados 
    def save(self):
        # define un montototal a 0
        montototal = 0
        
        # recorre los items del diccionario car
        for key , value in self.cart.items():
            # suma a montototal el subtotal de los productos  
            montototal += float(value['subtotal'])
        # guarda los datos en las variable correspondientes 
        self.session['MontoTotal'] = montototal
        self.session['cart'] = self.cart
        self.session.modified = True
        
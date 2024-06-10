from django.contrib import admin

# Register your models here.
from nucleoangel.models import Proveedor
from nucleoangel.models import Categoria
from nucleoangel.models import Producto
from nucleoangel.models import Caja
from nucleoangel.models import Empleado
from nucleoangel.models import Usuario
from nucleoangel.models import Factura
from nucleoangel.models import DetalleFactura
from nucleoangel.models import CajaEmpleado



# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Caja)
admin.site.register(Empleado)
admin.site.register(Usuario)
admin.site.register(Factura)
admin.site.register(DetalleFactura)
admin.site.register(CajaEmpleado)


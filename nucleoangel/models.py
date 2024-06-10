from django.db import models

# Create your models here.
from django.db import models

class Proveedor(models.Model):
    idProveedor = models.CharField(max_length=4, primary_key=True)
    ruc = models.CharField(max_length=13, unique=True)
    nombreProveedor = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    correo = models.EmailField(max_length=60, blank=True, null=True)

class Categoria(models.Model):
    idCategoria = models.CharField(max_length=4, primary_key=True)
    nombreCategoria = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=1, choices=(('A', 'Activo'), ('P', 'Pendiente')), default='A')

class Producto(models.Model):
    idProducto = models.CharField(max_length=4, primary_key=True)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    idProveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    nombreProducto = models.CharField(max_length=50, blank=True, null=True)
    fechaFabricacion = models.DateField(blank=True, null=True)
    fechaVencimiento = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()

class Caja(models.Model):
    idCaja = models.CharField(max_length=5, primary_key=True)
    numeroCaja = models.SmallIntegerField()
    fecHoraApertura = models.DateTimeField(blank=True, null=True)
    fecHoraCierre = models.DateTimeField(blank=True, null=True)

class Empleado(models.Model):
    idEmpleado = models.CharField(max_length=5, primary_key=True)
    clave = models.BinaryField(max_length=100)
    cargo = models.CharField(max_length=20)
    foto = models.CharField(max_length=30, blank=True, null=True)

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    correo = models.EmailField(max_length=60, blank=True, null=True)

class Factura(models.Model):
    numeroFactura = models.AutoField(primary_key=True)
    idCaja = models.ForeignKey(Caja, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    valorTotal = models.DecimalField(max_digits=6, decimal_places=2)
    impuesto = models.DecimalField(max_digits=6, decimal_places=2)
    descuento = models.DecimalField(max_digits=6, decimal_places=2)

class DetalleFactura(models.Model):
    idfacPro = models.AutoField(primary_key=True)
    numeroFactura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    iva = models.CharField(max_length=1, choices=(('S', 'Si'), ('N', 'No')))
    descuento = models.CharField(max_length=1, choices=(('S', 'Si'), ('N', 'No')))

class CajaEmpleado(models.Model):
    idCajaEmpleado = models.AutoField(primary_key=True)
    idCaja = models.ForeignKey(Caja, on_delete=models.CASCADE)
    idEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
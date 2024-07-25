# Generated by Django 5.0.4 on 2024-05-16 01:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('idCaja', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('numeroCaja', models.SmallIntegerField()),
                ('fecHoraApertura', models.DateTimeField(blank=True, null=True)),
                ('fecHoraCierre', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nombreCategoria', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('P', 'Pendiente')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('idEmpleado', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('clave', models.BinaryField(max_length=100)),
                ('cargo', models.CharField(max_length=20)),
                ('foto', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('idProveedor', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('ruc', models.CharField(max_length=13, unique=True)),
                ('nombreProveedor', models.CharField(max_length=50)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('direccion', models.CharField(blank=True, max_length=60, null=True)),
                ('correo', models.EmailField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CajaEmpleado',
            fields=[
                ('idCajaEmpleado', models.AutoField(primary_key=True, serialize=False)),
                ('idCaja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleoangel.caja')),
                ('idEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleoangel.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('numeroFactura', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('valorTotal', models.DecimalField(decimal_places=2, max_digits=6)),
                ('impuesto', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=6)),
                ('idCaja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleoangel.caja')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nombreProducto', models.CharField(blank=True, max_length=50, null=True)),
                ('fechaFabricacion', models.DateField(blank=True, null=True)),
                ('fechaVencimiento', models.DateField(blank=True, null=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stock', models.IntegerField()),
                ('idCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleoangel.categoria')),
                ('idProveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleoangel.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('idfacPro', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('iva', models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1)),
                ('descuento', models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1)),
                ('numeroFactura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleoangel.factura')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleoangel.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('direccion', models.CharField(blank=True, max_length=60, null=True)),
                ('correo', models.EmailField(blank=True, max_length=60, null=True)),
                ('idEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nucleoangel.empleado')),
            ],
        ),
    ]
from django.db import models

class Rol_Produccion(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=50)
    descripcion_rol = models.TextField()
    departamento = models.CharField(max_length=50)
    salario_promedio = models.DecimalField(max_digits=10, decimal_places=2)
    habilidades_requeridas = models.TextField()

    def __str__(self):
        return self.nombre_rol

class Miembro_Equipo(models.Model):
    id_miembro = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol_Produccion, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    especialidad_tecnica = models.CharField(max_length=100)
    disponibilidad = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Proyecto_Audiovisual(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    tipo_produccion = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin_estimada = models.DateField()
    presupuesto = models.DecimalField(max_digits=15, decimal_places=2)
    estado_proyecto = models.CharField(max_length=50)
    id_director = models.ForeignKey(Miembro_Equipo, on_delete=models.CASCADE)
    descripcion = models.TextField()
    distribucion_prevista = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Escena(models.Model):
    id_escena = models.AutoField(primary_key=True)
    id_proyecto = models.ForeignKey(Proyecto_Audiovisual, on_delete=models.CASCADE)
    numero_escena = models.IntegerField()
    descripcion_escena = models.TextField()
    localizacion = models.CharField(max_length=255)
    fecha_grabacion_estimada = models.DateField()
    hora_grabacion = models.TimeField()
    actores_involucrados = models.TextField()
    equipos_especiales = models.TextField()

    def __str__(self):
        return f"Escena {self.numero_escena} - {self.id_proyecto.titulo}"

class Material_Grabado(models.Model):
    id_material = models.AutoField(primary_key=True)
    id_escena = models.ForeignKey(Escena, on_delete=models.CASCADE)
    tipo_material = models.CharField(max_length=50)
    duracion_segundos = models.IntegerField()
    formato_archivo = models.CharField(max_length=20)
    fecha_grabacion_real = models.DateTimeField()
    ruta_almacenamiento = models.CharField(max_length=255)
    notas_tecnicas = models.TextField()
    version = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.tipo_material} - Escena {self.id_escena.numero_escena}"

class Presupuesto_Detalle(models.Model):
    id_item_presupuesto = models.AutoField(primary_key=True)
    id_proyecto = models.ForeignKey(Proyecto_Audiovisual, on_delete=models.CASCADE)
    categoria_gasto = models.CharField(max_length=100)
    descripcion_gasto = models.TextField()
    monto_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    monto_real = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_gasto = models.DateField()
    aprobado_por = models.CharField(max_length=100)
    tipo_moneda = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.categoria_gasto} - {self.id_proyecto.titulo}"

class Contrato_Talento(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    id_proyecto = models.ForeignKey(Proyecto_Audiovisual, on_delete=models.CASCADE)
    id_miembro = models.ForeignKey(Miembro_Equipo, on_delete=models.CASCADE)
    fecha_firma = models.DateField()
    salario_acordado = models.DecimalField(max_digits=10, decimal_places=2)
    clausulas_especiales = models.TextField()
    duracion_contrato = models.CharField(max_length=50)
    rol_especifico = models.CharField(max_length=100)

    def __str__(self):
        return f"Contrato de {self.id_miembro} para {self.id_proyecto.titulo}"

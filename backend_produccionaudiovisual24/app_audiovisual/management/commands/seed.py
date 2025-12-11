
from django.core.management.base import BaseCommand
from app_audiovisual.models import (
    Rol_Produccion,
    Miembro_Equipo,
    Proyecto_Audiovisual,
    Escena,
    Material_Grabado,
    Presupuesto_Detalle,
    Contrato_Talento,
)
import random
from datetime import date, time

class Command(BaseCommand):
    help = "Seeds the database with initial data."

    def handle(self, *args, **options):
        self.stdout.write("Seeding database...")

        # Create Rol_Produccion
        roles = []
        for i in range(3):
            rol = Rol_Produccion.objects.create(
                nombre_rol=f"Rol {i}",
                descripcion_rol=f"Descripción del rol {i}",
                departamento=f"Departamento {i}",
                salario_promedio=random.uniform(30000, 80000),
                habilidades_requeridas=f"Habilidades {i}",
            )
            roles.append(rol)

        # Create Miembro_Equipo
        miembros = []
        for i in range(3):
            miembro = Miembro_Equipo.objects.create(
                nombre=f"Nombre {i}",
                apellido=f"Apellido {i}",
                rol=random.choice(roles),
                email=f"miembro{i}@example.com",
                telefono=f"123-456-789{i}",
                fecha_contratacion=date.today(),
                salario_base=random.uniform(40000, 90000),
                especialidad_tecnica=f"Especialidad {i}",
                disponibilidad="Full-time",
            )
            miembros.append(miembro)

        # Create Proyecto_Audiovisual
        proyectos = []
        for i in range(3):
            proyecto = Proyecto_Audiovisual.objects.create(
                titulo=f"Proyecto {i}",
                tipo_produccion="Cine",
                fecha_inicio=date.today(),
                fecha_fin_estimada=date.today(),
                presupuesto=random.uniform(100000, 500000),
                estado_proyecto="En desarrollo",
                id_director=random.choice(miembros),
                descripcion=f"Descripción del proyecto {i}",
                distribucion_prevista="Cines",
            )
            proyectos.append(proyecto)

        # Create Escena
        escenas = []
        for i in range(3):
            escena = Escena.objects.create(
                id_proyecto=random.choice(proyectos),
                numero_escena=i + 1,
                descripcion_escena=f"Descripción de la escena {i}",
                localizacion=f"Localización {i}",
                fecha_grabacion_estimada=date.today(),
                hora_grabacion=time(10, 0, 0),
                actores_involucrados=f"Actor {i}",
                equipos_especiales="Ninguno",
            )
            escenas.append(escena)

        # Create Material_Grabado
        for i in range(3):
            Material_Grabado.objects.create(
                id_escena=random.choice(escenas),
                tipo_material="Video",
                duracion_segundos=random.randint(60, 300),
                formato_archivo="MP4",
                fecha_grabacion_real=date.today(),
                ruta_almacenamiento=f"/videos/escena_{i}.mp4",
                notas_tecnicas="Sin notas",
                version="1.0",
            )

        # Create Presupuesto_Detalle
        for i in range(3):
            Presupuesto_Detalle.objects.create(
                id_proyecto=random.choice(proyectos),
                categoria_gasto="Producción",
                descripcion_gasto=f"Gasto de producción {i}",
                monto_estimado=random.uniform(1000, 5000),
                monto_real=random.uniform(900, 6000),
                fecha_gasto=date.today(),
                aprobado_por="Director de Finanzas",
                tipo_moneda="USD",
            )

        # Create Contrato_Talento
        for i in range(3):
            Contrato_Talento.objects.create(
                id_proyecto=random.choice(proyectos),
                id_miembro=random.choice(miembros),
                fecha_firma=date.today(),
                salario_acordado=random.uniform(5000, 20000),
                clausulas_especiales="Ninguna",
                duracion_contrato="6 meses",
                rol_especifico="Protagonista",
            )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))


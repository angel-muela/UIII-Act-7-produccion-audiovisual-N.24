from django.urls import path
from . import views

urlpatterns = [
    # Rutas para Proyecto_Audiovisual
    path('proyectos/', views.ProyectoAudiovisualListView.as_view(), name='proyecto_list'),
    path('proyectos/nuevo/', views.ProyectoAudiovisualCreateView.as_view(), name='proyecto_create'),
    path('proyectos/editar/<int:pk>/', views.ProyectoAudiovisualUpdateView.as_view(), name='proyecto_update'),
    path('proyectos/eliminar/<int:pk>/', views.ProyectoAudiovisualDeleteView.as_view(), name='proyecto_delete'),

    # Rutas para Miembro_Equipo
    path('miembros/', views.MiembroEquipoListView.as_view(), name='miembro_list'),
    path('miembros/nuevo/', views.MiembroEquipoCreateView.as_view(), name='miembro_create'),
    path('miembros/editar/<int:pk>/', views.MiembroEquipoUpdateView.as_view(), name='miembro_update'),
    path('miembros/eliminar/<int:pk>/', views.MiembroEquipoDeleteView.as_view(), name='miembro_delete'),

    # Rutas para Rol_Produccion
    path('roles/', views.RolProduccionListView.as_view(), name='rol_list'),
    path('roles/nuevo/', views.RolProduccionCreateView.as_view(), name='rol_create'),
    path('roles/editar/<int:pk>/', views.RolProduccionUpdateView.as_view(), name='rol_update'),
    path('roles/eliminar/<int:pk>/', views.RolProduccionDeleteView.as_view(), name='rol_delete'),

    # Rutas para Escena
    path('escenas/', views.EscenaListView.as_view(), name='escena_list'),
    path('escenas/nuevo/', views.EscenaCreateView.as_view(), name='escena_create'),
    path('escenas/editar/<int:pk>/', views.EscenaUpdateView.as_view(), name='escena_update'),
    path('escenas/eliminar/<int:pk>/', views.EscenaDeleteView.as_view(), name='escena_delete'),

    # Rutas para Material_Grabado
    path('materiales/', views.MaterialGrabadoListView.as_view(), name='material_list'),
    path('materiales/nuevo/', views.MaterialGrabadoCreateView.as_view(), name='material_create'),
    path('materiales/editar/<int:pk>/', views.MaterialGrabadoUpdateView.as_view(), name='material_update'),
    path('materiales/eliminar/<int:pk>/', views.MaterialGrabadoDeleteView.as_view(), name='material_delete'),

    # Rutas para Presupuesto_Detalle
    path('presupuestos/', views.PresupuestoDetalleListView.as_view(), name='presupuesto_list'),
    path('presupuestos/nuevo/', views.PresupuestoDetalleCreateView.as_view(), name='presupuesto_create'),
    path('presupuestos/editar/<int:pk>/', views.PresupuestoDetalleUpdateView.as_view(), name='presupuesto_update'),
    path('presupuestos/eliminar/<int:pk>/', views.PresupuestoDetalleDeleteView.as_view(), name='presupuesto_delete'),

    # Rutas para Contrato_Talento
    path('contratos/', views.ContratoTalentoListView.as_view(), name='contrato_list'),
    path('contratos/nuevo/', views.ContratoTalentoCreateView.as_view(), name='contrato_create'),
    path('contratos/editar/<int:pk>/', views.ContratoTalentoUpdateView.as_view(), name='contrato_update'),
    path('contratos/eliminar/<int:pk>/', views.ContratoTalentoDeleteView.as_view(), name='contrato_delete'),
]
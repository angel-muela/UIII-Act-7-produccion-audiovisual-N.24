from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import (
    Proyecto_Audiovisual,
    Miembro_Equipo,
    Rol_Produccion,
    Escena,
    Material_Grabado,
    Presupuesto_Detalle,
    Contrato_Talento
)
from .forms import (
    ProyectoAudiovisualForm,
    MiembroEquipoForm,
    EscenaForm,
    MaterialGrabadoForm,
    PresupuestoDetalleForm,
    ContratoTalentoForm,
)

# Vista de Inicio
def inicio(request):
    return render(request, 'index.html')

# Vistas para Proyecto_Audiovisual
class ProyectoAudiovisualListView(ListView):
    model = Proyecto_Audiovisual
    template_name = 'app_audiovisual/proyecto_audiovisual_list.html'

class ProyectoAudiovisualCreateView(CreateView):
    model = Proyecto_Audiovisual
    form_class = ProyectoAudiovisualForm
    template_name = 'app_audiovisual/proyecto_audiovisual_form.html'
    success_url = reverse_lazy('proyecto_list')

class ProyectoAudiovisualUpdateView(UpdateView):
    model = Proyecto_Audiovisual
    form_class = ProyectoAudiovisualForm
    template_name = 'app_audiovisual/proyecto_audiovisual_form.html'
    success_url = reverse_lazy('proyecto_list')

class ProyectoAudiovisualDeleteView(DeleteView):
    model = Proyecto_Audiovisual
    template_name = 'app_audiovisual/proyecto_audiovisual_confirm_delete.html'
    success_url = reverse_lazy('proyecto_list')

# Vistas para Miembro_Equipo
class MiembroEquipoListView(ListView):
    model = Miembro_Equipo
    template_name = 'app_audiovisual/miembro_equipo_list.html'

class MiembroEquipoCreateView(CreateView):
    model = Miembro_Equipo
    form_class = MiembroEquipoForm
    template_name = 'app_audiovisual/miembro_equipo_form.html'
    success_url = reverse_lazy('miembro_list')

class MiembroEquipoUpdateView(UpdateView):
    model = Miembro_Equipo
    form_class = MiembroEquipoForm
    template_name = 'app_audiovisual/miembro_equipo_form.html'
    success_url = reverse_lazy('miembro_list')

class MiembroEquipoDeleteView(DeleteView):
    model = Miembro_Equipo
    template_name = 'app_audiovisual/miembro_equipo_confirm_delete.html'
    success_url = reverse_lazy('miembro_list')

# Vistas para Rol_Produccion
class RolProduccionListView(ListView):
    model = Rol_Produccion
    template_name = 'app_audiovisual/rol_produccion_list.html'

class RolProduccionCreateView(CreateView):
    model = Rol_Produccion
    fields = '__all__'
    template_name = 'app_audiovisual/rol_produccion_form.html'
    success_url = reverse_lazy('rol_list')

class RolProduccionUpdateView(UpdateView):
    model = Rol_Produccion
    fields = '__all__'
    template_name = 'app_audiovisual/rol_produccion_form.html'
    success_url = reverse_lazy('rol_list')

class RolProduccionDeleteView(DeleteView):
    model = Rol_Produccion
    template_name = 'app_audiovisual/rol_produccion_confirm_delete.html'
    success_url = reverse_lazy('rol_list')

# Vistas para Escena
class EscenaListView(ListView):
    model = Escena
    template_name = 'app_audiovisual/escena_list.html'

class EscenaCreateView(CreateView):
    model = Escena
    form_class = EscenaForm
    template_name = 'app_audiovisual/escena_form.html'
    success_url = reverse_lazy('escena_list')

class EscenaUpdateView(UpdateView):
    model = Escena
    form_class = EscenaForm
    template_name = 'app_audiovisual/escena_form.html'
    success_url = reverse_lazy('escena_list')

class EscenaDeleteView(DeleteView):
    model = Escena
    template_name = 'app_audiovisual/escena_confirm_delete.html'
    success_url = reverse_lazy('escena_list')

# Vistas para Material_Grabado
class MaterialGrabadoListView(ListView):
    model = Material_Grabado
    template_name = 'app_audiovisual/material_grabado_list.html'

class MaterialGrabadoCreateView(CreateView):
    model = Material_Grabado
    form_class = MaterialGrabadoForm
    template_name = 'app_audiovisual/material_grabado_form.html'
    success_url = reverse_lazy('material_list')

class MaterialGrabadoUpdateView(UpdateView):
    model = Material_Grabado
    form_class = MaterialGrabadoForm
    template_name = 'app_audiovisual/material_grabado_form.html'
    success_url = reverse_lazy('material_list')

class MaterialGrabadoDeleteView(DeleteView):
    model = Material_Grabado
    template_name = 'app_audiovisual/material_grabado_confirm_delete.html'
    success_url = reverse_lazy('material_list')

# Vistas para Presupuesto_Detalle
class PresupuestoDetalleListView(ListView):
    model = Presupuesto_Detalle
    template_name = 'app_audiovisual/presupuesto_detalle_list.html'

class PresupuestoDetalleCreateView(CreateView):
    model = Presupuesto_Detalle
    form_class = PresupuestoDetalleForm
    template_name = 'app_audiovisual/presupuesto_detalle_form.html'
    success_url = reverse_lazy('presupuesto_list')

class PresupuestoDetalleUpdateView(UpdateView):
    model = Presupuesto_Detalle
    form_class = PresupuestoDetalleForm
    template_name = 'app_audiovisual/presupuesto_detalle_form.html'
    success_url = reverse_lazy('presupuesto_list')

class PresupuestoDetalleDeleteView(DeleteView):
    model = Presupuesto_Detalle
    template_name = 'app_audiovisual/presupuesto_detalle_confirm_delete.html'
    success_url = reverse_lazy('presupuesto_list')

# Vistas para Contrato_Talento
class ContratoTalentoListView(ListView):
    model = Contrato_Talento
    template_name = 'app_audiovisual/contrato_talento_list.html'

class ContratoTalentoCreateView(CreateView):
    model = Contrato_Talento
    form_class = ContratoTalentoForm
    template_name = 'app_audiovisual/contrato_talento_form.html'
    success_url = reverse_lazy('contrato_list')

class ContratoTalentoUpdateView(UpdateView):
    model = Contrato_Talento
    form_class = ContratoTalentoForm
    template_name = 'app_audiovisual/contrato_talento_form.html'
    success_url = reverse_lazy('contrato_list')

class ContratoTalentoDeleteView(DeleteView):
    model = Contrato_Talento
    template_name = 'app_audiovisual/contrato_talento_confirm_delete.html'
    success_url = reverse_lazy('contrato_list')

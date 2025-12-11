
from django import forms
from .models import (
    Proyecto_Audiovisual,
    Miembro_Equipo,
    Escena,
    Material_Grabado,
    Presupuesto_Detalle,
    Contrato_Talento,
)

class ProyectoAudiovisualForm(forms.ModelForm):
    class Meta:
        model = Proyecto_Audiovisual
        fields = "__all__"
        widgets = {
            "fecha_inicio": forms.DateInput(attrs={"type": "date"}),
            "fecha_fin_estimada": forms.DateInput(attrs={"type": "date"}),
        }

class MiembroEquipoForm(forms.ModelForm):
    class Meta:
        model = Miembro_Equipo
        fields = "__all__"
        widgets = {
            "fecha_contratacion": forms.DateInput(attrs={"type": "date"}),
        }

class EscenaForm(forms.ModelForm):
    class Meta:
        model = Escena
        fields = "__all__"
        widgets = {
            "fecha_grabacion_estimada": forms.DateInput(attrs={"type": "date"}),
            "hora_grabacion": forms.TimeInput(attrs={"type": "time"}),
        }

class MaterialGrabadoForm(forms.ModelForm):
    class Meta:
        model = Material_Grabado
        fields = "__all__"
        widgets = {
            "fecha_grabacion_real": forms.DateInput(attrs={"type": "date"}),
        }

class PresupuestoDetalleForm(forms.ModelForm):
    class Meta:
        model = Presupuesto_Detalle
        fields = "__all__"
        widgets = {
            "fecha_gasto": forms.DateInput(attrs={"type": "date"}),
        }

class ContratoTalentoForm(forms.ModelForm):
    class Meta:
        model = Contrato_Talento
        fields = "__all__"
        widgets = {
            "fecha_firma": forms.DateInput(attrs={"type": "date"}),
        }

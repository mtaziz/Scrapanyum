from django.forms import ModelForm, TextInput, Textarea
from models import Business, Batch, Client, BrandReportInstance


class BrandReportInstanceForm(ModelForm):
    class Meta:
        model = BrandReportInstance
        fields = ['business_name', 'tripadvisor_url', 'google_url', 'facebook_url']
        widgets = {
            'tripadvisor_url': TextInput(
                attrs={'id': 'tripadvisor_url_field', 'placeholder': 'URL de Trip Advisor'}
            ),
            'google_url': TextInput(
                attrs={'id': 'google_url_field', 'placeholder': 'URL de Google Reviews'}
            ),
            'facebook_url': TextInput(
                attrs={'id': 'facebook_url_field', 'placeholder': 'URL de Facebook'}
            ),
        }


class BusinessForm(ModelForm):
    class Meta:
        model = Business
        fields = ['client', 'brand', 'NIF', 'owner_name', 'business_address', 'business_telephone', 'business_email', 'web_url']
        widgets = {
            'brand': TextInput(
                attrs={'id': 'brand_field', 'placeholder': 'Nombre de la empresa'}
            ),
            'NIF': TextInput(
                attrs={'id': 'NIF_field', 'placeholder': 'Numero de Identificacion Fiscal'}
            ),
            'owner_name': TextInput(
                attrs={'id': 'owner_name_field', 'placeholder': 'Nombre Persona de Contacto'}
            ),
            'business_address': TextInput(
                attrs={'id': 'business_address_field', 'placeholder': 'Direccion'}
            ),
            'business_telephone': TextInput(
                attrs={'id': 'business_telephone_field', 'placeholder': 'telefono de contacto'}
            ),
            'business_email': TextInput(
                attrs={'id': 'business_email_field', 'placeholder': 'Correo Electronico'}
            ),
            'web_url': TextInput(
                attrs={'id': 'web_url_field', 'placeholder': 'Pagina Web'}
            ),
        }


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['DNI', 'name', 'address', 'telephone', 'email', 'legalitas_id']
        widgets = {
            'DNI': TextInput(
                attrs={'id': 'DNI_field', 'placeholder': 'Documento de Identificacion'}
            ),
            'name': TextInput(
                attrs={'id': 'name_field', 'placeholder': 'Nombre del Cliente'}
            ),
            'address': TextInput(
                attrs={'id': 'address_field', 'placeholder': 'Direccion'}
            ),
            'telephone': TextInput(
                attrs={'id': 'telephone_field', 'placeholder': 'Numero de telefono'}
            ),
            'email': TextInput(
                attrs={'id': 'email_field', 'placeholder': 'Direccion de Email'}
            ),
            'legalitas_id': TextInput(
                attrs={'id': 'legalitas_id_field', 'placeholder': 'Documento de Identificacion'}
            ),
        }


class BatchForm(ModelForm):
    class Meta:
        model = Batch
        fields = ['start', 'end']

        widgets = {
            'start': TextInput(
                attrs={'id': 'start_field', 'placeholder': 'Fecha de Entrada'}

            ),
            'end': TextInput(
                attrs={'id': 'end_field', 'placeholder': 'Fecha de Salida'}

            ),
        }



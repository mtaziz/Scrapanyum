import json

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

from Core.forms import BatchForm
from Core.forms import BrandReportInstanceForm
from Core.forms import BusinessForm
from Core.forms import ClientForm
from Core.models import BrandReportInstance
from Proxifier.models import ProxifierInstance
from .models import Client, Business, Batch


def dashboard(request):
    client_form = ClientForm()
    business_form = BusinessForm()
    batch_form = BatchForm()
    brand_report_instance_form = BrandReportInstanceForm()

    import uuid
    alert_hash = uuid.uuid1().hex
    batch_list = Batch.objects.all()

    return render(request, 'home.html', {
        'batch_list': batch_list,
        'client_form': client_form,
        'business_form': business_form,
        'batch_form': batch_form,
        'brand_report_instance_form': brand_report_instance_form,
        'alert_hash': alert_hash
    })


def refresh_client(request):
    search = request.GET.get("search")
    client_list = Client.objects.filter(name__startswith=search)

    return render_to_response('clients.html', {'client_list': client_list})


def refresh_business(request):
    search = request.GET.get("search")
    business_list = Business.objects.filter(brand__startswith=search)

    return render_to_response('business.html', {'business_list': business_list})


# AJAX endpoint for new client
def create_client_ajax(request):
    if request.method == 'POST':
        response_data = {}
        client = Client(
            DNI=request.POST.get('DNI'),
            name=request.POST.get('name'),
            address=request.POST.get('address'),
            telephone=request.POST.get('telephone'),
            email=request.POST.get('email'),
            legalitas_id=request.POST.get('legalitas_id'),
        )
        client.save()

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


# AJAX endpoint for deleting clients
def delete_client_ajax(request):
    if request.method == 'POST':
        response_data = {}
        client_id = request.POST.get('client_id').strip()
        client = Client.objects.get(name=client_id)
        client.delete()
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


# AJAX endpoint for new business
def create_business_ajax(request):
    if request.method == 'POST':
        response_data = {}
        print request.POST
        client = Client.objects.get(id=request.POST.get('client'))
        business = Business(
            client=client,
            brand=request.POST.get('brand'),
            NIF=request.POST.get('NIF'),
            owner_name=request.POST.get('owner_name'),
            business_address=request.POST.get('business_address'),
            business_telephone=request.POST.get('business_telephone'),
            business_email=request.POST.get('business_email'),
            web_url=request.POST.get('web_url'),
        )
        business.save()
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


# AJAX endpoint for deleting businesss
def delete_business_ajax(request):
    if request.method == 'POST':
        response_data = {}
        business_id = request.POST.get('business_id').strip()
        business = Business.objects.get(brand=business_id)
        business.delete()
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


# AJAX endpoint to create the batch
def create_batch_ajax(request):
    print "wiki"
    try:
        if request.method == 'POST':
            response_data = {}
            client = Client.objects.get(name=request.POST.get('client').strip())

            batch = Batch(
                client=client,
                start=request.POST.get('start'),
                end=request.POST.get('end'),
            )

            type = request.POST.get('instance_type')

            if type == "idm":
                idm = BrandReportInstance(
                    google_url=request.POST.get('google'),
                    tripadvisor_url=request.POST.get('trip_advisor'),
                    facebook_url=request.POST.get('facebook'),
                    business_name=request.POST.get('business').strip()
                )
                idm.save()
                business = Business.objects.get(brand=request.POST.get('business').strip())
                batch.business = business
                batch.product_type = "IDM"
                batch.product_instance = "idm_" + str(idm.id)

            batch.save()

            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
        else:
            return HttpResponse(
                json.dumps({"nothing to see": "this isn't happening"}),
                content_type="application/json"
            )
    except Exception as e:
        print e.message
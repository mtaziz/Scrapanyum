from django.shortcuts import render

from Scraper.models import TripAdvisorReview
from Scraper.models import GoogleReview
from Core.models import BrandReportInstance
from Core.models import Batch


def trip_manager_view(request):
    results_trip = TripAdvisorReview.objects.all()
    results_google = GoogleReview.objects.all()

    return render(request, 'scraper_manager.html', {'results_google': results_google,
                                                    'results_trip': results_trip})


def task_scheduler_view(request):
    batch_list = Batch.objects.filter(status="pending", product_type="IDM")
    pending_reports = []
    wip_reports = []
    done_reports = []

    for batch in batch_list:
        report_id = batch.product_instance.replace("idm_", "")
        report = BrandReportInstance.objects.get(id=report_id)
        pending_reports.append({"name": batch.business.brand, "report": report})

    wip_list = Batch.objects.filter(status="wip", product_type="IDM")
    for batch in wip_list:
        report_id = batch.product_instance.replace("idm_", "")
        report = BrandReportInstance.objects.get(id=report_id)
        wip_reports.append({"name": batch.business.brand, "report": report})

    done_list = Batch.objects.filter(status="done", product_type="IDM")
    for batch in done_list:
        report_id = batch.product_instance.replace("idm_", "")
        report = BrandReportInstance.objects.get(id=report_id)
        done_reports.append({"name": batch.business.brand, "report": report})

    return render(request, 'task_scheduler.html', {"pending_reports": pending_reports,
                                              "wip_reports": wip_reports,
                                              "done_reports": done_reports})


def generate_AJAX(request):
    index = request.GET['index']
    if int(index) == 0:
        time_delay = datetime.datetime.utcnow() + timedelta(seconds=1 * (int(index)))
    else:
        time_delay = datetime.datetime.utcnow() + timedelta(minutes=10 * (int(index)))
    report_id = request.GET['report_id']
    batch = Batch.objects.get(product_instance="idm_" + report_id)
    report = BrandReportInstance.objects.get(id=report_id)

    schedule_report_job(report, batch.business, batch, time_delay, report_id)
    # report_generator_aux.generate(report, batch.business, batch)

    return HttpResponse(status=200)
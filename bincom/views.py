from django.utils import timezone
from django.db.models import Sum
from django.shortcuts import render, redirect
from bincom.models import AnnouncedPuResults, PollingUnit
from django.views.generic import View


def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid


def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class PollingUnitResultView(View):
    def get(self, request, *args, **kwargs):
        ...
        polling_unit = AnnouncedPuResults.objects.filter(
            polling_unit_uniqueid__isnull=False).values('polling_unit_uniqueid')
        pu_ids = []
        for item in polling_unit:
            pu_id_to_int = int(item['polling_unit_uniqueid'])
            pu_ids.append(pu_id_to_int)
        polling_unit = list(set(pu_ids))
        polling_unit.sort()

        context = {
            'polling_unit': polling_unit,

        }
        return render(request, 'select_polling_unit.html', context)

    def post(self, request, *args, **kwargs):
        ...
        # get the poll id via form submit
        poll_id = request.POST.get('poll_id')
        print(poll_id)
        # filter by the poll id
        polling_unit_data = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=poll_id)
        if polling_unit_data:

            context = {
                'polling_unit_data': polling_unit_data,

            }
            return render(request, 'polling_result.html', context)
        return render(request, 'polling_result.html',)


class SummedPollingUnitResultView(View):
    def get(self, request, *args, **kwargs):
        ...
        polling_unit = AnnouncedPuResults.objects.filter(
            polling_unit_uniqueid__isnull=False).values('polling_unit_uniqueid')
        pu_ids = []
        for item in polling_unit:
            pu_id_to_int = int(item['polling_unit_uniqueid'])
            pu_ids.append(pu_id_to_int)
        polling_unit = list(set(pu_ids))
        polling_unit.sort()

        context = {
            'polling_unit': polling_unit,

        }
        return render(request, 'select_polling_unit.html', context)

    def post(self, request, *args, **kwargs):
        ...
        # get the poll id via form submit
        poll_id = request.POST.get('poll_id')
        print(poll_id)
        # filter by the poll id
        polling_unit_data = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=poll_id)
        if polling_unit_data:
            pollling_unit_info = PollingUnit.objects.filter(polling_unit_id=poll_id).first()
            polling_unit_data = polling_unit_data.aggregate(total_score=Sum('party_score'))
            print(polling_unit_data)

            context = {
                'polling_unit_data': polling_unit_data,
                'poll_id': poll_id,
                'pollling_unit_info': pollling_unit_info,

            }
            return render(request, 'polling_unit_sum.html', context)
        # An error message can be dropped here
        return render(request, 'polling_unit_sum.html',)


class AddNewPollingUnit(View):

    def get(self, request, *args, **kwargs):
        ...

        return render(request, 'add_polling_unit.html',)

    def post(self, request, *args, **kwargs):
        # get form data
        uniqueid = request.POST.get('uniqueid')
        polling_unit_id = request.POST.get('polling_unit_id')
        ward_id = request.POST.get('ward_id')
        lga_id = request.POST.get('lga_id')
        uniquewardid = request.POST.get('uniquewardid')
        polling_unit_number = request.POST.get('polling_unit_number')
        polling_unit_name = request.POST.get('polling_unit_name')
        polling_unit_description = request.POST.get('polling_unit_description')
        lat = request.POST.get('lat')
        long = request.POST.get('long')
        form_data = ['polling_unit_id',
                     'ward_id',
                     'lga_id',
                     'uniquewardid',
                     'polling_unit_number',
                     'polling_unit_name',
                     'polling_unit_description',
                     'lat',
                     'long',
                     'form_data']
        valid_data = is_valid_form(form_data)
        if valid_data:
            try:
                PollingUnit.objects.create(
                    uniqueid=uniqueid,
                    entered_by_user=request.user,
                    date_entered=timezone.now(),
                    user_ip_address=get_user_ip(request),
                    lga_id=lga_id,
                    polling_unit_id=polling_unit_id,
                    ward_id=ward_id,
                    uniquewardid=uniquewardid,
                    polling_unit_number=polling_unit_number,
                    polling_unit_name=polling_unit_name,
                    polling_unit_description=polling_unit_description,
                    lat=lat,
                    long=long,
                )

                # A success message here message can be dropped here
                return render('add-unit',)
            except ValueError:

                # An error message, please fill out the required field
                return redirect('add-unit')
            # An error message, please fill out the required field
        return redirect('add-unit',)

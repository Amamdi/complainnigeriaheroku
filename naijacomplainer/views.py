from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ComplainerForm, DateForm
from .models import Complainer
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.contrib.auth.models import User
from django.db.models import Count, F, Sum, Avg
from django.db.models.functions import ExtractYear, ExtractMonth
from util.charts import months, get_year_dict
from datetime import datetime

# Create your views here.


BACKGROUND_COLOR = [
    'rgba(255, 99, 132, 0.2)',
    'rgba(54, 162, 235, 0.2)',
    'rgba(255, 206, 86, 0.2)',
    'rgba(75, 192, 192, 0.2)',
    'rgba(153, 102, 255, 0.2)',
    'rgba(255, 159, 64, 0.2)',
    'rgba(256, 100, 14, 0.2)',
    'rgba(55, 163, 236, 0.2)',
    'rgba(257, 207, 87, 0.2)',
    'rgba(76, 193, 193, 0.2)',
    'rgba(154, 103, 256, 0.2)',
    'rgba(256, 160, 65, 0.2)',
    'rgba(257, 101, 133, 0.2)',
    'rgba(56, 164, 237, 0.2)',
    'rgba(258, 208, 88, 0.2)',
    'rgba(77, 194, 194, 0.2)',
    'rgba(155, 104, 257, 0.2)',
    'rgba(259, 160, 66, 0.2)',
    'rgba(260, 104, 134, 0.2)',
    'rgba(57, 166, 239, 0.2)',
    'rgba(260, 210, 88, 0.2)',
    'rgba(77, 196, 194, 0.2)',
    'rgba(156, 106, 259, 0.2)',
    'rgba(261, 161, 67, 0.2)',
    'rgba(262, 102, 134, 0.2)',
    'rgba(59, 166, 240, 0.2)',
    'rgba(263, 208, 88, 0.2)',
    'rgba(79, 198, 194, 0.2)',
    'rgba(159, 108, 260, 0.2)',
    'rgba(265, 161, 66, 0.2)',
    'rgba(268, 102, 136, 0.2)',
    'rgba(60, 168, 241, 0.2)',
    'rgba(270, 210, 90, 0.2)',
    'rgba(80, 200, 196, 0.2)',
    'rgba(160, 104, 264, 0.2)',
    'rgba(272, 211, 65, 0.2)'
]
borderColor = [
    'rgba(255, 99, 132, 1)',
    'rgba(54, 162, 235, 1)',
    'rgba(255, 206, 86, 1)',
    'rgba(75, 192, 192, 1)',
    'rgba(153, 102, 255, 1)',
    'rgba(255, 159, 64, 1)',
    'rgba(255, 99, 132, 1)',
    'rgba(54, 162, 235, 1)',
    'rgba(255, 206, 86, 1)',
    'rgba(75, 192, 192, 1)',
    'rgba(153, 102, 255, 1)',
    'rgba(255, 159, 64, 1)',
    'rgba(255, 99, 132, 1)',
    'rgba(54, 162, 235, 1)',
    'rgba(255, 206, 86, 1)',
    'rgba(75, 192, 192, 1)',
    'rgba(153, 102, 255, 1)',
    'rgba(255, 159, 64, 1)',
    'rgba(255, 99, 132, 1)',
    'rgba(54, 162, 235, 1)',
    'rgba(255, 206, 86, 1)',
    'rgba(75, 192, 192, 1)',
    'rgba(153, 102, 255, 1)',
    'rgba(255, 159, 64, 1)',
    'rgba(255, 99, 132, 1)',
    'rgba(54, 162, 235, 1)',
    'rgba(255, 206, 86, 1)',
    'rgba(75, 192, 192, 1)',
    'rgba(153, 102, 255, 1)',
    'rgba(255, 159, 64, 1)',
    'rgba(255, 99, 132, 1)',
    'rgba(54, 162, 235, 1)',
    'rgba(255, 206, 86, 1)',
    'rgba(75, 192, 192, 1)',
    'rgba(153, 102, 255, 1)',
    'rgba(255, 159, 64, 1)',
]
borderWidth = ['1']


@login_required
def emp(request):
    # print(request.POST)
    if request.method == "POST":
        form = ComplainerForm(request.POST)
        if form.is_valid():
            try:
                # print(request)
                # form.save()
                instance = form.save()
                instance.user = request.user
                instance.save()
                # form.save(user=request.user)
                # return HttpResponse('Complaint successfully submitted')
                # (request, 'index.html', {'form': form})
                # i only added the code below
                # however if you want to use redirect, you have to add it above
                # then change the httpresponse below to redirect
                return redirect('/success/')
                # ensure you add success to your url
                # eg. path('success/', views.success, name='success'),
            except:
                pass
    elif request.method == "GET":
        form = ComplainerForm(request.GET)
        lists = Complainer.objects.filter(user=request.user)

        query = request.GET.get('q')
        submitbutton = request.GET.get('submit')
        if query is not None:
            try:
                lookups = Q(date__icontains=query) | Q(state__icontains=query) | Q(state=query) | Q(
                    complaintIsAgainst__icontains=query) | Q(natureOfComplaint__icontains=query) | Q(
                    complaint__icontains=query) | Q(firstname__icontains=query) | Q(lastname__icontains=query)
                results = Complainer.objects.filter(lookups, user=request.user).distinct()
                context = {'results': results, 'submitbutton': submitbutton}
                return render(request, 'index2.html', context)

            except:
                return render(request, 'index2.html', {'form': form, 'lists': lists})
        # for list in lists:
        #     print(list.date)
        return render(request, 'index2.html', {'form': form, 'lists': lists})
    else:
        return render(request, 'index2.html', {'form': form, 'lists': lists})


# def employee_detail(request, employee_id):
#     try:
#         employee = Employee.objects.get(id=employee_id)
#     except Employee.DoesNotExist:
#         raise Http404("Employee does not exist")
#     return render(request, 'employee_detail.html', {'employee': employee})


def dashboard(request):
    lists = Complainer.objects.all()
    return render(request, "dashboard.html", {'lists': lists})


def edit(request, id):
    complainer = Complainer.objects.get(id=id, user=request.user)
    return render(request, 'edit.html', {'complainer': complainer})


def update(request, id):
    complainer = Complainer.objects.get(id=id, user=request.user)
    form = ComplainerForm(request.POST, instance=complainer)
    # print('update')
    if form.is_valid():
        # print(form)
        # form.save()
        instance = form.save()
        instance.user = request.user
        instance.save()
        return redirect("/index2/")
    # print(form.errors)
    # print(request.POST)
    return render(request, 'edit.html', {'complainer': complainer, 'form': form})


def destroy(request, id):
    complainer = Complainer.objects.get(id=id, user=request.user)
    complainer.delete()
    return redirect("/index2/")


def index(request):
    return render(request, 'index.html')


def success(request):
    return render(request, 'success.html')


# def user(request):
#     lists = Complainer.objects.filter(user=request.user)
#     return render(request, 'index.html', {'lists': lists})


# def success(request):
#     return HttpResponse('Complaint successfully submitted')


def searchposts(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(date__icontains=query) | Q(firstname__icontains=query) | Q(lastname__icontains=query) | Q(
                state__icontains=query) | Q(complaintIsAgainst__icontains=query) | Q(
                natureOfComplaint__icontains=query) | Q(complaint__icontains=query)

            results = Complainer.objects.filter(lookups).distinct()
            # sorted_count = Complainer.objects.filter(lookups).annotate(count=Count(lookups))
            context = {'results': results, 'submitbutton': submitbutton}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100
    }
    return JsonResponse(data)


# def get_filter_options(request):
#     lists = Complainer.objects.annotate(year=ExtractYear('date')).values('year').order_by('-year').distinct()
#     options = [complaint['year'] for complaint in lists]
#
#     return JsonResponse({
#         'options': options,
#     })


# ------------- CHANGES INSIDE THIS CLASS ---------------
class HomeView(View):
    def get(self, request, *args, **kwargs):
        sorted_list_state = Complainer.objects.values("state").annotate(count=Count('state')).order_by('-count')[:5]
        sorted_list_nature = Complainer.objects.values("natureOfComplaint").annotate(
            count=Count('natureOfComplaint')).order_by('-count')[:5]

        date_form = DateForm()
        context = {"sorted_list_state": sorted_list_state, "sorted_list_nature": sorted_list_nature, "form": date_form}

        return render(request, 'chart.html', context)

    def sort_states(self, item):
        return item.get("count")

    def sort_nature(self, item):
        return item.get("count")

    def post(self, request, *args, **kwargs):
        # sorted_list_state = Complainer.objects.values("state").annotate(count=Count('state')).order_by('-count')[:5]
        # sorted_list_nature = Complainer.objects.values("natureOfComplaint").annotate(count=Count('natureOfComplaint')).order_by('-count')[:5]

        date_form = DateForm()
        context = {"sorted_list_state": '', "sorted_list_nature": '', "form": date_form}

        date = request.POST.get("date")

        # ----------- CHANGE START ------------
        if date:
            date_split = date.split(" ")
            date_array = date_split[0].split("/")
            year = int(date_array[2])
            month = int(date_array[1])
            day = int(date_array[0])
            qs_1 = Complainer.objects.filter(date__year=year, date__month=month, date__day=day)
        else:
            qs_1 = Complainer.objects.all()

        # ------------ CHANGE END --------------
        qs_2 = qs_1.values("state").annotate(count=Count('state'))
        qs_3 = qs_1.values("natureOfComplaint").annotate(count=Count('natureOfComplaint'))
        states_by_count = dict()
        nature_by_count = dict()
        # states_by_count = get_year_dict()
        for r in qs_2:

            if states_by_count.get(r.get("state")):
                states_by_count[r.get("state")] += 1
                continue
            states_by_count[r.get("state")] = 1
        sorted_list_state = [{"state": k, "count": v} for k, v in states_by_count.items()]
        sorted_list_state.sort(key=self.sort_states, reverse=True)
        context["sorted_list_state"] = sorted_list_state[:5]

        for r in qs_3:

            if nature_by_count.get(r.get("natureOfComplaint")):
                nature_by_count[r.get("natureOfComplaint")] += 1
                continue
            nature_by_count[r.get("natureOfComplaint")] = 1
        sorted_list_nature = [{"natureOfComplaint": k, "count": v} for k, v in nature_by_count.items()]
        sorted_list_nature.sort(key=self.sort_states, reverse=True)
        context["sorted_list_nature"] = sorted_list_nature[:5]

        # print(request.POST)
        # print(sorted_list_state)
        # print(sorted_list_nature)
        # print(type(date))
        # print(date)
        # date_split = date.split(" ")
        # date_array = date_split[0].split("/")
        # year = int(date_array[2])
        # month = int(date_array[1])
        # date_obj = datetime.strptime(date, '%d-%m-%Y %H:%M')
        # print(date_obj)
        # print(year)
        # print(month)
        # print(states_by_count)
        print("I am returning")
        context["filter_date"] = date
        return render(request, 'chart.html', context)

        # THIS CODE IS WORKING
        # date_form = DateForm()
        # context = {"sorted_list_state":'', "sorted_list_nature": '', "form": date_form}
        #
        # date = request.POST.get("date")
        # date_split = date.split(" ")
        # date_array = date_split[0].split("/")
        # year = int(date_array[2])
        # month = int(date_array[1])
        # qs_1 = Complainer.objects.filter(date__year=year, date__month=month)
        # qs_2 = qs_1.values("state").annotate(count=Count('state'))
        # states_by_count = dict()
        # #states_by_count = get_year_dict()
        # for r in qs_2:
        #
        #     if states_by_count.get(r.get("state")):
        #         states_by_count[r.get("state")] += 1
        #         continue
        #     states_by_count[r.get("state")] = 1
        # sorted_list_state = [{"state": k, "count": v} for k,v in states_by_count.items()]
        # sorted_list_state.sort(key=self.sort_states, reverse=True)
        # context["sorted_list_state"] = sorted_list_state[:5]
        # # print(request.POST)
        # # print(sorted_list_state)
        # # print(sorted_list_nature)
        # # print(type(date))
        # # print(date)
        # # date_split = date.split(" ")
        # # date_array = date_split[0].split("/")
        # # year = int(date_array[2])
        # # month = int(date_array[1])
        # # date_obj = datetime.strptime(date, '%d-%m-%Y %H:%M')
        # # print(date_obj)
        # # print(year)
        # # print(month)
        # print( states_by_count)
        #
        # return render(request, 'chart.html', context)


# THIS CODE BELOW IS WORKING
#     def get(self, request, *args, **kwargs):
#         year = 2021
#         month = 2
#         qs_1 = Complainer.objects.filter(date__year=year)
#         qs_2 = qs_1.values("state").annotate(count=Count('state'))
#         states_by_count = dict()
#         #states_by_count = get_year_dict()
#         for r in qs_2:
#             if states_by_count.get(r.get("state")):
#                 states_by_count[r.get("state")] += 1
#                 continue
#             states_by_count[r.get("state")] = 1
#
#         return JsonResponse({
#             'title': f'Complainers in {year} month {month}',
#             'data': {
#                 'labels': list(states_by_count.keys()),
#                 'datasets': [{
#                     'label': 'state',
#                     'data': list(states_by_count.values()),
#                 }]
#             },
#         })


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        lookupsAbia = Q(state__icontains='Abia')
        lookupsAbuja = Q(state__icontains='Abuja')
        lookupsAdamawa = Q(state__icontains='Adamawa')
        lookupsAkwaIbom = Q(state__icontains='Akwa-Ibom')
        lookupsAnambra = Q(state__icontains='Anambra')
        lookupsBauchi = Q(state__icontains='Bauchi')
        lookupsBayelsa = Q(state__icontains='Bayelsa')
        lookupsBenue = Q(state__icontains='Benue')
        lookupsBorno = Q(state__icontains='Borno')
        lookupsCrossRiver = Q(state__icontains='Cross-River')
        lookupsDelta = Q(state__icontains='Delta')
        lookupsEbonyi = Q(state__icontains='Ebonyi')
        lookupsEdo = Q(state__icontains='Edo')
        lookupsEkiti = Q(state__icontains='Ekiti')
        lookupsEnugu = Q(state__icontains='Enugu')
        lookupsGombe = Q(state__icontains='Gombe')
        lookupsImo = Q(state__icontains='Imo')
        lookupsJigawa = Q(state__icontains='Jigawa')
        lookupsKaduna = Q(state__icontains='Kaduna')
        lookupsKano = Q(state__icontains='Kano')
        lookupsKatsina = Q(state__icontains='Katsina')
        lookupsKebbi = Q(state__icontains='Kebbi')
        lookupsKogi = Q(state__icontains='Kogi')
        lookupsKwara = Q(state__icontains='Kwara')
        lookupsLagos = Q(state__icontains='lagos')
        lookupsNasarawa = Q(state__icontains='Nasarawa')
        lookupsNiger = Q(state__icontains='Niger')
        lookupsOgun = Q(state__icontains='Ogun')
        lookupsOndo = Q(state__icontains='Ondo')
        lookupsOsun = Q(state__icontains='Osun')
        lookupsOyo = Q(state__icontains='Oyo')
        lookupsPlateau = Q(state__icontains='Plateau')
        lookupsRivers = Q(state__icontains='Rivers')
        lookupsSokoto = Q(state__icontains='Sokoto')
        lookupsTaraba = Q(state__icontains='Taraba')
        lookupsYobe = Q(state__icontains='Yobe')
        lookupsZamfara = Q(state__icontains='Zamfara')

        abia_count = Complainer.objects.filter(lookupsAbia).distinct().count()
        abuja_count = Complainer.objects.filter(lookupsAbuja).distinct().count()
        adamawa_count = Complainer.objects.filter(lookupsAdamawa).distinct().count()
        akwaibom_count = Complainer.objects.filter(lookupsAkwaIbom).distinct().count()
        anambra_count = Complainer.objects.filter(lookupsAnambra).distinct().count()
        bauchi_count = Complainer.objects.filter(lookupsBauchi).distinct().count()
        bayelsa_count = Complainer.objects.filter(lookupsBayelsa).distinct().count()
        benue_count = Complainer.objects.filter(lookupsBenue).distinct().count()
        borno_count = Complainer.objects.filter(lookupsBorno).distinct().count()
        crossriver_count = Complainer.objects.filter(lookupsCrossRiver).distinct().count()
        delta_count = Complainer.objects.filter(lookupsDelta).distinct().count()
        ebonyi_count = Complainer.objects.filter(lookupsEbonyi).distinct().count()
        edo_count = Complainer.objects.filter(lookupsEdo).distinct().count()
        ekiti_count = Complainer.objects.filter(lookupsEkiti).distinct().count()
        enugu_count = Complainer.objects.filter(lookupsEnugu).distinct().count()
        gombe_count = Complainer.objects.filter(lookupsGombe).distinct().count()
        imo_count = Complainer.objects.filter(lookupsImo).distinct().count()
        jigawa_count = Complainer.objects.filter(lookupsJigawa).distinct().count()
        kaduna_count = Complainer.objects.filter(lookupsKaduna).distinct().count()
        kano_count = Complainer.objects.filter(lookupsKano).distinct().count()
        katsina_count = Complainer.objects.filter(lookupsKatsina).distinct().count()
        kebbi_count = Complainer.objects.filter(lookupsKebbi).distinct().count()
        kogi_count = Complainer.objects.filter(lookupsKogi).distinct().count()
        kwara_count = Complainer.objects.filter(lookupsKwara).distinct().count()
        lagos_count = Complainer.objects.filter(lookupsLagos).distinct().count()
        nasarawa_count = Complainer.objects.filter(lookupsNasarawa).distinct().count()
        niger_count = Complainer.objects.filter(lookupsNiger).distinct().count()
        ogun_count = Complainer.objects.filter(lookupsOgun).distinct().count()
        ondo_count = Complainer.objects.filter(lookupsOndo).distinct().count()
        osun_count = Complainer.objects.filter(lookupsOsun).distinct().count()
        oyo_count = Complainer.objects.filter(lookupsOyo).distinct().count()
        plateau_count = Complainer.objects.filter(lookupsPlateau).distinct().count()
        rivers_count = Complainer.objects.filter(lookupsRivers).distinct().count()
        sokoto_count = Complainer.objects.filter(lookupsSokoto).distinct().count()
        taraba_count = Complainer.objects.filter(lookupsTaraba).distinct().count()
        yobe_count = Complainer.objects.filter(lookupsYobe).distinct().count()
        zamfara_count = Complainer.objects.filter(lookupsZamfara).distinct().count()

        labels = ['Abia', 'Abuja', 'Adamawa', 'Akwa-Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno',
                  'Cross-river', 'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'Gombe', 'Imo', 'Jigawa', 'Kaduna', 'Kano',
                  'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun', 'Ondo', 'Osun', 'Oyo',
                  'Plateau', 'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara']
        default_items = [abia_count, abuja_count, adamawa_count, akwaibom_count, anambra_count, bauchi_count,
                         bayelsa_count, benue_count, borno_count, crossriver_count, delta_count, ebonyi_count,
                         edo_count, ekiti_count, enugu_count, gombe_count, imo_count, jigawa_count, kaduna_count,
                         kano_count, katsina_count, kebbi_count, kogi_count, kwara_count, lagos_count, nasarawa_count,
                         niger_count, ogun_count, ondo_count, osun_count, oyo_count, plateau_count, rivers_count,
                         sokoto_count, taraba_count, yobe_count, zamfara_count]
        # date_form = DateForm() "form": date_form
        complaint = {'labels': labels, 'default': default_items}
        return Response(complaint)


class ChartData2(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None, ):
        lookupsFederalGovernment = Q(complaintIsAgainst__icontains='Federal Government')
        lookupsStateGovernment = Q(complaintIsAgainst__icontains='State Government')
        lookupsLocalGovernment = Q(complaintIsAgainst__icontains='Local Government')
        lookupsPrivateCompany = Q(complaintIsAgainst__icontains='Private Company')
        lookupsPublicCompany = Q(complaintIsAgainst__icontains='Public Company')
        lookupsOther = Q(complaintIsAgainst__icontains='Other')

        federal_count = Complainer.objects.filter(lookupsFederalGovernment).distinct().count()
        state_count = Complainer.objects.filter(lookupsStateGovernment).distinct().count()
        local_count = Complainer.objects.filter(lookupsLocalGovernment).distinct().count()
        private_count = Complainer.objects.filter(lookupsPrivateCompany).distinct().count()
        public_count = Complainer.objects.filter(lookupsPublicCompany).distinct().count()
        other_count = Complainer.objects.filter(lookupsOther).distinct().count()

        labels = ['Public Company', 'Private Company', 'Local Government', 'State Government', 'Federal Government',
                  'Other']
        default_items = [public_count, private_count, local_count, state_count, federal_count, other_count]
        complaint = {'labels': labels, 'default': default_items}
        return Response(complaint)


class ChartData3(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None, ):
        lookupsDelayOfService = Q(natureOfComplaint__icontains='Delay of Service')
        lookupsVandalism = Q(natureOfComplaint__icontains='Vandalism')
        lookupsCompliance = Q(natureOfComplaint__icontains='Non compliance with Regulation')
        lookupsBribery = Q(natureOfComplaint__icontains='Demand for Bribery')
        lookupsInfrastructure = Q(natureOfComplaint__icontains='Unrepaired or Damaged Infrastructure')
        lookupsInsecurity = Q(natureOfComplaint__icontains='Insecurity')
        lookupsSalary = Q(natureOfComplaint__icontains='Non payment of salary')
        lookupsOther = Q(natureOfComplaint__icontains='Other')

        delay_count = Complainer.objects.filter(lookupsDelayOfService).distinct().count()
        vandalism_count = Complainer.objects.filter(lookupsVandalism).distinct().count()
        compliance_count = Complainer.objects.filter(lookupsCompliance).distinct().count()
        bribery_count = Complainer.objects.filter(lookupsBribery).distinct().count()
        infrastructure_count = Complainer.objects.filter(lookupsInfrastructure).distinct().count()
        insecurity_count = Complainer.objects.filter(lookupsInsecurity).distinct().count()
        salary_count = Complainer.objects.filter(lookupsSalary).distinct().count()
        other_count = Complainer.objects.filter(lookupsOther).distinct().count()

        labels = ['Delay of Service', 'Vandalism', 'Non compliance with Regulation', 'Demand for Bribery',
                  'Unrepaired or Damaged Infrastructure', 'Insecurity', 'Non payment of salary', 'Other']
        default_items = [delay_count, vandalism_count, compliance_count, bribery_count, infrastructure_count,
                         insecurity_count, salary_count, other_count]
        complaint = {'labels': labels, 'default': default_items}
        return Response(complaint)


# ------------- CHANGES INSIDE THIS CLASS ---------------

class PieChartView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def sort_states(self, item):
        return item.get("count")

    def sort_nature(self, item):
        return item.get("count")

    def post(self, request, *args, **kwargs):
        # sorted_list_state = Complainer.objects.values("state").annotate(count=Count('state')).order_by('-count')[:5]
        # sorted_list_nature = Complainer.objects.values("natureOfComplaint").annotate(count=Count('natureOfComplaint')).order_by('-count')[:5]

        date = request.data.get("date")

        # ----------- CHANGE START ------------

        if date:
            date_split = date.split(" ")
            date_array = date_split[0].split("/")
            year = int(date_array[2])
            month = int(date_array[1])
            day = int(date_array[0])
            qs_1 = Complainer.objects.filter(date__year=year, date__month=month, date__day=day)
        else:
            qs_1 = Complainer.objects.all()

        # ----------- CHANGE END ------------

        qs_2 = qs_1.values("state").annotate(count=Count('state'))
        qs_3 = qs_1.values("natureOfComplaint").annotate(count=Count('natureOfComplaint'))
        states_by_count = dict()
        nature_by_count = dict()
        # states_by_count = get_year_dict()
        for r in qs_2:

            if states_by_count.get(r.get("state")):
                states_by_count[r.get("state")] += 1
                continue
            states_by_count[r.get("state")] = 1
        sorted_list_state = [{"state": k, "count": v} for k, v in states_by_count.items()]
        sorted_list_state.sort(key=self.sort_states, reverse=True)
        context = dict()
        context["sorted_list_state"] = sorted_list_state

        for r in qs_3:

            if nature_by_count.get(r.get("natureOfComplaint")):
                nature_by_count[r.get("natureOfComplaint")] += 1
                continue
            nature_by_count[r.get("natureOfComplaint")] = 1
        sorted_list_nature = [{"natureOfComplaint": k, "count": v} for k, v in nature_by_count.items()]

        sorted_list_nature.sort(key=self.sort_states, reverse=True)

        labels = [k for k, v in nature_by_count.items()]
        context["labels"] = labels
        context["datasets"] = [
            {
                "label": 'Number of complaints according to defaulter',
                "data": [v for k, v in nature_by_count.items()],
                "backgroundColor": BACKGROUND_COLOR[:len(labels)],
                "borderColor": borderColor[:len(labels)],
                "borderWidth": borderWidth[:len(labels)]
            }
        ]
        context["sorted_list_nature"] = sorted_list_nature

        print("I am returning")
        print("this was called")
        context["filter_date"] = date
        return Response(context, status=status.HTTP_200_OK)


# ------------- CHANGES INSIDE THIS CLASS ---------------

class AreaChartView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def sort_defaulters(self, item):
        return item.get("count")

    def sort_nature(self, item):
        return item.get("count")

    def post(self, request, *args, **kwargs):
        # sorted_list_state = Complainer.objects.values("state").annotate(count=Count('state')).order_by('-count')[:5]
        # sorted_list_nature = Complainer.objects.values("natureOfComplaint").annotate(count=Count('natureOfComplaint')).order_by('-count')[:5]

        date = request.data.get("date")

        # ----------- CHANGE START ------------

        if date:
            date_split = date.split(" ")
            date_array = date_split[0].split("/")
            year = int(date_array[2])
            month = int(date_array[1])
            day = int(date_array[0])
            qs_1 = Complainer.objects.filter(date__year=year, date__month=month, date__day=day)
        else:
            qs_1 = Complainer.objects.all()

        # ----------- CHANGE END ------------

        qs_2 = qs_1.values("complaintIsAgainst").annotate(count=Count('complaintIsAgainst'))

        defaulters_by_count = dict()
        nature_by_count = dict()
        # states_by_count = get_year_dict()
        for r in qs_2:

            if defaulters_by_count.get(r.get("complaintIsAgainst")):
                defaulters_by_count[r.get("complaintIsAgainst")] += 1
                continue
            defaulters_by_count[r.get("complaintIsAgainst")] = 1
        sorted_list_defaulters = [{"complaintIsAgainst": k, "count": v} for k, v in defaulters_by_count.items()]
        sorted_list_defaulters.sort(key=self.sort_defaulters, reverse=True)
        context = dict()
        context["sorted_list_defaulters"] = sorted_list_defaulters

        # for r in qs_3:

        #     if nature_by_count.get(r.get("natureOfComplaint")):
        #         nature_by_count[r.get("natureOfComplaint")] += 1
        #         continue
        #     nature_by_count[r.get("natureOfComplaint")] = 1
        # sorted_list_nature = [{"natureOfComplaint": k, "count": v} for k, v in nature_by_count.items()]
        #
        # sorted_list_nature.sort(key=self.sort_states, reverse=True)

        labels = [k for k, v in defaulters_by_count.items()]
        context["labels"] = labels
        context["datasets"] = [
            {
                "label": 'Number of complaints according to defaulter',
                "data": [v for k, v in defaulters_by_count.items()],
                "backgroundColor": BACKGROUND_COLOR[:len(labels)],
                "borderColor": borderColor[:len(labels)],
                "borderWidth": borderWidth[:len(labels)]
            }
        ]
        context["sorted_list_defaulters"] = sorted_list_defaulters

        print("I am returning")
        print("this was called")
        context["filter_date"] = date
        return Response(context, status=status.HTTP_200_OK)


# ------------- CHANGES INSIDE THIS CLASS ---------------

class BarChartView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def sort_states(self, item):
        return item.get("count")

    def sort_nature(self, item):
        return item.get("count")

    def post(self, request, *args, **kwargs):
        # sorted_list_state = Complainer.objects.values("state").annotate(count=Count('state')).order_by('-count')[:5]
        # sorted_list_nature = Complainer.objects.values("natureOfComplaint").annotate(count=Count('natureOfComplaint')).order_by('-count')[:5]

        date = request.data.get("date")

        # ----------- CHANGE START ------------

        if date:
            date_split = date.split(" ")
            date_array = date_split[0].split("/")
            year = int(date_array[2])
            month = int(date_array[1])
            day = int(date_array[0])
            qs_1 = Complainer.objects.filter(date__year=year, date__month=month, date__day=day)
        else:
            qs_1 = Complainer.objects.all()

        # ----------- CHANGE END ------------

        qs_2 = qs_1.values("state").annotate(count=Count('state'))

        states_by_count = dict()
        nature_by_count = dict()
        # states_by_count = get_year_dict()
        for r in qs_2:

            if states_by_count.get(r.get("state")):
                states_by_count[r.get("state")] += 1
                continue
            states_by_count[r.get("state")] = 1
        sorted_list_state = [{"state": k, "count": v} for k, v in states_by_count.items()]
        sorted_list_state.sort(key=self.sort_states, reverse=True)
        context = dict()
        context["sorted_list_state"] = sorted_list_state

        # for r in qs_3:
        #
        #     if nature_by_count.get(r.get("natureOfComplaint")):
        #         nature_by_count[r.get("natureOfComplaint")] += 1
        #         continue
        #     nature_by_count[r.get("natureOfComplaint")] = 1
        # sorted_list_nature = [{"natureOfComplaint": k, "count": v} for k, v in nature_by_count.items()]
        #
        # sorted_list_nature.sort(key=self.sort_states, reverse=True)

        labels = [k for k, v in states_by_count.items()]
        context["labels"] = labels
        context["datasets"] = [
            {
                "label": 'Number of complaints according to states',
                "data": [v for k, v in states_by_count.items()],
                "backgroundColor": BACKGROUND_COLOR[:len(labels)],
                # "borderColor": borderColor[:len(labels)],
                # "borderWidth": borderWidth[:len(labels)]
            }
        ]
        context["sorted_list_state"] = sorted_list_state

        print("I am returning")
        print("this was called")
        context["filter_date"] = date
        return Response(context, status=status.HTTP_200_OK)












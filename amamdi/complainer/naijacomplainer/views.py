from django.shortcuts import render, redirect  
from django.http import HttpResponse
from .forms import ComplainerForm  
from .models import Complainer  
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.db.models import Count
# Create your views here.


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
                #(request, 'index.html', {'form': form})
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
                return render(request, 'index.html', context)

            except:
                return render(request, 'index.html', {'form': form, 'lists': lists})
        # for list in lists:
        #     print(list.date)
        return render(request, 'index.html', {'form': form, 'lists': lists})
    else:
        return render(request, 'index.html', {'form': form, 'lists': lists})


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
        return redirect("/index/")
    # print(form.errors)
    # print(request.POST)
    return render(request, 'edit.html', {'complainer': complainer, 'form': form})


def destroy(request, id):
    complainer = Complainer.objects.get(id=id, user=request.user)
    complainer.delete()
    return redirect("/index/")


def base(request):
    return render(request, 'Base.html')


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
            lookups = Q(date__icontains=query) | Q(firstname__icontains=query) | Q(lastname__icontains=query) | Q(state__icontains=query) | Q(complaintIsAgainst__icontains=query) | Q(natureOfComplaint__icontains=query) | Q(complaint__icontains=query)

            results = Complainer.objects.filter(lookups).distinct()
            # sorted_count = Complainer.objects.filter(lookups).annotate(count=Count(lookups))
            context = {'results': results, 'submitbutton': submitbutton}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')


class HomeView(View):
    def get(self, request, *args, **kwargs):
        sorted_list_state = Complainer.objects.values("state").annotate(count=Count('state')).order_by('-count')[:5]
        sorted_list_nature = Complainer.objects.values("natureOfComplaint").annotate(count=Count('natureOfComplaint')).order_by('-count')[:5]

        context = {"sorted_list_state": sorted_list_state, "sorted_list_nature": sorted_list_nature}

        return render(request, 'chart.html', context)


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100
    }
    return JsonResponse(data)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None,):
        # date = [date.date for date in Complainer.objects.all()]
        # firstname = [firstname.firstname for firstname in Complainer.objects.all()]
        # lastname = [lastname.lastname for lastname in Complainer.objects.all()]
        # context = {'date': date}
        # date_count = Complainer.objects.filter(date).count()
        # firstname_count = Complainer.objects.filter(firstname=firstname).count()
        # qs_count = Complainer.objects.all().count()
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

        labels = ['Abia', 'Abuja', 'Adamawa', 'Akwa-Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno', 'Cross-river', 'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'Gombe', 'Imo', 'Jigawa', 'Kaduna', 'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun', 'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara']
        default_items = [abia_count, abuja_count, adamawa_count, akwaibom_count, anambra_count, bauchi_count, bayelsa_count, benue_count, borno_count, crossriver_count, delta_count, ebonyi_count, edo_count, ekiti_count, enugu_count, gombe_count, imo_count, jigawa_count, kaduna_count, kano_count, katsina_count, kebbi_count, kogi_count, kwara_count, lagos_count, nasarawa_count, niger_count, ogun_count, ondo_count, osun_count, oyo_count, plateau_count, rivers_count, sokoto_count, taraba_count, yobe_count, zamfara_count]
        complaint = {'labels': labels, 'default': default_items}
        return Response(complaint)

        # usernames = [user.username for user in User.objects.all()]
        # return Response(usernames)


class ChartData2(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None,):
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

        labels = ['Public Company', 'Private Company', 'Local Government', 'State Government', 'Federal Government', 'Other']
        default_items = [public_count, private_count, local_count, state_count, federal_count, other_count]
        complaint = {'labels': labels, 'default': default_items}
        return Response(complaint)


class ChartData3(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None,):
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

        labels = ['Delay of Service', 'Vandalism', 'Non compliance with Regulation', 'Demand for Bribery', 'Unrepaired or Damaged Infrastructure', 'Insecurity', 'Non payment of salary', 'Other']
        default_items = [delay_count, vandalism_count, compliance_count, bribery_count, infrastructure_count, insecurity_count, salary_count, other_count]
        complaint = {'labels': labels, 'default': default_items}
        return Response(complaint)


def map(request):
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

        Region = ['Abia', 'Abuja', 'Adamawa', 'Akwa-Ibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Benue', 'Borno', 'Cross-river',
                  'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'Gombe', 'Imo', 'Jigawa', 'Kaduna', 'Kano', 'Katsina',
                  'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun', 'Ondo', 'Osun', 'Oyo', 'Plateau',
                  'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara']
        default_items = [abia_count, abuja_count, adamawa_count, akwaibom_count, anambra_count, bauchi_count, bayelsa_count,
                         benue_count, borno_count, crossriver_count, delta_count, ebonyi_count, edo_count, ekiti_count,
                         enugu_count, gombe_count, imo_count, jigawa_count, kaduna_count, kano_count, katsina_count,
                         kebbi_count, kogi_count, kwara_count, lagos_count, nasarawa_count, niger_count, ogun_count,
                         ondo_count, osun_count, oyo_count, plateau_count, rivers_count, sokoto_count, taraba_count,
                         yobe_count, zamfara_count]
        complaint = {'Region': Region, 'default': default_items}
        # return Response(complaint)
        return render(request, 'vectorMap.html', complaint)


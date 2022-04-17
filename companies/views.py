from django.shortcuts import render
from . import models
import json

from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    pass


@csrf_exempt
def item_filtering(request, pk):
    if request.method == "POST":
        # 여기에 if 문걸어서 받아온 값 걸러서 필터링 조건 다시 세워야함
        # test = models.Company.objects.filter(pk=pk).filter(sections__pk=1)
        print(request.POST.get("type"))
        section = models.Section.objects.all()
        section_json = serializers.serialize("json", section)
        section_json_load = json.loads(section_json)
        if request.POST.get("type") == "row":
            section_filter = [
                x for x in section_json_load if -50 < x["fields"]["temperature"] <= 25
            ]
            filtering_data = json.dumps(section_filter)
            return HttpResponse(content=filtering_data)
        elif request.POST.get("type") == "nomal":
            section_filter = [
                x for x in section_json_load if 26 <= x["fields"]["temperature"] <= 50
            ]
            filtering_data = json.dumps(section_filter)
            return HttpResponse(content=filtering_data)

        elif request.POST.get("type") == "high":
            section_filter = [
                x for x in section_json_load if 51 <= x["fields"]["temperature"] <= 99
            ]
            filtering_data = json.dumps(section_filter)
            return HttpResponse(content=filtering_data)
        else:
            pass

    elif request.method == "GET":
        company = models.Company.objects.all()
        return render(
            request,
            "companies/company_list.html",
            context={"company": company},
        )


@csrf_exempt
def company_detail(request, pk):
    if request.method == "POST":
        item_id = json.loads(request.body)
        company_all = models.Company.objects.filter(company_list__name="포스코")
        sections = models.Section.objects.all().filter(pk=item_id)
        item_data = serializers.serialize("json", sections)
        company_all_data = serializers.serialize("json", company_all)
        response = HttpResponse(
            json.dumps({"item_data": item_data, "company_all_data": company_all_data})
        )
        return response

    elif request.method == "GET":
        company = models.Company.objects.get(pk=pk)
        return render(
            request,
            "companies/company_detail.html",
            context={"company": company},
        )

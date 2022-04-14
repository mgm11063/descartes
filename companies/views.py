from django.shortcuts import render
from . import models
import json

from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def company_list(request):
    if request.method == "POST":

        # 여기에 if 문걸어서 받아온 값 걸러서 필터링 조건 다시 세워야함
        print(
            request,
            "asdfadsfjaisdfkjafijosiojpijpjiopiohuiuhjkioi111111212313131232131231231232",
        )
        section = models.Section.objects.all()
        section_json = serializers.serialize("json", section)
        section_json_load = json.loads(section_json)
        section_filter = [
            x for x in section_json_load if x["fields"]["temperature"] < 20
        ]
        filtering_data = json.dumps(section_filter)
        return HttpResponse(content=filtering_data)

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
        sections = models.Section.objects.all().filter(pk=item_id)
        item_data = serializers.serialize("json", sections)

        response = HttpResponse(content=item_data)
        return response

    elif request.method == "GET":
        company = models.Company.objects.get(pk=pk)
        return render(
            request,
            "companies/company_detail.html",
            context={"company": company},
        )

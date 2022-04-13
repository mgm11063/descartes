from django.shortcuts import render
from . import models
import json
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

# def company_detail(request, pk):
#     company = models.Company.objects.get(pk=pk)

#     return render(
#         request,
#         "companies/company_detail.html",
#         context={"company": company},
#     )


@csrf_exempt
def company_detail(request, pk):
    if request.method == "POST":
        data = json.loads(request.body)
        # do something
        print(data)

        context = {
            "result": data,
        }
        return JsonResponse(context)

    elif request.method == "GET":
        company = models.Company.objects.get(pk=pk)
        return render(
            request,
            "companies/company_detail.html",
            context={"company": company},
        )

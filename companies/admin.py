from django.contrib import admin
from .models import Company, Section, CompanyList, RiskFactor


class SectionAdmin(admin.StackedInline):
    list_display = ("id",)
    extra = 1
    model = Section


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "company_list", "year")
    search_fields = ("year",)

    inlines = [SectionAdmin]


@admin.register(CompanyList)
class CompanyListAdmin(admin.ModelAdmin):
    pass


@admin.register(RiskFactor)
class RiskFactorAdmin(admin.ModelAdmin):
    pass

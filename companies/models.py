import datetime
from django.db import models
from core.models import CoreModel
from django.core.validators import MaxValueValidator, MinValueValidator


YEAR_CHOICES = []
for r in range(1995, (datetime.datetime.now().year + 1)):
    YEAR_CHOICES.append((r, r))


class Company(CoreModel):
    def __str__(self):
        return self.company_list.name

    # class Meta:
    #     verbose_name = "회사"

    year = models.IntegerField(
        ("year"),
        max_length=4,
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year,
    )

    company_list = models.ForeignKey(
        "CompanyList", related_name="company_list", on_delete=models.SET_NULL, null=True
    )

    risk_factor = models.ManyToManyField(
        "RiskFactor", related_name="risk_factor", blank=True
    )


class Section(CoreModel):
    class Meta:
        verbose_name = "구역 "

    notice = models.ForeignKey(
        Company, related_name="sections", on_delete=models.CASCADE
    )
    name = models.CharField(
        "구역이름",
        max_length=140,
        null=True,
    )

    latitude = models.FloatField(
        "위도", null=True, validators=[MinValueValidator(0), MaxValueValidator(300)]
    )
    longitude = models.FloatField(
        "경도", null=True, validators=[MinValueValidator(0), MaxValueValidator(300)]
    )
    temperature = models.FloatField(
        "온도", null=True, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return self.name


class AbstractItem(CoreModel):
    """Abstract Item"""

    # 어플리케이션에서 공통되게 자신의 이름(name)을 반환해준다.
    name = models.CharField(max_length=80)

    class mata:
        abstract = True

    def __str__(self):
        return self.name


class CompanyList(AbstractItem):
    """CompanyList Model Definition"""

    class Meta:
        verbose_name_plural = "CompanyList"


class RiskFactor(AbstractItem):
    """RiskFactor Model Definition"""

    class Meta:
        verbose_name_plural = "RiskFactor"

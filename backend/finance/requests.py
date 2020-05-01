from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Expense
from .serializers import CategoryByMonthSerializers


@api_view(['GET'])
def month_categories(request, year, month):
    super_categories = Category.objects.all()
    expenses = Expense.objects.filter(date__month=month, date__year=year)
    to_return = CategoryByMonthSerializers(super_categories, many=True, context={'expenses': expenses})

    return Response(to_return.data)

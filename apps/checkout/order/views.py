"""Views for orders API"""
import os, django
from rest_framework.decorators import api_view
from producer import confirm_order
from rest_framework.response import Response
from json import dumps

@api_view(['POST'])
def confirm(request):
    """Returns successful confirm."""

    order = {
        "id": "2",
        "code": "5555",
        "user_id": "1",
        "ambassador_email": "ambassador@test.com",
        "first_name": "Fin",
        "last_name": "Exampler",
        "email": "test@email.com",
        "country": "PL",
        "city": "Wwa",
        "zip": "01-002",
        "admin_revenue": 300,
        "ambassador_revenue": 200,
    }
    confirm_order(data=dumps(order))

    return Response({"message": "success"})
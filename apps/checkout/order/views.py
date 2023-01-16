"""Views for orders API"""

from rest_framework.decorators import api_view
from producer import confirm_order
from rest_framework.response import Response

@api_view(['POST'])
def confirm(request):
    """Returns successful confirm."""
    data = {'number' : 100}
    confirm_order(data=data)

    return Response({'number': data["number"]})
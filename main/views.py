from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Event, Organization
from .serializers import EventSerializer, OrganizationSerializer


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by('end')
    serializer_class = EventSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class OrgList(generics.ListCreateAPIView):
    queryset = Organization.objects.all().order_by('name')
    serializer_class = OrganizationSerializer


@api_view(['POST'])
def save_events(request):
    """Handle saving events"""
    for event in request.data['events']:
        Event.objects.create(
            id=event['id'],
            name=event['name'],
            start=event['start'],
            end=event['end']
        )

    return Response({'success': True})

# @api_view(['POST'])
# def save_org(request):
#     """Handle saving events"""
#     Event.objects.create(
#         id=request.data['id'],
#         name=request.data['name'],
#         start=request.data['start'],
#         end=request.data['end']
#     )

#     return Response({'success': True})


from rest_framework import viewsets
from .models import Listing
from .serializers import ListingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all().order_by("-created_at")
    serializer_class = ListingSerializer


from rest_framework import generics, permissions, authentication

from api.permissions import IsStaffEditorPermission
from .models import Product
from .serializers import ProductSerializer
from api.authentication import TokenAuthentication

class AdminProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer):
        super().perform_create(serializer)

admin_product_list_create_view=AdminProductListCreateAPIView.as_view()

class AdminProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

admin_product_retrieve_update_destroy=AdminProductListCreateAPIView.as_view()


class ListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

product_list_view = ListAPIView.as_view()
    


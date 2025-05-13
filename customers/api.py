from .models import Customer, DocumentType, Product, Purchase
from rest_framework import viewsets, permissions
from .serializers import CustomerSerializer, DocumentTypeSerializer, ProductSerializer, PurchaseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def customer_by_document(request):
    doc_type = request.GET.get('document_type')
    doc_number = request.GET.get('identification_number')
    if not doc_type or not doc_number:
        return Response({'error': 'document_type and identification_number are required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        customer = Customer.objects.get(document_type=doc_type, identification_number=doc_number)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
    customer_data = CustomerSerializer(customer).data
    purchases = Purchase.objects.filter(customer=customer)
    purchases_data = PurchaseSerializer(purchases, many=True).data
    total_purchases = sum([float(p['total']) for p in purchases_data])
    response = customer_data
    response['purchases'] = purchases_data
    response['total_purchases'] = total_purchases
    return Response(response)

class DocumentTypeViewSet(viewsets.ModelViewSet):
    queryset = DocumentType.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DocumentTypeSerializer
    
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerSerializer
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer
    
class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PurchaseSerializer
from rest_framework import routers
from django.urls import path
from .api import CustomerViewSet, DocumentTypeViewSet, ProductViewSet, PurchaseViewSet, customer_by_document
from .views import customer_lookup_view

router = routers.DefaultRouter()
router.register('api/document_type', DocumentTypeViewSet, 'document_type')
router.register('api/customer', CustomerViewSet, 'customer')
router.register('api/product', ProductViewSet, 'product')
router.register('api/purchase', PurchaseViewSet, 'purchase')

urlpatterns = router.urls + [
    path('api/customer_by_document/', customer_by_document, name='customer_by_document'),
    path('customer_lookup/', customer_lookup_view, name='customer_lookup'),
]
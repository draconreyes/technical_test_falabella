from  rest_framework import serializers
from .models import Customer, DocumentType, Product, Purchase, PurchaseProduct

class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = (
            'id',
            'name',
            'description'
        )
        read_only_fields = ('id',)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'country',
            'city',
            'address',
            'identification_number',
            'document_type',
            'created_at'
        )
        read_only_fields = ('id','created_at')
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price'
        )
        read_only_fields = ('id',)
        
class PurchaseProductSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField()

    class Meta:
        model = PurchaseProduct
        fields = ('product', 'quantity')

class PurchaseSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    products = PurchaseProductSerializer(many=True, write_only=True)
    purchase_date = serializers.DateTimeField(read_only=True)
    total = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = Purchase
        fields = (
            'id',
            'customer',
            'products',
            'purchase_date',
            'total',
        )
        read_only_fields = ('id','purchase_date','total')

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        purchase = Purchase.objects.create(**validated_data)
        total = 0
        for prod in products_data:
            product = prod['product']
            quantity = prod['quantity']
            PurchaseProduct.objects.create(purchase=purchase, product=product, quantity=quantity)
            total += product.price * quantity
        purchase.total = total
        purchase.save()
        return purchase


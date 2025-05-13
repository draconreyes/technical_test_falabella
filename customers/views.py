import requests
from django.shortcuts import render

def customer_lookup_view(request):
    context = {}
    # Obtener todos los tipos de documento desde la API
    try:
        doc_types_response = requests.get('http://localhost:8000/api/document_type/')
        if doc_types_response.status_code == 200:
            context['document_types'] = doc_types_response.json()
        else:
            context['document_types'] = []
    except Exception as e:
        context['document_types'] = []
        context['error'] = f"Error fetching document types: {e}"
    if request.method == 'POST':
        doc_type = request.POST.get('document_type')
        doc_number = request.POST.get('identification_number')
        if doc_type and doc_number:
            try:
                api_url = f'http://localhost:8000/api/customer_by_document/?document_type={doc_type}&identification_number={doc_number}'
                api_response = requests.get(api_url)
                if api_response.status_code == 200:
                    data = api_response.json()
                    context['customer'] = data
                    context['purchases'] = data.get('purchases', [])
                    context['total_purchases'] = data.get('total_purchases', 0)
                    # Construir texto para exportar
                    export_text = 'Customer Info\n'
                    export_text += f"Name: {data.get('first_name', '')} {data.get('last_name', '')}\n"
                    export_text += f"Email: {data.get('email', '')}\n"
                    export_text += f"Phone: {data.get('phone_number', '')}\n"
                    export_text += f"Country: {data.get('country', '')}\n"
                    export_text += f"City: {data.get('city', '')}\n"
                    export_text += f"Address: {data.get('address', '')}\n"
                    export_text += f"Document Type: {data.get('document_type', '')}\n"
                    export_text += f"Identification Number: {data.get('identification_number', '')}\n"
                    export_text += f"\nTotal Purchases: {data.get('total_purchases', 0)}\n"
                    export_text += '\nPurchases:\n'
                    if data.get('purchases'):
                        for purchase in data['purchases']:
                            export_text += f"Date: {purchase.get('purchase_date', '')} | Total: {purchase.get('total', '')}\n"
                    else:
                        export_text += 'No purchases found.\n'
                    context['export_text'] = export_text
                else:
                    error_msg = api_response.json().get('error', 'Customer not found.')
                    context['error'] = error_msg
            except Exception as e:
                context['error'] = str(e)
        else:
            context['error'] = 'Both fields are required.'
    return render(request, 'customers/customer_lookup.html', context)

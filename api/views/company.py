from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from ..models.company import Company
import json

# Create your views here.
class CompanyView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if(id > 0):
            companies = list(Company.objects.filter(id=id).values())
            if len(companies)>0:
                company = companies[0];
                datos={
                    'isValid':True,
                    'message':'Company',
                    'data':company
                }
            else:
                datos= {
                    'isValid':False,
                    'message':'Company not found'
                }
            return JsonResponse(datos)
        else:
            companies = list(Company.objects.values())
            if len(companies)>0:
                datos={
                    'isValid':True,
                    'message':'List companies',
                    'data':companies
                }
            else:
                datos= {
                    'isValid':False,
                    'message':'List companies not found'
                }
            return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        Company.objects.create(
            name=jd['name'],
            website=jd['website'],
            foundation=jd['foundation']
        )
        datos = {'isValid':True, 'message':'Company add success'}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            company = Company.objects.get(id=id)
            company.name = jd['name'];
            company.website = jd['website']
            company.foundation = jd['foundation']
            
            company.save();
            
            datos = {'isValid':True, 'message':'Company update success'}
        else:
            datos = {'isValid':False, 'message':'Company not found'}
        return JsonResponse(datos)
    
    def delete(self, request):
        pass
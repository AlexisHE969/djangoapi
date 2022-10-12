from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from ..models.people import People
import json

class PeopleView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if(id > 0):
            result = list(People.objects.filter(id=id).values())
            if len(result)>0:
                people = result[0];
                datos={
                    'isValid':True,
                    'message':'People',
                    'data':people
                }
            else:
                datos= {
                    'isValid':False,
                    'message':'People not found'
                }
            return JsonResponse(datos)
        else:
            people = list(People.objects.values())
            if len(people)>0:
                datos={
                    'isValid':True,
                    'message':'List people',
                    'data':people
                }
            else:
                datos= {
                    'isValid':False,
                    'message':'List people not found'
                }
            return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        People.objects.create(
            email=jd['email'],
            age=jd['age'],
            gender=jd['gender']
        )
        datos = {'isValid':True, 'message':'Company add success'}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        people = list(People.objects.filter(id=id).values())
        if len(people) > 0:
            people = People.objects.get(id=id)
            people.email = jd['email'];
            people.age = jd['age']
            people.gender = jd['gender']
            
            people.save();
            
            datos = {'isValid':True, 'message':'Company update success'}
        else:
            datos = {'isValid':False, 'message':'Company not found'}
        return JsonResponse(datos)
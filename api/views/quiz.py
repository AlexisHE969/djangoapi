from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from ..models.quiz import Quiz
import json

class QuizView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if(id > 0):
            result = list(Quiz.objects.filter(id=id).values())
            if len(result)>0:
                quiz = result[0];
                datos={
                    'isValid':True,
                    'message':'Quiz',
                    'data':quiz
                }
            else:
                datos= {
                    'isValid':False,
                    'message':'People not found'
                }
            return JsonResponse(datos)
        else:
            quiz = list(Quiz.objects.values())
            if len(quiz)>0:
                datos={
                    'isValid':True,
                    'message':'List Quiz',
                    'data':quiz
                }
            else:
                datos= {
                    'isValid':False,
                    'message':'List people not found'
                }
            return JsonResponse(datos)
    
    def post(self, request):
        jd = json.loads(request.body)
        Quiz.objects.create(
            people = jd['people'],
            fovorite_social_network = jd['fovorite_social_network'],
            time_facebook = jd['time_facebook'],
            time_whatsapp = jd['time_whatsapp'],
            time_twitter = jd['time_twitter'],
            time_instagram = jd['time_instagram'],
            time_tiktok = jd['time_tiktok'],
        )
        datos = {'isValid':True, 'message':'Company add success'}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        quiz = list(Quiz.objects.filter(id=id).values())
        if len(quiz) > 0:
            quiz = Quiz.objects.get(id=id)
            quiz.people = jd['people'],
            quiz.fovorite_social_network = jd['fovorite_social_network'],
            quiz.time_facebook = jd['time_facebook'],
            quiz.time_whatsapp = jd['time_whatsapp'],
            quiz.time_twitter = jd['time_twitter'],
            quiz.time_instagram = jd['time_instagram'],
            quiz.time_tiktok = jd['time_tiktok'],
            
            quiz.save();
            
            datos = {'isValid':True, 'message':'Company update success'}
        else:
            datos = {'isValid':False, 'message':'Company not found'}
        return JsonResponse(datos)
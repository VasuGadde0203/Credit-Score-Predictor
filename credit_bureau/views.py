# views.py

from django.shortcuts import render, redirect
from .models import Question, UserResponse
# from .utils import calculate_credit_score
from django.http import JsonResponse
from django.shortcuts import render
from django.core.serializers import serialize


def question_form(request):
    questions = Question.objects.all()
    
    questions_json = serialize('json', questions, fields=('question_text', 'option_a', 'option_b', 'option_c', 'option_d'))
    
    return render(request, 'credit_bureau/question_form.html', {'questions_json': questions_json})


def submit_responses(request):
    if request.method == 'POST':
        total_score = 0
        
        for question in Question.objects.all():
            answer = request.POST.get(f'question_{question.id}')

            if answer:
                if answer == 'A':
                    total_score += 10
                elif answer == 'B':
                    total_score += 7
                elif answer == 'C':
                    total_score += 5
                elif answer == 'D':
                    total_score += 3

                # Save the response
                UserResponse.objects.create(
                    question=question,
                    answer=answer
                )

        print(f"Total Score: {total_score}")  # Debugging line
        return redirect('results', score=total_score)
    else:
        return redirect('question_form')




def results(request, score):
    return render(request, 'credit_bureau/results.html', {'score': score})

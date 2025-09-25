from django.shortcuts import render, redirect
from .models import Question
import telebot
admin_id = 'ADMIN'


bot = telebot.TeleBot('TOKEN')
# Create your views here.
def home_page(request):
    if request.method == 'POST':
        st_name = request.POST.get('st_name')
        group_num = request.POST.get('group_num')
        return redirect(f'/test-time/{st_name}-{group_num}')
    return render(request, 'home.html')


def test_time(request, pk):
    questions = Question.objects.all()
    student = pk.split('-')
    name = f'{student[0]} {student[1]}-й поток'
    context = {'questions': questions, 'student': name}

    if request.method == "POST":
        questions = Question.objects.all()
        answers = {}
        text = f'Результаты студента {name}\n\n'
        for question in questions:
            code_key = f'code_{question.id}'
            text_key = f'answer_{question.id}'

            answer = request.POST.get(code_key, '').strip()

            if not answer:
                answer = request.POST.get(text_key, '').strip()

            if answer:
                answers[question.id] = answer
        for q, a in answers.items():
            text += f'Вопрос {q}.\nОтвет:\n<code>{a}</code>\n\n'
        print(text)
        bot.send_message(admin_id, text, parse_mode='HTML')
        return redirect('/end')
    return render(request, "main.html", context)


def end_page(request):
    return render(request, 'end.html')

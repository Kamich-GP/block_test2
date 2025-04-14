from django.shortcuts import render, redirect
from .models import Question
import telebot
admin_id = 791555605


bot = telebot.TeleBot('7666731778:AAGEPjPNYZi52DPCLT1krb6XSSrcW7m128Y')
# Create your views here.
def main_page(request):
    all_questions = Question.objects.all()
    text = ''
    if request.method == 'POST':
        name = request.POST.get('st_name')
        group = request.POST.get('st_group')
        questions = Question.objects.all()
        answers = {}
        text = f'Результаты студента {name} поток {group}\n\n'
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
        bot.send_message(admin_id, text, parse_mode='HTML')
        return redirect('/end')

    return render(request, 'main.html', {'questions': all_questions})


def end_page(request):
    return render(request, 'end.html')

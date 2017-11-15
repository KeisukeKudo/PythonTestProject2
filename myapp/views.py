from django.shortcuts import render, redirect
from .models import MessageBord


def MyAppIndex(request):
    msg = request.GET.get('words')

    delete_text = request.POST.getlist('delete_text')
    if delete_text:
        MessageBord.objects.filter(id__in=delete_text).delete()

    data_list = MessageBord.objects.order_by('-id')
    contexts = {
        'result_list': data_list
    }

    if msg is not None:
        message_data = MessageBord()
        message_data.new_message = msg
        message_data.save()

    return render(request, 'myapp/index.html', contexts)
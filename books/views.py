import datetime
from django.http import HttpResponse 


def writers_view(request):
    writers_list = [
        "Лев Толстой",
        "Фёдор Достоевский",
        "Чингиз Айтматов", 
        "Алыкул Осмонов",
        "Гоголь",
        "Булгаков",
        "Маяковский",
        "Лермонтов",
        "Есенин",
        "Касым Тыныстанов"
    ]

    html_output = "<h1>10 Великих писателей</h1>" + "<br>".join(writers_list)
    return HttpResponse(html_output)


def quotes_view(request):
    quotes_list = [
        "1. Жить – хорошо, а хорошо жить – еще лучше.", 
        "2. В человеке должно быть всё прекрасно. (Чехов)",
        "3. Чтение – лучшее учение.",
        "4. Душа обязана трудиться. (Платонов)",
        "5. Если любишь – значит живешь.",
    ]
    html_output = "<h1>5 Цитат</h1>" + "<br>".join(quotes_list)
    return HttpResponse(html_output)

def time_view(request): 
    now = datetime.datetime.now()
    formatted_time = now.strftime('%Y-%m-%d %H:%M:%S') 
    return HttpResponse(f"<h1>Системное время</h1>Текущее системное время: {formatted_time}")
from django.shortcuts import render, get_object_or_404
from .models import WriterQuotes

def writer_list(request):
    writers = WriterQuotes.objects.all()
    return render(request, "books/writer_list.html", {"writers": writers})

def writer_detail(request, pk):
    writer = get_object_or_404(WriterQuotes, pk=pk)
    return render(request, "books/writer_detail.html", {"writer": writer})

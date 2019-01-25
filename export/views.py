from django.shortcuts import render


def index(request):
    page_name = "エクスポートページ"
    context = {'page_name': page_name}
    return render(request, 'export/index.html', context)

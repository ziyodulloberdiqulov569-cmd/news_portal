from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import News, Comment
from django.core.paginator import Paginator
from .models import News, Category

def home(request):
    query = request.GET.get('q')

    if query:
        news_queryset = News.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(category__name__icontains=query)
        ).order_by('-created_at')
    else:
        news_queryset = News.objects.all().order_by('-created_at')

    paginator = Paginator(news_queryset, 5)  # har sahifada 5 ta yangilik

    page_number = request.GET.get('page')
    news_list = paginator.get_page(page_number)

    popular_news = News.objects.order_by('-views_count')[:5]
    categories = Category.objects.all()

    return render(request, 'news/home.html', {
        'news_list': news_list,
        'popular_news': popular_news,
        'categories': categories,
    })


def news_detail(request, id):
    news = get_object_or_404(News, id=id)

    news.views_count += 1
    news.save()

    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')

        if name and text:
            Comment.objects.create(
                news=news,
                name=name,
                text=text

            related_news = News.objects.filter(
                category=news.category
            ).exclude(
                id=news.id
            ).order_by('-created_at')[:4]
            )

    comments = news.comments.all().order_by('-created_at')
        
        return render(request, 'news/detail.html', {
            'news': news,
            'comments': comments,
            'related_news': related_news,
        })

def category_news(request, category_id):
    news_list = News.objects.filter(
        category_id=category_id
    )

    return render(request, 'news/home.html', {
        'news_list': news_list
    })

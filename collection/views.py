from functools import reduce
import re

from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from collection.models import Item


class IndexText:
    title = 'Моя коллекция'
    headline = 'Моя коллекция'
    time = 'Врема добавления'
    name = 'Название'
    keys = 'Ключевые слова'
    comments = 'Комментарии'
    photo = 'Фото'
    search = 'ПОИСК: '
    go = 'ИСКАТЬ'
    no_item = 'Коллекция пуста'


class DetailsText:
    time = 'Врема добавления:'
    keys = 'Ключевые слова:'
    comments = 'Комментарии:'


def split_search(search_str):
    if search_str != '':
        search_list = re.split(r'\s|,|;', search_str)
        search_list = list(filter(''.__ne__, search_list))
    else:
        search_list = ['']
    return search_list


def index(request):
    search_text = ''
    if request.POST:
        search_text = request.POST['search']
        search_list = split_search(search_text)
    else:
        search_list = ['']
    query_list_1 = [Q(name__icontains=word) for word in search_list]
    query_list_2 = [Q(key_words__icontains=word) for word in search_list]
    query_list_3 = [Q(info__icontains=word) for word in search_list]
    query = reduce(lambda x, y: x | y, query_list_1 + query_list_2 + query_list_3)
    col = Item.objects.filter(query).order_by('-post_date')
    context = {'col': col, 'search_text': search_text, 'mytext': IndexText}
    return render(request, 'collection/index.html', context)


def details(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {'item': item, 'mytext': DetailsText}
    return render(request, 'collection/details.html', context)

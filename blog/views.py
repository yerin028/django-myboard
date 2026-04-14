from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView    

from blog.models import Post

# Create your views here.

class PostLV(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 2

class PostDV(DetailView):
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'mod_date'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'mod_date'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'mod_date' 
    month_format = '%m'

class PostDAV(DayArchiveView):  
    model = Post
    date_field = 'mod_date' 
    month_format = '%m'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'mod_date'
# from django.shortcuts import render
# from django.views.generic import ListView, DetailView
# from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView    

# from blog.models import Post

# # Create your views here.

# class PostLV(ListView):
#     model = Post
#     context_object_name = 'posts'
#     paginate_by = 2

# class PostDV(DetailView):
#     model = Post

# class PostAV(ArchiveIndexView):
#     model = Post
#     date_field = 'mod_date'

# class PostYAV(YearArchiveView):
#     model = Post
#     date_field = 'mod_date'
#     make_object_list = True

# class PostMAV(MonthArchiveView):
#     model = Post
#     date_field = 'mod_date' 
#     month_format = '%m'

# class PostDAV(DayArchiveView):  
#     model = Post
#     date_field = 'mod_date' 
#     month_format = '%m'

# class PostTAV(TodayArchiveView):
#     model = Post
#     date_field = 'mod_date'

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.dates import (
    ArchiveIndexView,
    YearArchiveView,
    MonthArchiveView,
    DayArchiveView,
    TodayArchiveView
)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from blog.models import Post
from blog.ai import ask_ai

# 게시판 기본 cbv
class PostLV(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 2

class PostDV(DetailView):
    model = Post

# 아카이브 기능
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

# ai 챗봇 api
@csrf_exempt
def post_ai_chat(requests, pk):
    if requests.method == "POST":
        question = requests.POST.get("question")

        post = get_object_or_404(Post, pk=pk)

        prompt = f"""
게시글 내용:
{post.content}

사용자 질문:
{question}

이 게시글 내용을 기반으로 정확하고 간결하게 답변해줘.
"""
        
        try:
            answer = ask_ai(prompt)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        
        return JsonResponse({
            "answer":answer
        })
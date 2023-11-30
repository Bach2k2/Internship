from django.http import HttpResponse
from .models import Novel
from django.shortcuts import get_object_or_404, render
from django.template import loader


def index(request):
    novel_list = Novel.objects.order_by("-published_date").all()
    # output = novel
    # return HttpResponse(novel_list);
   
    context = {'novel_list': novel_list}
    return render(request,'novels/index.html' ,context)

    # Way 2: 
    # template = loader.get_template("novels/index.html")
    # return HttpResponse(template.render(context, request))

def detail(request, novel_id):
    novel = get_object_or_404(Novel, pk=novel_id)
    # return HttpResponse("You're looking at novel %s." % novel_id)
    return render(request, "novels/detail.html", {"novel": novel})


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
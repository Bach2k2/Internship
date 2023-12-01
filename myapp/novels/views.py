from django.http import HttpResponse
from .models import Novel
from django.shortcuts import get_object_or_404, render,redirect
from django.template import loader
from .forms import NovelForm


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

def create_novel(request):
    # print("hehe")
    if request.method == 'POST':
        form = NovelForm(request.POST)
        if form.is_valid(): 
            # Novel.objects.create(form); 
            title = form.cleaned_data['title']
            published_date = form.cleaned_data['published_date']
            year = form.cleaned_data['year']
            status = form.cleaned_data['status']
            category = form.cleaned_data['category']
            print(category)

            # Create a Novel object
            novel = Novel.objects.create(
                title=title,
                published_date=published_date,
                year=year,
                status=status,
                category=category
            )
            # Novel.objects.add(novel)
            novel.save();
            return redirect("/novels/")
    else:
        print("not valid")
        form = NovelForm()

    return render(request, 'novels/create_novel.html', {'form': form})


# def addNovel(request):
#     return HttpResponse("You're voting on question %s." % question_id)
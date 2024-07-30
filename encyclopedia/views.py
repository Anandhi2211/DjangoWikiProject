import random
import markdown2
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entrypage(request,title):

    content = util.get_entry(title)
    htmlcontent = markdown2.markdown(content) 
    if content is not None:
        return render(request, "encyclopedia/entrypage.html", {
            "title": title,
            "entrypage": htmlcontent
        })
    else:
        return render(request, "encyclopedia/notfound.html", {
            "title": title
        })

def search(request):
    title = request.GET.get('q')
    content = util.get_entry(title) 
    htmlcontent = markdown2.markdown(content)

    names = { name.lower() for name in util.list_entries()}
    if content is not None and title.lower() in names :
        return render(request,"encyclopedia/entrypage.html", {
            "title":title,
            "entrypage":htmlcontent
        }) 
    else:
        matchingnames = []
        for name in names:
            if title in name.lower():
                matchingnames.append(name)
        return render (request , "encyclopedia/index.html", {
            "entries": matchingnames
        })
  

def newpage(request):
            return render(request, "encyclopedia/newpage.html")
       

        
def save(request):
        if request.method == "POST":
            title = request.POST.get('title')
            content = request.POST.get('content')
            htmlcontent = markdown2.markdown(content)
            for name in util.list_entries():
                    if name.lower() == title.lower():
                           return render(request,"encyclopedia/filealreadyexist.html",{
                                            "title": title
                           })
        util.save_entry(title,content)
        return render(request, "encyclopedia/entrypage.html",{
            "title":title,
            "entrypage":htmlcontent})

def editpage(request,title):
     
     content = util.get_entry(title)
     return render(request,"encyclopedia/editpage.html",{
          "title":title,
          "content":content
     })

def editsave(request):
     if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content') 
        util.save_entry(title,content)
        newcontent = util.get_entry(title) 
        htmlcontent = markdown2.markdown(newcontent)
        if newcontent is not None:
                return render(request, "encyclopedia/entrypage.html", {
                    "title": title,
                    "entrypage": htmlcontent
                    })
        else:
                return render(request, "encyclopedia/notfound.html", {
            "title": title
        })    


def randompage(request):
    list = util.list_entries()
    if list:
            title = random.choice(list)
            content = util.get_entry(title)
            htmlcontent = markdown2.markdown(content)
            return render(request,"encyclopedia/entrypage.html",{
                "title":title,
                "entrypage":htmlcontent
                })
    else:
            return render(request, "encyclopedia/notfound.html", {
            "title": title
        })  
          


     

          

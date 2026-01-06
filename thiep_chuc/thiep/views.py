from django.shortcuts import render, redirect, get_object_or_404
from .models import Info
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, "index.html")

def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        loi_chuc = request.POST.get("loi_chuc")
        loai_thiep = request.POST.get("loai_thiep")
        Info.objects.create(
            date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            person_name = name,
            cau_chuc = loi_chuc,
            loai_thiep = loai_thiep,
        )
        return redirect("thiep:create")
    infos = Info.objects.all().order_by('-id')
    return render(request, "create.html", {'infos': infos})

def delete_id(request, id):
    info = get_object_or_404(Info, id=id)
    info.delete()
    return redirect("thiep:create")

def edit(request, id):
    info = get_object_or_404(Info, id=id)
    if request.method == "POST":
        info.person_name = request.POST.get("name")
        info.cau_chuc = request.POST.get("cau_chuc")
        info.loai_thiep = request.POST.get("loai_thiep")
        info.save()
        return redirect("thiep:create")
    return render(request, "edit.html", {"info": info})

def thiep(request, id):
    info = get_object_or_404(Info, id=id)
    return render(request, "themes.html", {"info": info})
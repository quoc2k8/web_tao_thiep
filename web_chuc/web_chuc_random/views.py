# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Log
from datetime import datetime

def chuc(request):
    if request.method == "POST":
        ten = request.POST.get("ten")
        loi_chuc = request.POST.get("loichuc")
        loai = request.POST.get("loai")

        Log.objects.create(
            date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            who = ten,
            loi_chuc = loi_chuc,
            loai = loai
        )

    return render(request, "chuc.html")


def log_chuc(request):
    # XÓA
    if request.method == "POST":
        log_id = request.POST.get("log_id")
        log = get_object_or_404(Log, id=log_id)
        log.delete()
        return redirect("web_chuc_random:show_logs")

    # HIỂN THỊ
    logs = Log.objects.all().order_by('-id')
    return render(request, "show_logs.html", {"logs": logs})


def log_detail(request, id):
    log = get_object_or_404(Log, id=id)
    return render(request, "thu.html", {"log": log})


def log_edit(request, id):
    log = get_object_or_404(Log, id=id)
    if request.method == "POST":
        log.who = request.POST.get("ten")
        log.loi_chuc = request.POST.get("loichuc")
        log.loai = request.POST.get("loai")
        log.save()
        return redirect("web_chuc_random:show_logs")
    return render(request, "edit_log.html", {"log": log})
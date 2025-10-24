from django.shortcuts import render, redirect
from app import models
from app.utils.bootstrap import BootStrapModelForm
from app.utils.pagination import Pagination


class ImageUploadForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.ImageUpload
        fields = "__all__"


def image_list(request):
    """ 图片列表 """
    queryset = models.ImageUpload.objects.all().order_by('-create_time')
    
    # 分页
    page_object = Pagination(request, queryset, page_size=10)
    
    return render(request, 'image_list.html', {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    })


def image_add(request):
    """ 上传图片 """
    title = "上传图片"
    if request.method == "GET":
        form = ImageUploadForm()
        return render(request, 'image_add.html', {"form": form, "title": title})

    form = ImageUploadForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/image/list/')
    return render(request, 'image_add.html', {"form": form, "title": title})


def image_delete(request):
    """ 删除图片 """
    nid = request.GET.get('nid')
    models.ImageUpload.objects.filter(id=nid).delete()
    return redirect('/image/list/')


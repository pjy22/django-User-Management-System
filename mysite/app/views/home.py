from django.shortcuts import render, redirect


def home(request):
    """ 首页 - 重定向到部门列表 """
    return redirect('/admin/list/')

# -*- coding: utf-8 -*-
from django.shortcuts import render
from zolServer.detail import detail
from zolServer.scrapy import scrapy
from django.http import HttpResponse
import sys
import threading
import time
reload(sys)
from zolServer import models
sys.setdefaultencoding('utf8')

def show(request):
    '''绑定主页/index的方法
    :param request:
    :return:
    '''

    Mydetail = detail()
    #从数据库获取当前数据日期
    try:
        date = models.scrapy_date.objects.get(id="zuixinjilu")
        date = date.date
    except Exception:
        date = "暂时没有数据"
    option = request.GET.get('option', "NULL")
    order = request.GET.get('order', "NULL")
    print option
    print order
    if option=='cpu':
        if order == 'name':
         return render(request, 'home.html', {'main': Mydetail.getcpu_main(),'time':date})
        if order == 'sales':
         return render(request, 'home.html', {'main': Mydetail.getcpu_main().order_by('sales'),'time':date})
        if order == 'price_up':
         return render(request, 'home.html', {'main': Mydetail.getcpu_main().order_by('price'),'time':date})
        if order == 'price_down':
            return render(request, 'home.html', {'main': Mydetail.getcpu_main().order_by('-price'),'time':date})
    if option=='board':
        if order == 'name':
            return render(request, 'home.html', {'main': Mydetail.getboard_main(),'time':date})
        if order == 'sales':
            return render(request, 'home.html', {'main': Mydetail.getboard_main().order_by('sales'),'time':date})
        if order == 'price_up':
            return render(request, 'home.html', {'main': Mydetail.getboard_main().order_by('price'),'time':date})
        if order == 'price_down':
            return render(request, 'home.html', {'main': Mydetail.getboard_main().order_by('-price'),'time':date})
        return render(request, 'home.html', {'main': Mydetail.getboard_main(),'time':date})

    if option=='memory':
        if order == 'name':
         return render(request, 'home.html', {'main': Mydetail.getmem_main(),'time':date})
        if order == 'sales':
         return render(request, 'home.html', {'main': Mydetail.getmem_main().order_by('sales'),'time':date})
        if order == 'price_up':
         return render(request, 'home.html', {'main': Mydetail.getmem_main().order_by('price'),'time':date})
        if order == 'price_down':
            return render(request, 'home.html', {'main': Mydetail.getmem_main().order_by('-price'),'time':date})
        return render(request, 'home.html', {'main': Mydetail.getmem_main()})

    if option=='power':
        if order == 'name':
         return render(request, 'home.html', {'main': Mydetail.getpower_main(),'time':date})
        if order == 'sales':
         return render(request, 'home.html', {'main': Mydetail.getpower_main().order_by('sales'),'time':date})
        if order == 'price_up':
         return render(request, 'home.html', {'main': Mydetail.getpower_main().order_by('price'),'time':date})
        if order == 'price_down':
            return render(request, 'home.html', {'main': Mydetail.getpower_main().order_by('-price'),'time':date})
        return render(request, 'home.html', {'main': Mydetail.getpower_main()})

    if option=='radiator':
        if order == 'name':
         return render(request, 'home.html', {'main': Mydetail.getradiator_main(),'time':date})
        if order == 'sales':
         return render(request, 'home.html', {'main': Mydetail.getradiator_main().order_by('sales'),'time':date})
        if order == 'price_up':
         return render(request, 'home.html', {'main': Mydetail.getradiator_main().order_by('price'),'time':date})
        if order == 'price_down':
            return render(request, 'home.html', {'main': Mydetail.getradiator_main().order_by('-price'),'time':date})
        return render(request, 'home.html', {'main': Mydetail.getpower_main()})

    if option=='graphic':
        if order == 'name':
            return render(request, 'home.html', {'main': Mydetail.getgraphic_main(),'time':date})
        if order == 'sales':
            return render(request, 'home.html', {'main': Mydetail.getgraphic_main().order_by('sales'),'time':date})
        if order == 'price_up':
            return render(request, 'home.html', {'main': Mydetail.getgraphic_main().order_by('price'),'time':date})
        if order == 'price_down':
            return render(request, 'home.html', {'main': Mydetail.getgraphic_main().order_by('-price')})
        return render(request, 'home.html', {'main': Mydetail.getgraphic_main(),'time':date})
    return render(request, 'home.html',{'time':date})
def crawl(request):
    '''
    绑定抓取界面/scrapy的方法
    :param request:
    :return:
    '''
    date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    #threads=[] 
    #threads.append(threading.Thread(target=scrapy.scrapy(),args=(u"jason",)))
    #threads[0].start()
    try:
        models.scrapy_date.objects.get(id="zuixinjilu")
    except:
        obj = models.scrapy_date(date=date,id="zuixinjilu")
        obj.save()

    #更新scapy.scrapy_date第一行记录
    obj = models.scrapy_date.objects.get(id='zuixinjilu')
    obj.date = date
    obj.save()
    return render(request, 'testl.html')
def parameter(request):
    '''
    绑定参数界面/parameter的方法
    :param request:
    :return:
    '''
    Mydetail = detail()
    id  = request.GET.get('id', "NULL")
    attr = request.GET.get('attr',"NULL")
    if attr=='cpu':
        main = models.cpu_list_test.objects.get(id=id)
        para = Mydetail.getcpu_detail(id)
    if attr=='board':
        main = models.board_list_test.objects.get(id=id)
        para = Mydetail.getboard_detail(id)
    if attr=='mem':
        main = models.mem_list_test.objects.get(id=id)
        para = Mydetail.getmem_detail(id)
    if attr=='graphic':
        main = models.graphic_list_test.objects.get(id=id)
        para = Mydetail.getgraphic_detail(id)
    if attr=='power':
        main = models.power_list_test.objects.get(id=id)
        para = Mydetail.getpower_detail(id)
    if attr=='radiator':
        main = models.radiator_list_test.objects.get(id=id)
        para = Mydetail.getradiator_detail(id)
    return render(request, 'parameter.html',{'main':main,'para':para})
def info(request):
    id = request.GET.get('info', "0")
    from zolServer import models
    info = models.cpu_list_test.objects.get(id=id)
    return render(request, 'newsdemo.html', {'info': info})
def demo(request):
    return HttpResponse("Hello Word")
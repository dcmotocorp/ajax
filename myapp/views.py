from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *
from .forms import ProductForm,CustomerForm
from django.http import JsonResponse

# Create your views here.
def home(request):
    o_data=Order.objects.all()
    context={
        "data":o_data,
    }
    return render(request,"myapp/orderlisting.html",{"context":context})

def customer(request):
    context ={} 
    context['form']= CustomerForm() 
    return render(request,"myapp/customer.html",context)

def add_customer(request):
    fname=request.POST['first_name']
    lname=request.POST['last_name']
    contact_no=request.POST['contact_no']
    pincode=request.POST['pincode']

    cid=Customer.objects.create(first_name=fname,last_name=lname,contact_no=contact_no,pincode=pincode)


    c_all = Customer.objects.all()
    p_all = Product.objects.all()
    context = {
        'c_all': c_all,
        'p_all': p_all,
    }

    return render(request,"myapp/orderform.html",{'context':context})

def product(request):
    context ={} 
    context['form']= ProductForm() 
    return render(request, "myapp/product.html", context)

def add_product(request):
    name=request.POST['name']
    unit_price=request.POST['unit_price']

    pid=Product.objects.create(name=name,unit_price=unit_price)


    c_all = Customer.objects.all()
    p_all = Product.objects.all()
    context = {
        'c_all': c_all,
        'p_all': p_all,
    }

    return render(request, "myapp/orderform.html",{'context':context})

def get_price(request):
    print("----> selected value ",request.POST['selected'])
    product_id=request.POST['selected']
    print("------------->selected value ",product_id)
    pid=Product.objects.get(id=product_id)
    res=pid.unit_price
    data=res
    context={
        'data':data,
    }
    print("------------------------>context :",data)
    return JsonResponse({'context':context})

def get_total(request):
    qty=request.POST['selected']
    price=request.POST['price']
    updated_price=float(price)
    total_price=int(qty)*updated_price
    data=float(total_price)
    context={
        'data':data,
    }
    print("------------------------>context :",data)
    return JsonResponse({'context':context})

def add_order(request):
    customer_id=request.POST['customer_id']
    product_id=request.POST['product_id']
    price=request.POST['price']
    qtyvalue=request.POST['qtyvalue']
    total=request.POST['total']

    print("-----> customer_id",customer_id)
    print("-----> total",total)
    pid=Product.objects.get(id=product_id)
    cid=Customer.objects.get(id=customer_id)
    print("---> unit price",pid.unit_price)
    oid=Order.objects.create(customer_id=cid,product_id=pid,unit_price=pid.unit_price,qty=qtyvalue,total_price=total)
    result="order added successfully"
    context = {
        'data': result,
    }
    print("----->successfully added",result)
    return JsonResponse({'context': context})

def order(request):
    c_all = Customer.objects.all()
    p_all = Product.objects.all()
    context = {
        'c_all': c_all,
        'p_all': p_all,
    }
    return render(request, "myapp/orderform.html", {'context': context})

def del_order(request,pk):
    orderid=Order.objects.get(id=pk)
    orderid.delete()

    return HttpResponseRedirect(reverse('home'))

def update_order(request,uk):
    print("---->uk",uk)
    oid=Order.objects.get(id=uk)
    print("oduidiid",oid)
    pid=Product.objects.get(name=oid.product_id)
    cid=Customer.objects.get(first_name=oid.customer_id)
    context={
        'oid':oid,
        'pid':pid,
        'cid':cid,
    }
    print("----------------->cid",cid.first_name)
    return render(request, "myapp/updateorder.html",{'context':context})

def update_data(request):
    oid=request.POST['orderid']
    total_price=request.POST['totalprice']
    o=Order.objects.get(id=oid)
    print("---->oid",o)
    print("--###########################")
    #oid = Order.objects.get(id=oid)
    print("---> oid update value ",o.total_price)
    o.total_price=total_price
    o.save()
    return HttpResponseRedirect(reverse('home'))

def search_value(request):
    name = request.POST['searchname']
    print("-------> name",name)
    cid=Customer.objects.filter(first_name=name)
    print("---> search cid",cid[0].id)
    data=Order.objects.filter(customer_id=cid[0].id)
    print("----->data with customer wise", data)
    cdata=list(cid.values())
    data=list(data.values())
    if data:
        context = {
            'cdata':cdata,
            'data': data,
        }
        return JsonResponse({'context': context})
    else:
        pid=Product.objects.filter(name=name)
        data = Order.objects.filter(product_id=pid)
        print("----->data with product wise",data)
        data = list(data.values())
        context = {
            'data': data,
        }
        return JsonResponse({'context': context})

    # print(len(name))
    # if len(name) != 0:
    #     print("---------------->", name)
    #     data = User.objects.filter(name=name)
    #     data = list(data.values())
    #     print("------------->", data)
    #     if data:
    #         status = "result found"
    #     else:
    #         status = "no result found"
    # else:
    #     data = User.objects.values()
    #     data = list(data)
    #     if data:
    #         status = "result found"
    #     else:
    #         status = "no result found"

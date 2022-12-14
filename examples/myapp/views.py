from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

data = {
    "telefon" : "telefon kategorisindeki ürünler",
    "bilgisayar" : "bilgisayar kategorisindeki ürünler",
    "elektronik" : "eektronik kategorisindeki ürünler"
}

def index(request):
    return render (request,'myapp/index.html')

def details(request):
    return HttpResponse("details")

def getProductsByCategoryId(request, category_id):
    category_list = list(data.keys())
    if category_id > len(category_list):
        return HttpResponseNotFound("yanlış kategori seçimi")
    redirect_text = category_list[category_id-1]
    return redirect("/products/" + redirect_text)
    
def getProductsByCategory(request, category):
    try:
        category_text = data[category]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("yanlış kategori seçimi")






from django.shortcuts import render, redirect
from .forms import CeleryForm, ParagonForm
from dupa.models import Paragon
import pytesseract

from .tasks import mul,items_from_image

from PIL import Image, ImageFilter

def start_page(request):
    return render(request,'base.html')

def produkty(request):
    return render(request, 'produkty.html')

def numbers(request):
    if request.method == "POST":
        form = CeleryForm(request.POST or None)
        if form.is_valid():
          #  new_join = form.save(commit=False)
          #  new_join.ip_address = get_ip(request)
          #  new_join.ref_id = get_ref_id()
          #  new_join.save()
            num1=int(request.POST.get('number_1'))
            num2=int(request.POST.get('number_2'))
            print(type(num1))
            mul.delay(num1,num2)
    #    return HttpResponseRedirect('/%s' % (new_join.ref_id))
    else:
        form = CeleryForm()
        
    context = {'form':form}
    return render(request, 'numbers.html', context)

def paragon_base(request):
    context={}
    return render(request, 'dupa/base_paragon.html', context)


def lista_paragonow(request):
    qs = Paragon.objects.filter(user1=request.user)[::-1]   #.reverse()
    context={}
    try:
        itemki =[]
        for i in qs:
            itemki.append(i.paragonitems_set.all())
        context['itemki'] = itemki

    except:
        pass
    context['qs'] = qs
    return render(request, 'dupa/paragon_list2.html', context)


def analyse_image(image):
    im = Image.open(image)
    exif_data = im._getexif()
    return exif_data

def tesseract_analyse(image):
    dane = pytesseract.image_to_string(Image.open(image))
    return dane


def add_receipt(request):
    if request.method == 'POST':
        form =ParagonForm(request.POST, request.FILES)
        print(request.FILES['image'])
        if form.is_valid():
            new_rec =form.save(commit=False)
            #new_rec.image_data =tesseract_analyse(request.FILES['image']) 
            new_rec.user1=request.user            
            new_rec.save()
            print('filenme', new_rec.image.name)
          
#hj=Paragon.objects.get(image='IMG_20170113_191541_iKnevFQ.jpg')
            print(4* 'id ', new_rec.id)

            items_from_image.delay(new_rec.image.name)
            return redirect('paragony:lista_paragonow')
    else:
        form =ParagonForm()
    
    context = {'form':form}
    return render (request, 'dupa/paragon_form.html', context)



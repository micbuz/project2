from django.shortcuts import render, HttpResponseRedirect
from .forms import EmailForm, JoinForm
from .models import Join



def share(request, ref_id):
    context={'ref_id':ref_id}
#    context = {}
    print(ref_id)
    return render(request, 'share.html', context)


def get_ip(request):
    try:
        x_forward = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forward:
            ip = x_forward.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    except:
        ip = ''

    return ip

import uuid
def get_ref_id():
    ref_id = str(uuid.uuid4())[:11].replace('-','').lower()

    try:
        id_exists = Join.objects.get(ref_id=ref_id)
        return get_ref_id()
    except:
        return ref_id


def email_form(request):
    print(request.POST)
    print(request.META.get('REMOTE_ADDR'))
    print(request.META.get('HTTP_X_FORWARDED_FOR'))
    d=get_ip(request)
    print('d:',d)
    
    if request.method == "POST":
        form = JoinForm(request.POST or None)
        if form.is_valid():
            new_join = form.save(commit=False)
            new_join.ip_address = get_ip(request)
            new_join.ref_id = get_ref_id()
            new_join.save()
        return HttpResponseRedirect('/%s' % (new_join.ref_id))
    else:
        form = JoinForm()
    context = {'form':form}
    return render(request, 'email.html', context)



from django.shortcuts import render
from RV.models import RunicheskiyVosk
from django.views.generic import View
from .forms import RunaForm
from django.shortcuts import redirect
from .utils import *


# Create your views here.
class RasskladView(View):
    def get(self, request):
        form = RunaForm()
        return render(request, 'RV/index.html', context={'form': form })

    def post(self, request):
        form = RunaForm()
        return render(request, 'RV/index.html', context={'form': form } )


def RasskladShow(request):
    form = RunaForm(request.POST)

    if form.is_valid():
        form_cleaned_data = form.cleaned_data
        direct_order, reverse_order = \
            generate_order_answer(form_cleaned_data)

    context = {
            'form': form, 'direct_order': direct_order,
            'reverse_order': reverse_order
            }

    return render(request,'RV/runicheskiy_vosk.html', context=context)

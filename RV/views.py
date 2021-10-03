from django.shortcuts import render
from RV.models import RunicheskiyVosk
from RV.models import ManticKeys
from django.views.generic import View
from .forms import RunaForm, ManticForm
from django.shortcuts import redirect
from .utils import *


# Create your views here.
class RvIndex(View):
    def get(self, request):
        form = RunaForm()
        return render(request, 'RV/rv_index.html', context={'form': form})

    def post(self, request):
        form = RunaForm()
        return render(request, 'RV/rv_index.html', context={'form': form } )


class RvResult(View):
    def get(self, request):
        form = RunaForm()
        return render(request, 'RV/rv_result.html', context={'form':form})

    def post(self, request):
        form = RunaForm(request.POST)
        context = {
            'form': form
        }

        if form.is_valid():
            obj_form = form.save()
            form_cleaned_data = form.cleaned_data
            answers_keys = \
                generate_order_answer(form_cleaned_data)

            context['obj_form'] = obj_form
            for i in answers_keys.values():
                obj_mk = ManticKeys.objects.get(value_keys = i)#
                obj_form.mantickeys_set.add(obj_mk)#
            obj_form.save()
            context['obj_form'] = obj_form
            return render(request,'RV/rv_result.html', context=context)

        return render(request,'RV/rv_index.html', context=context)

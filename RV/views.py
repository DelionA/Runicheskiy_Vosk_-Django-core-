from django.shortcuts import render
from RV.models import RunicheskiyVosk
from RV.models import AnswersKeys
from django.views.generic import View
from .forms import RunaForm
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
            answers_keys['rv_answers_keys']=obj_form
            obj_ak = AnswersKeys.objects.create(**answers_keys)
            context['obj_ak']=obj_ak

            return render(request,'RV/rv_result.html', context=context)

        return render(request,'RV/rv_index.html', context=context)

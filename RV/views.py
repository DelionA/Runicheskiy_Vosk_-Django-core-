from django.shortcuts import render
from RV.models import RunicheskiyVosk
from django.views.generic import View
from .forms import RunaForm
from .forms import RunaFormResult
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
            # print('**************')
            form_cleaned_data = form.cleaned_data
            direct_order, reverse_order = \
                generate_order_answer(form_cleaned_data)



            context = {
                    'form': form,
                     'direct_order': direct_order,
                    'reverse_order': reverse_order
                    }
            return render(request,'RV/rv_result.html', context=context)

        return render(request,'RV/rv_index.html', context=context)

from django.shortcuts import render, redirect
from django.urls import reverse
from crispy.forms import BasicForm
from django.contrib import messages
from django.views import View

# Create your views here.

class MyView(View):
    template_name = None
    def get(self, request):
        old_data = {
            'title':'SakaiCar',
            'mileage' :42,
            'purchase_date':'2018-08-14'
            }
        form = BasicForm(initial=old_data)
        ctx={'form':form}

        return render(request,self.template_name,ctx)

    def post(self, request):
        form = BasicForm(request.POST)

        if not form.is_valid():
            ctx = {'form':form}
            return render(request, self.template_name, ctx)

        messages.add_message(request, messages.SUCCESS, 'Data saved.')

        return redirect(reverse('crispy:main'))

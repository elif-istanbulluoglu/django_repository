from django.shortcuts import render, HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from . import models
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
#def index(request):
   # return HttpResponse("Hello, world.")

def index(request):
         return render(request, 'index.html')
def about(request):
     return render(request, 'about.html')

def destinations(request):
       all_destinations = models.Destination.objects.all()
       return render(request, 'destinations.html', {'destinations': all_destinations})
       
class DestinationDetailView(generic.DetailView):
    template_name = 'destination_detail.html'
    model = models.Destination
    context_object_name = 'destination'

class DestinationCreateView(generic.CreateView):
      model = models.Destination
      fields = ['name', 'description']
      template_name = 'destination_form.html'

class DestinationUpdateView(generic.UpdateView):
      model = models.Destination
      fields = ['name', 'description']
      template_name = 'destination_form.html'

class DestinationDeleteView(generic.DeleteView):
      model = models.Destination
      template_name = 'destination_confirm_delete.html'
      success_url = reverse_lazy('destinations')
      

class CruiseDetailView(generic.DetailView):
    template_name = 'cruise_detail.html'
    model = models.Cruise
    context_object_name = 'cruise'

class InforequestCreate(SuccessMessageMixin, generic.CreateView):
    model = models.InfoRequest
    fields = ['name', 'email', 'cruise', 'notes']
    success_message = "Thank you %(name)s! We will email you when we have more information about %(cruise)s!."
    template_name = 'info_request_create.html'
    success_url = reverse_lazy('index')
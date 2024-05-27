from django.shortcuts import render, reverse
from django.views import generic
from .models import Facility
from .forms import FacilityCreateForm
from .utils import generate_random_id
from django.views import generic
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse
# Create your views here.
class LandingPageView(generic.TemplateView):
    template_name = "facilities/landing_page.html"

class FacilityListView(generic.ListView):
    template_name = "facilities/facility_list.html"
    
    def get_queryset(self):
        return Facility.objects.all()

class FacilityCreateView(generic.CreateView):
    template_name = "facilities/create_facility.html"
    form_class = FacilityCreateForm

    def form_valid(self, form):
        district_code = form.cleaned_data['district'].district_code
        facility_code = generate_random_id(district_code)
        form.instance.facility_code = facility_code
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("core:facility-list")


# class SignoutView(generic.RedirectView):
#     permanent = False
#     query_string = True   

#     def get_redirect_url(self):
#         logout(self.request)
#         messages.success(self.request, 'You are now logged out')
#         return reverse('login')
from django.urls import path
from . import views
from .views import LandingPageView, FacilityListView, FacilityCreateView

app_name = "core"

urlpatterns = [
      path('', LandingPageView.as_view(), name="landing-page"),
      path('facilities/', FacilityListView.as_view(), name="facility-list"),
      path('facilities/create/', FacilityCreateView.as_view(), name="create-facility"),
    #   path('logout/', SignoutView.as_view(), name='logout'),
]

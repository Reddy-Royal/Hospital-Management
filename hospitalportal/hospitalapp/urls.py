from django.urls import path
from . import views
from django.contrib.auth import views as a
urlpatterns = [
	path('',views.home,name= "hm"),
	path('abt/',views.about,name= "ab"),
	path('cnt/',views.contact,name= "ct"),
	path('signup/',views.signup,name= "su"),
	path('lgo/',a.LoginView.as_view(template_name="html/login.html"),name="lg"),
	path('lgt/',a.LogoutView.as_view(template_name="html/logout.html"),name="lgtn"),
	path('arogyasri/',views.arogyasricr,name="agscr"),
	path('docpro/',views.docprocr,name="docprof"),
	path('staffl/',views.staffcrt,name='staffct'),
]
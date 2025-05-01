from django.shortcuts import render,redirect
from . forms import UserForm,ReForm,UsupForm,docform,stafform
from . models import User,staff,docprofile

# Create your views here.

def home(request):
	k = staff.objects.filter(usj_id=request.user.id)
	f = staff.objects.all()
	s = docprofile.objects.all()
	sdt,jct = {},{}
	for i in s:
		sdt[i.id]=i.id,i.dname,i.mobilenum
	for j in f:
		if j.jcmp_id in sdt:
			jct[j.id]=j.jtitle,j.jexpr,j.jreq,j.jcrtm,i.dname,j.jsal,sdt[j.jcmp_id][0],sdt[j.jcmp_id][1]
	


	return render(request,'html/home.html',{'rj':k,'uj':jct.values()})

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')
def signup(request):
	if request.method == "POST":
		g = UserForm(request.POST)
		if g.is_valid():
			g.save()
			return redirect('/lgo')
	g = UserForm()
	return render(request,'html/signup.html',{'t':g})
def arogyasricr(request):
	w = User.objects.get(id=request.user.id)
	if request.method == "POST":
		t = ReForm(request.POST)
		y = UsupForm(request.POST,instance=w)
		if t.is_valid() and y.is_valid():
			k=t.save(commit=False)
			k.usd_id = request.user.id
			w.has_arogyasri = 1
			w.save()
			y.save()
			k.save()
			return redirect('/')
	t = ReForm()
	y = UsupForm(instance=w)
	return render(request,'html/arogyasricr.html',{'q':y,'r':t})
def docprocr(request):
	v = User.objects.get(id=request.user.id)
	if request.method=="POST":

		h = docform(request.POST)
		if h.is_valid():
			w = h.save(commit=False)
			w.usd_id = request.user.id
			v.has_hospital = 1
			w.save()
			v.save()
			return redirect('/')
	h = docform()
	return render(request,'html/docpr.html',{'b':h})
def staffcrt(request):
	h = staff.objects.filter(usj_id=request.user.id)
	if request.method == "POST":
		t = stafform(request.POST)
		if t.is_valid():
			c = t.save(commit=False)
			c.usj_id = request.user.id
			c.jcmp_id = request.user.docprofile.id
			c.save()
			return redirect('/staffl')
	t = stafform()
	return render(request,'html/staffl.html',{'w':t,'s':h})

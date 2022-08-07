from django.shortcuts import render, redirect
from .models import StudentModel
from .forms import StudentForm

def home(request):
	data = StudentModel.objects.all()
	return render(request, 'home.html', {'data':data})

def create(request):
	if request.method == "POST":
		f = StudentForm(request.POST, request.FILES)
		if f.is_valid():
			f.save()
			fm = StudentForm()
			return render(request, 'create.html', {'fm':fm, 'msg':'record created'})
		else:
			return render(request, 'create.html', {'fm':f, 'msg':'check errors'})
	else:
			fm = StudentForm()
			return render(request, 'create.html', {'fm':fm})

def delete(request, id):
	d = StudentModel.objects.get(rno=id)
	d.file.delete()
	d.delete()
	return redirect('home')

from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from .forms import PersonForm
from .models import Clientes,Servicos,Cliente_servicos


#@login_required
def index(request):
	return render(request,'index.html')

#@login_required
def persons_list(request):
	clientes = Clientes.objects.all()[:100]
	return render(request,'person.html',{'persons':clientes})

#@login_required
def persons_new(request):
	form = PersonForm(request.POST, None)
	if form.is_valid():
		form.save()
		return redirect('persons_new')
	return render(request, 'person_form.html',{'form':form})

#@login_required
def persons_update(request,id_cliente):

	person = get_object_or_404(Person, pk=id_cliente)
	form = PersonForm(request.POST or None, instance=person)

	if form.is_valid():
		form.save()
		return redirect('persons_list')
	return render(request,'person_form.html',{'form': form})

#@login_required
def persons_delete(request, id_cliente):
	person = get_object_or_404(Person, pk=id_cliente)

	if request.method == 'POST':
		person.delete()
		return redirect('persons_list')
	return render(request,'person_delete_confirm.html',{'person':person})

def servicelist(request):
	services = Servicos.objects.all()
	return render(request,'servicelist.html',{'services':services})


def cesta(request):
	cesta = Cliente_servicos.objects.all()
	return render(request,'cesta.html',{'cestas':cesta})

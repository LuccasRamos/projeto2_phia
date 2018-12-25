from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.template import Context, loader
from .models import Person
from .forms import PersonForm


from .models import Question, Cliente
# Create your views here.

def index1(request):
	client_list = Cliente.objects.order_by('-pub_date')[:5]
	context = {'client_list':client_list}
	return render(request,'app1/index.html',context)

# Leave the rest of the views (detail, results, vote) unchanged

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def hello(request):
	return HttpResponse("TESTE")

def link2(request):
	return HttpResponse("Pagina de teste link2")

def link3(request,num):
	return HttpResponse("Numero escolhido foi o: "+str(num))


def link4(request, nome):
	return HttpResponse("O Nome e o :"+str(request)+str(nome))

def lerdobanco(v_nome):
		lista_nome = [
			{'nome': 'a', 'idade':'24'},
			{'nome': 'b', 'idade':'23'},
			{'nome': 'c', 'idade':'26'},
		]

		for pessoa in lista_nome:
			if pessoa['nome']==v_nome:
				return pessoa
			else:
				return {'nome':'Nao encontrado','idade':0}

def fname(request,v_nome_2):
	result = lerdobanco(v_nome_2)
	if int(result['idade']) > 0:
		return HttpResponse(str('A pessoa foi encontrada e ela tem: '+result['idade'] + ' anos'))
	else:
		return HttpResponse('Ninguem foi encontrado')

def artigos(request,nome_candango):
	pessoa = lerdobanco(nome_candango)['idade']
	return render(request,'artigos.html',{'v_pessoa':pessoa})


def principal(request):
	return render(request,'index_1.html') #apaga saporra depois pq ja tem o index criado com a mesma rota. 

def index(request):
	return render(request,'index_1.html')

def person_list(request):
	persons = Person.objects.all()
	return render(request,'person.html',{'persons':persons})

def person_new(request):
	form = PersonForm(request.POST, None)
	if form.is_valid():
		form.save()
		return redirect('person_new')
	return render(request, 'person_form.html',{'form':form})

def person_update(request,id):
	person = get_object_or_404(Person, pk=id)
	form = PersonForm(request.POST or None, instance=person)

	if form.is_valid():
		form.save()
		return redirect('persons_list')

	return render(request,'person_form.html',{'form': form})

def person_delete(request, id):
	person = get_object_or_404(Person, pk=id)

	if request.method == 'POST':
		person.delete()
		return redirect('persons_list')

	return render(request,'person_delete_confirm.html',{'person':person})
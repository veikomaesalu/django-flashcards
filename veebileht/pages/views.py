from django.shortcuts import render

def home(request):
	return render(request, "home.html", {})






def add(request):
	from random import randint
	num1 = randint(0,10)
	num2 = randint(0,10)

	if request.method == "POST":
		answer = request.POST['vastus']
		vana_num_1 = request.POST['vana_num1']
		vana_num_2 = request.POST['vana_num2']

		correct_answer = int(vana_num_1) + int(vana_num_2)
		if correct_answer == int(answer):
			minu_vastus = "ÕIGE!"
		else:
			minu_vastus = "VALE!"
		return render(request, "add.html", 
		{'minuvastus':minu_vastus,
		'num_1':num1,
		'num_2':num2 })


	return render(request, "add.html",
	{'num_1':num1,
	'num_2':num2 })

def subst(request):
	from random import randint
	arv1 = randint(0,10)
	arv2 = randint(0,10)

	if request.method == "POST":
		vastus_tagasi = request.POST['vastus']
		esimene_nr_tagasi = request.POST['esimene_arv']
		teine_nr_tagasi = request.POST['teine_arv']
		oige_vastus = int(esimene_nr_tagasi) - int(teine_nr_tagasi)
		if oige_vastus == int(vastus_tagasi):
			minu_vastus = "Õigus!!! " + esimene_nr_tagasi + ' - ' + teine_nr_tagasi + ' on ' + str(vastus_tagasi)
		else:
			minu_vastus = "Vale!!!  " + esimene_nr_tagasi + ' - ' + teine_nr_tagasi + ' ei ole ' + str(vastus_tagasi)
		return render(request, "subst.html", 
			{'vastus_tagasi':vastus_tagasi,
			 'minu_vastus':minu_vastus,
			 'arv1':arv1,
		 	 'arv2':arv2})

	return render(request, "subst.html", 
		{'arv1':arv1,
		 'arv2':arv2})
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


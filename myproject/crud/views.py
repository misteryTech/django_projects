from django.shortcuts import render, redirect, get_object_or_404
from .models import Person



from django.shortcuts import render
from .models import Person

def insert_data(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')

        Person.objects.create(name=name, email=email, age=age)

    records = Person.objects.all()
    return render(request, 'insert_form.html', {'records': records})




def edit_data(request, id):
    record = get_object_or_404(Person, id=id)

    if request.method == "POST":
        record.name = request.POST.get('name')
        record.email = request.POST.get('email')
        record.age = request.POST.get('age')
        record.save()
        return redirect('insert_data')

    return render(request, 'edit_form.html', {'record': record})


def delete_data(request, id):
    record = get_object_or_404(Person, id=id)
    record.delete()
    return redirect('insert_data')

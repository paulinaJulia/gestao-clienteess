from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import person
from .form import personForm

@login_required

def persons_list(request):
    persons = person.objects.all()
    return render(request, 'person.html', {'persons': persons})

@login_required
def persons_new(request):
    form = personForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})

@login_required
def person_update(request, id):
    Person = get_object_or_404(person, pk=id)
    form = personForm(request.POST or None, request.FILES or None, instance=Person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})

@login_required
def person_delete(request, id):
    Person = get_object_or_404(person, pk=id)

    if request.method == 'POST':
        Person.delete()
        return redirect('person_list')
    return render(request, 'person_delete_confirm.html', {'person': person})


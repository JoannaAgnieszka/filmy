from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View

from movie_app.models import Person, Category, Movie
from movie_app.forms import MovieForm


class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


class AddPersonView(View):

    def get(self, request):
        return render(request, 'add_person.html')

    def post(self, request):
        fn = request.POST.get('first_name', '')  # request.POST['first_name']
        ln = request.POST.get('last_name', '')
        Person.objects.create(first_name=fn, last_name=ln)
        return redirect(reverse("person"))


class ListMovieView(View):

    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movie_list.html", {'movies': movies})

class ListCategoryView(View):

    def get(self, request):
        categories = Category.objects.all()
        return render(request, "category_list.html", {'categories': categories})

class ListPersonView(View):

    def get(self, request):
        persons = Person.objects.all()
        return render(request, "person_list.html", {'persons': persons})



class AddCategoryView(View):

    def get(self, request):
        return render(request, 'add_category.html')

    def post(self, request):
        name = request.POST.get('name', '')
        Category.objects.create(name=name)
        return redirect(reverse('category'))


class AddMovieView(View):

    def get(self, request):
        form = MovieForm()
        return render(request, 'add_obj.html', {'form': form})

    def post(self, request):
        form = MovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            year = form.cleaned_data['year']
            Movie.objects.create(title=title, year=year)
            return redirect(reverse('movie'))
        return render(request, 'add_obj.html', {'form': form})

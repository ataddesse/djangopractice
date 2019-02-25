
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Album
from .forms import UserForm

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration.html'
    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    def get(self, request):
        user =form.save(commit=False)

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.Set_password(password)
        user.save()

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')
        return render(request, self.template_name, {'form':form})



class IndexView(generic.ListView):
    template_name = 'music/index.html'
    def get_queryset(self):
         return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields= ['artist', 'album_title', 'genre', 'album_logo' ]

class AlbumUpdate(UpdateView):
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']
class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('index')
def home(request):
    return render(request, "home.html", {})
def about(request):
    return render(request, "about.html", {})
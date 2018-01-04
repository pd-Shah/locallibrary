from django.shortcuts import render
from django.views import generic

from . import models


class Index(generic.TemplateView):

    template_name='catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_books'] = models.Book.objects.all().count()
        context['num_instances'] = models.BookInstance.objects.all().count()
        context['num_instances_available'] = models.BookInstance.objects.filter(status__exact='a').count()
        context['num_authors'] =models.Author.objects.count()
        return context

class BookListView(generic.ListView):
    model=models.Book
    template_name='catalog/book_list.html'

class BookDetailView(generic.DetailView):
    model = models.Book
    template_name='catalog/book_detail.html'

class AuthorListView(generic.ListView):
    model = models.Author
    template_name = 'catalog/author_list.html'

# def index(request):
#     """
#     View function for home page of site.
#     """
#     # Generate counts of some of the main objects
#     num_books=models.Book.objects.all().count()
#     num_instances=models.BookInstance.objects.all().count()
#     # Available books (status = 'a')
#     num_instances_available=models.BookInstance.objects.filter(status__exact='a').count()
#     num_authors=models.Author.objects.count()  # The 'all()' is implied by default.
#
#     # Render the HTML template index.html with the data in the context variable
#     return render(
#         request,
#         'catalog/index.html',
#         context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
#     )

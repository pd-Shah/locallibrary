from django.shortcuts import render
from . import models

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=models.Book.objects.all().count()
    num_instances=models.BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=models.BookInstance.objects.filter(status__exact='a').count()
    num_authors=models.Author.objects.count()  # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'catalog/index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )

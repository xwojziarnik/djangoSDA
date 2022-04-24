from django.forms import Form, CharField, ModelForm
import logging

from books.models import BookAuthor, Book

logger = logging.getLogger("forms_logger")

class CategoryForm(Form):
    name = CharField(max_length=156, required=True)

    def clean_name(self):
        logger.info(self.cleaned_data)
        return self.cleaned_data.get("name")

class AuthorForm(ModelForm):
    class Meta:
        model = BookAuthor
        exclude = []

    name = CharField(min_length=3, max_length=256, required=True)

    def clean(self):
        result = super().clean()
        logger.info(f"AuthorForm - clean run - result is {result}")
        return result

class BookForm(ModelForm):
    class Meta:
        model = Book
        # exclude = []
        fields = [
            "title",
            "authors",
            "publisher",
            "published_date",
            "categories",
            "average_rating",
        ]

    title = CharField(min_length=3, max_length=256, required=True)

    def clean(self):
        result = super().clean()
        logger.info(f"BookForm - clean run - result is {result}")
        return result
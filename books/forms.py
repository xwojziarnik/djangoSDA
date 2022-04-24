from django.forms import Form, CharField
import logging

logger = logging.getLogger("forms_logger")

class CategoryForm(Form):
    name = CharField(max_length=156, required=True)

    def clean_name(self):
        logger.info(self.cleaned_data)
        return self.cleaned_data.get("name")
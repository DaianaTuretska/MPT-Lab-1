from django.forms.models import BaseInlineFormSet

from .models import ArticleImage


class ArticleImageInlineFormSet(BaseInlineFormSet):
    def save_new(self, form, commit=True):
        """Override save_new to handle multiple files."""
        images = form.cleaned_data.pop("image", [])
        instances = []
        common_data = {
            field: form.cleaned_data[field]
            for field in form.cleaned_data
            if field in form._meta.fields
        }
        for img in images:
            instance = ArticleImage(**common_data, image=img)
            if commit:
                instance.save()
            instances.append(instance)
        # Note: Returning multiple instances may require additional adjustments
        # since admin inline formsets typically expect one instance per form.
        # You might need to customize how the inline formset handles these extra instances.
        return instances[0] if instances else None

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, ArticleToTag, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class ArticleToTagFormset(BaseInlineFormSet):
    def clean(self):
        has_main = False
        for form in self.forms:
            is_main = form.cleaned_data.get('is_main')
            if is_main and not has_main:
                has_main = True
                continue
            elif not is_main:
                continue
            elif is_main and has_main:
                raise ValidationError('Главный раздел может быть только один!')
        if not has_main:
            raise ValidationError('Нужен хотя бы один главный раздел!')
        return super().clean()


class ArticleToTagInline(admin.TabularInline):
    model = ArticleToTag
    formset = ArticleToTagFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleToTagInline]

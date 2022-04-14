from pyexpat import model
from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError

from .models import Article, Scope, ArticleScope


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        scopes_quantity = len(
            [form.cleaned_data['is_main'] for form in self.forms if form.cleaned_data['is_main'] == True]
        )
        
        if scopes_quantity == 0:
            raise ValidationError('Укажите основной раздел')
        elif scopes_quantity > 1:
            raise ValidationError('Основным может быть только один раздел')

        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline,]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', ]

from pyexpat import model
from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError

from .models import Article, Scope, ArticleScope


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_scopes_cnt = 0

        for form in self.forms:
            if form['is_main'].data == True:
                main_scopes_cnt += 1
                #from.cleaned_data.get('is_main')
        
        if main_scopes_cnt == 0:
            raise ValidationError('Укажите основной раздел')
        elif main_scopes_cnt > 1:
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

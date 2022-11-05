from django.contrib import admin
from django.core.exceptions import ValidationError

from django.forms import BaseInlineFormSet
from .models import Article, Tag, ArticleTag


class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        if len(self.forms) == 0:
            raise ValidationError('Нет ни одного тега')
        self.count_tag_is_main = 0

        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data.get('is_main') and (form.cleaned_data.get('DELETE') == False):
                self.count_tag_is_main += 1
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        if self.count_tag_is_main == 0:
            raise ValidationError(f'Выберите главный тег')
        if self.count_tag_is_main > 1:
            raise ValidationError(f'Выбрано {self.count_tag_is_main} тегов, главный может быть один')
        return super().clean()  # вызываем базовый код переопределяемого метода



# @admin.register(ArticleTag)
class ArticleTagInline(admin.TabularInline):
    # list_display = ['article', 'tag', 'is_main']
    model = ArticleTag
    formset = ArticleTagInlineFormset
    extra = 0

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    # inlines = [ArticleTagInline]

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagInline]
    list_display = ['title', 'text', 'published_at', 'articletag']



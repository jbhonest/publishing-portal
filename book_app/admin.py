from django.contrib import admin
from .models import Publisher, Author, Book


class AuthorFilter(admin.SimpleListFilter):
    title = 'author'
    parameter_name = 'author'

    def lookups(self, request, model_admin):
        authors = set(Author.objects.all())
        return [(author.id, author.name) for author in authors]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(authors__id=self.value())
        return queryset


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'website', 'city', 'country')
    search_fields = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name', 'email')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_authors',
                    'publisher', 'publication_date')
    list_filter = ('publication_date', AuthorFilter, 'publisher')
    search_fields = ('title',)
    filter_horizontal = ('authors',)

    def get_authors(self, obj):
        return ", ".join(author.name for author in obj.authors.all())
    get_authors.short_description = 'Author(s)'

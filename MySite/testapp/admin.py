from django.contrib import admin

from testapp.models import Rubric


# class RubricAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'parent')
#     # list_display_links = ('id', 'title')
#     # search_fields = ('title',)
#     # prepopulated_fields = {'slug': ('title',)}


admin.site.register(Rubric)


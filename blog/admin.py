from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
# fields display on change list
	list_display = ['title', 'description']
# fields to filter the change list with
	list_filter = ['published', 'created']
#fields to search in change list
	search_fields = ['title', 'description', 'content']
#Enable the date drill down on the change list
	date_hierarchy = 'created'
# enable save button on top of change list
	save_on_top = True
#Prepopulate the slug from the title
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)

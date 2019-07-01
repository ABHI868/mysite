from django.contrib import admin
from .models import Post,Comment


@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
	list_display=('title','slug','author','publish','status')
	list_filter=('status','author','publish','created')
	search_fields=('title','body')
	ordering=('status','publish')
	date_hierarchy='publish'
	prepopulated_fields={'slug':('title',)}
	raw_id_fields=('author',)

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
	list_display=('name' ,'email','post','created','active')
	list_filter=('created','updated','active')
	search_fields=('name' ,'email','body')
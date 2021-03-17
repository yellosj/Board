from django.contrib import admin

# Register your models here.

from .models import Board   # 추가
# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'content', 'created_date', 'modified_date')


admin.site.register(Board, BoardAdmin)


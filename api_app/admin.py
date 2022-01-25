from django.contrib import admin
from .models import CartItem


# class TokenAdmin(admin.ModelAdmin):
#     list_display = ('key', 'user', 'created')
#     fields = ('user',)
#     ordering = ('-created',)


# admin.site.unregister(Token)
# admin.site.register(Token, TokenAdmin)
admin.site.register(CartItem)

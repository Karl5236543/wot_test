from django.contrib import admin
from django.utils.html import format_html
from django.shortcuts import reverse
from .forms import TankForm, PlayerForm

from .models import Player, Tank, TankProperties

class InlineTankProperty(admin.StackedInline):
    model = TankProperties
    extra = 1


@admin.register(Tank)
class TankAdmin(admin.ModelAdmin):
    # list_display = ('get_name', 'lvl', 'get_premium')
    # list_editable = ('lvl', )
    # fields = ('name', 'premium', 'type', 'lvl', 'get_name')
    readonly_fields = ('get_name', )
    form = TankForm
    inlines = [
        InlineTankProperty,
    ]

    fieldsets = (
        (None, {
            'fields': (
                'name',
                'premium',
                'photo',
            ),
        }),
        ('доп инфа', {
            'fields': (
                'type',
                'lvl',
            ),
        }),
        ('описание', {
            'fields': (
                'get_name',
            ),
            'classes': ('collapse', ),
        })



    )

    @admin.display(description='NAME')
    def get_name(self, obj):
        return format_html(
            '<span style="color: {};">{}</span>',
            self._get_tank_name_color(obj),
            obj.name,
        )

    def _get_tank_name_color(self, obj):
        if obj.premium:
            return '#937400'
        return ''

    
    @admin.display(description='LVL')
    def get_lvl(self, obj):
        return obj.lvl

    @admin.display(description='PREMIUM', boolean=True)
    def get_premium(self, obj):
        return obj.premium


    def get_list_display(self, request):
        return ('get_name', 'lvl', 'get_premium')

    

    def get_queryset(self, request):
        return Tank.objects.filter(premium=True)


    @admin.display(description='коментарий')
    def get_text_for_premium(self, obj):
        return """
        Ого, да это же прем танк!
        """

    
    def get_fields(self, request, obj=None):
        fields = list(super().get_fields(request, obj))
        if obj:
            fields.remove('premium')
        return fields

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    form = PlayerForm
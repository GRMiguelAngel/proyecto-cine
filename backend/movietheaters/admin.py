from django.contrib import admin
from .models import MovieTheater, Seat

# Register your models here.

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['number', 'row', 'movietheater']

class SeatInline(admin.TabularInline):
    model = Seat
    extra = 0
    can_delete = False
    readonly_fields = ('number', 'row')
    max_num = 0

@admin.register(MovieTheater)
class MovieTheaterAdmin(admin.ModelAdmin):
    list_display = ['number']
    inlines = [SeatInline]


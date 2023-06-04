from django.contrib import admin
from .models import Annonce, Maison, Reservation, Commentaire

@admin.register(Annonce)
class AnnonceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'location', 'owner')
    list_filter = ('location', 'owner')
    search_fields = ('title', 'location', 'owner__username')

@admin.register(Maison)
class MaisonAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'is_available')
    list_filter = ('city', 'is_available')
    search_fields = ('name', 'address', 'city')
    actions = ['mark_as_available', 'mark_as_unavailable']

    def mark_as_available(self, request, queryset):
        queryset.update(is_available=True)
        self.message_user(request, 'Selected houses have been marked as available.')

    def mark_as_unavailable(self, request, queryset):
        queryset.update(is_available=False)
        self.message_user(request, 'Selected houses have been marked as unavailable.')

    mark_as_available.short_description = 'Mark selected houses as available'
    mark_as_unavailable.short_description = 'Mark selected houses as unavailable'

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('maison', 'user.username', 'start_date', 'end_date', 'is_active')
    list_filter = ('maison', 'is_active')
    search_fields = ('maison__name', 'user__username')
    actions = ['activate_reservations', 'deactivate_reservations']

    def activate_reservations(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, 'Selected reservations have been activated.')

    def deactivate_reservations(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, 'Selected reservations have been deactivated.')

    activate_reservations.short_description = 'Activate selected reservations'
    deactivate_reservations.short_description = 'Deactivate selected reservations'

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('maison', 'user.username', 'content', 'created_at')
    list_filter = ('maison',)
    search_fields = ('maison__name', 'user__username')

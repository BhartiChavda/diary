from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('users/', views.manage_users, name='manage_users'),
    path('notes/', views.manage_notes, name='manage_notes'),
    path('view-note/<int:note_id>/', views.view_note, name='admin_view_note'),
    path('categories/', views.manage_categories, name='manage_categories'),
    path('delete-note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('toggle-user-status/<int:user_id>/', views.toggle_user_status, name='toggle_user_status'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('edit-user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('contacts/', views.manage_contacts, name='manage_contacts'),
    path('delete-contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    # Visibility
    path('post-visibility/', views.public_private_notes, name='public_private_notes'),
    # Moderation
    path('pending-approvals/', views.pending_approvals, name='pending_approvals'),
    path('approve-note/<int:note_id>/', views.approve_note, name='approve_note'),
    path('reject-note/<int:note_id>/', views.reject_note, name='reject_note'),
]

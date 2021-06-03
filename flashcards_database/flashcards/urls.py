from django.urls import path
from . import views

urlpatterns = [
    path('collection/', views.CollectionList.as_view()),
    path('collection/<int:collection_id>/', views.CollectionDetail.as_view()),
    path('collection/<int:collection_id>/flashcard/', views.FlashcardList.as_view()),
    path('collection/<int:collection_id>/flashcard/<int:card_id>/', views.FlashcardDetail.as_view()),
]

from django.urls import path
from .views import PostListView,AuthorListView, ContactUsRequestListView, CategoryListView, FAQListView, TagListView, ContactUsListView, PostDetailView,AuthorDetailView, ContactUsRequestDetailView, CategoryDetailView, FAQDetailView, TagDetailView, ContactUsDetailView

urlpatterns = [
    path('PostListView/', PostListView.as_view()),
    path('PostDetailView/<int:pk>/', PostDetailView.as_view()),
    path('AuthorListView/', AuthorListView.as_view()),
    path('AuthorDetailView/<int:pk>/', AuthorDetailView.as_view()),
    path('ContactUsRequestListView/', ContactUsRequestListView.as_view()),
    path('ContactUsRequestDetailView/<int:pk>/', ContactUsRequestDetailView.as_view()),
    path('CategoryListView/', CategoryListView.as_view()),
    path('CategoryDetailView/<int:pk>/', CategoryDetailView.as_view()),
    path('FAQListView/', FAQListView.as_view()),
    path('FAQDetailView/<int:pk>/', FAQDetailView.as_view()),
    path('TagListView/', TagListView.as_view()),
    path('TagDetailView/<int:pk>/', TagDetailView.as_view()),
    path('ContactUsListView/', ContactUsListView.as_view()),
    path('ContactUsDetailView/<int:pk>/', ContactUsDetailView.as_view())
]
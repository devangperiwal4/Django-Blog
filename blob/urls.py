from django.urls import path
from . import views
from .views import AddPostView, Homeview, ArticleDetailview, UpdatePost, DeletePost, AddCategoryView, CategoryView
urlpatterns = [
    # path('',views.home,name='home'),
    path('', Homeview.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailview.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),
    path('article/<int:pk>/edit/', UpdatePost.as_view(), name='update'),
    path('article/<int:pk>/delete/', DeletePost.as_view(), name='delete'),
    path('category/<str:cats>/', CategoryView, name='category'),
]

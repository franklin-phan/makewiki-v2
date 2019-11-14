from django.urls import path
from wiki.views import PageListView, PageDetailView
from django.conf.urls import include


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
    path('accounts/', include('django.contrib.auth.urls')),
    
]

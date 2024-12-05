# from .views import DocumentView, HomeView, SuperView
from django.urls import path

from .views import AccordionView, CardView, CarouselView, DocumentView, HtmlView, PageView, SuperView, TableView, TabsView


urlpatterns = [

    # Templates
    path('', HtmlView.as_view(template_name='home.html'), name='home'),
    path('theme.html', HtmlView.as_view(template_name='theme.html'), name='theme'),
    path('<str:page>.html', PageView.as_view()),

    # Document
    path('doc/', DocumentView.as_view(), name='document'),
    path('doc/<str:doc>', DocumentView.as_view()),

    # Cards
    path('card',  CardView.as_view(), name='card'),

    # Table
    path('table',  TableView.as_view(), name='table'),

    # Tabs and Accordion
    path('tabs',  TabsView.as_view(), name='tabs'),
    path('accordion',  AccordionView.as_view(), name='accordion'),

    # Carousel
    path('carousel',  CarouselView.as_view(), name='carousel'),

    # Super View
    path('super',  SuperView.as_view(), name='super'),

]

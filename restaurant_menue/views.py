from django.shortcuts import render
from django.views import generic
from . models import Item


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"

    def get_context_data(self):
        context = {"meal": ["Pizza", "pasta"],
                   "ingredients": ["things"]
                   }
        return context


class MenuItemDetails(generic.DetailView):
    model = Item
    template_name = "menu_item_details.html"





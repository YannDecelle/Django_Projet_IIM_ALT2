
from django import forms
from .models import ShopModel
from .models import BuyModel
 
# creating a form
class ShopAddForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = ShopModel
 
        # specify fields to be used
        fields = [
            "Product_Image",
            "Product_Name",
            "Product_Description",
            "Product_Stock",
            "Product_Price",
        ]

class BuyForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = BuyModel
 
        # specify fields to be used
        fields = [
            "User_Buy",
        ]
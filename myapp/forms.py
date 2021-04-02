from django import forms 
  
# creating a form  
class ProductForm(forms.Form): 
    name=forms.CharField(max_length=50)
    unit_price=forms.DecimalField(max_digits=6, decimal_places=2)

class CustomerForm(forms.Form):
    first_name=forms.CharField(max_length=25)
    last_name=forms.CharField(max_length=25)
    contact_no=forms.CharField(max_length=15)
    pincode=forms.IntegerField()

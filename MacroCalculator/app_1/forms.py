from django import forms

class IngredientsForm(forms.Form):
    ingredient_1 = forms.CharField(label='Ingredient 1', max_length=100,required=True)
    amount_1 = forms.CharField(label='Amount 1', max_length=100,required=True)
    ingredient_2 = forms.CharField(label='Ingredient 2', max_length=100,required=False)
    amount_2 = forms.CharField(label='Amount 2', max_length=100,required=False)
    ingredient_3 = forms.CharField(label='Ingredient 3', max_length=100,required=False)
    amount_3 = forms.CharField(label='Amount 3', max_length=100,required=False)
    ingredient_4 = forms.CharField(label='Ingredient 4', max_length=100,required=False)
    amount_4 = forms.CharField(label='Amount 4', max_length=100,required=False)
    ingredient_5 = forms.CharField(label='Ingredient 5', max_length=100,required=False)
    amount_5 = forms.CharField(label='Amount 5', max_length=100,required=False)
    ingredient_6 = forms.CharField(label='Ingredient 6', max_length=100,required=False)
    amount_6 = forms.CharField(label='Amount 6', max_length=100,required=False)
    ingredient_7 = forms.CharField(label='Ingredient 7', max_length=100,required=False)
    amount_7 = forms.CharField(label='Amount 7', max_length=100,required=False)
    ingredient_8 = forms.CharField(label='Ingredient 8', max_length=100,required=False)
    amount_8 = forms.CharField(label='Amount 8', max_length=100,required=False)
    ingredient_9 = forms.CharField(label='Ingredient 9', max_length=100,required=False)
    amount_9 = forms.CharField(label='Amount 9', max_length=100,required=False)
    ingredient_10 = forms.CharField(label='Ingredient 10', max_length=100,required=False)
    amount_10 = forms.CharField(label='Amount 10', max_length=100,required=False)
   
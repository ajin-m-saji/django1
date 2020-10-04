from django import forms

class TodoListForm(forms.Form):
    text=forms.CharField(max_length=45,
                        
                        widget=forms.TextInput(
                    attrs={'class':'form-control','Placeholder':'Enter todo eg Grocery shopping','aria-label':'Todo','aria-describedby':'add-btn'}))
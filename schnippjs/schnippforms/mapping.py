from django import forms
from schnippjs.schnippforms import schnippfields

FIELDS = {
    forms.CharField : schnippfields.text,
    forms.IntegerField: schnippfields.integer,
    forms.FloatField: schnippfields.floatingpoint,
    (forms.CharField, forms.Textarea): schnippfields.textarea,
    (forms.CharField, forms.HiddenInput): schnippfields.hiddeninput,
    (forms.ChoiceField, forms.HiddenInput): schnippfields.hiddeninput,
    forms.ModelChoiceField: schnippfields.modelchoice,
    forms.TypedChoiceField: schnippfields.dropdownselect,
    forms.DateField: schnippfields.datepicker,
    forms.BooleanField: schnippfields.checkbox,
}







   


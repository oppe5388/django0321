from django import forms


class CustomCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    template_name = 'myinfo/widgets/custom_checkbox.html'
    option_template_name = 'myinfo/widgets/custom_checkbox_option.html'

    def __init__(self, attrs=None):
        super().__init__(attrs)
        if 'class' in self.attrs:
            self.attrs['class'] += ' custom-checkbox'
        else:
            self.attrs['class'] = 'custom-checkbox'


class AccordionCheckbox(forms.CheckboxSelectMultiple):
    template_name = 'myinfo/widgets/accordion_check.html'

    class Media:
        css = {
            'all': [
                'myinfo/css/accordion.css',

            ]
        }
        js = [
            'myinfo/js/accordion.js'
        ]
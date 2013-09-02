from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit, Button, Fieldset, HTML
from django import forms

class IntroPForm(forms.Form):

    attention_getter = forms.CharField()
    transition_1 = forms.CharField()
    thesis_item1 = forms.CharField()
    thesis_item2 = forms.CharField()
    thesis_item3 = forms.CharField()
    transition_2 = forms.CharField()
    conclusion = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(IntroPForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                'Intro Paragraph',
                Field("attention_getter", css_class='form-control'),
                Field("transition_1", css_class='form-control'),
                Fieldset(
                    'Thesis',
                    Field("thesis_item1", css_class="form-control"),
                    Field("thesis_item2", css_class="form-control"),
                    Field("thesis_item3", css_class="form-control"),
                    css_class='col-md-offset-1'
                ),
                Field("transition_2", css_class="form-control"),
                Field("conclusion", css_class="form-control"),
            ),
            Div(
                FormActions(
                    Submit('save_intro', 'Submit', css_class="btn-primary"),
                    Button('cancel', 'Cancel')
                )
            )
        )


class BodyPForm(forms.Form):

    intro = forms.CharField()
    body = forms.CharField(widget=forms.Textarea())
    conclusion = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(BodyPForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                'Body Paragraph',
                Field("intro", css_class="form-control"),
                Field("body", css_class="form-control"),
                Field("conclusion", css_class="form-control"),
                ),
            Div(
                FormActions(
                    Submit('save_body', 'Submit', css_class="btn-primary"),
                    Button('cancel', 'Cancel')
                )
            )
        )


class ConclusionPForm(forms.Form):

    attention_getter = forms.CharField()
    thesis = forms.CharField()
    body = forms.CharField(widget=forms.Textarea())
    conclusion = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(ConclusionPForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Fieldset(
                'Conclusion Paragraph',
                Field("attention_getter", css_class="form-control"),
                Field("thesis", css_class="form-control"),
                Field("body", css_class="form-control"),
                Field("conclusion", css_class="form-control"),
                ),
            Div(
                FormActions(
                    Submit('save_intro', 'Submit', css_class="btn-primary"),
                    Button('cancel', 'Cancel')
                )
            )
        )

class SummaryForm(forms.Form):

    document = forms.CharField(widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super(SummaryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.form_tag = False
        #self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
                Field("document", css_class="form-control", rows=20),
            Div(
                FormActions(
                    Submit('save_intro', 'Submit', css_class="btn-primary"),
                    Button('cancel', 'Cancel')
                )
            )
        )

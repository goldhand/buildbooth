from django.shortcuts import get_object_or_404, render
from django.views import generic

from .forms import IntroPForm, BodyPForm, ConclusionPForm, SummaryForm


def nocontext_view(request):
    context = {
        'intro_form': IntroPForm(),
        'body_form': BodyPForm(),
        'conclusion_form': ConclusionPForm(),
        'summary_form': SummaryForm(),
    }
    return render(request, 'starterapp/nocontext.html', context)



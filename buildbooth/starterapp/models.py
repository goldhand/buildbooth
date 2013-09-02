from django.db import models

def nocontext_view(request):
	return render(request, 'starterapp/nocontext_view.html')


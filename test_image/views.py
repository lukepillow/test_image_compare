from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import ImageMatch
from django.forms import modelformset_factory



# Create your views here.
class IndexView(generic.ListView):
    template_name = 'test_image/index.html'
    context_object_name = 'first_match_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return ImageMatch.objects.all()[:5]

class DetailView(generic.DetailView):
    model = ImageMatch
    template_name = 'test_image/detail.html'
    def get_queryset(self):
        return ImageMatch.objects.all()


def compare_image(request):
    ImageMatchFormSet = modelformset_factory(ImageMatch, 
            fields =('id','apt_img_url','bnb_img_url','match'),extra=0)

    if request.method == 'POST':
        formset = ImageMatchFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/test_image/form/')

    else:
        formset = ImageMatchFormSet(queryset=ImageMatch.objects.filter(id__lt=110 , id__gt = 100))
    return render(request, 'test_image/test_form.html', {'formset': formset})



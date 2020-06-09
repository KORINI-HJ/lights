from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import Http404

from .models import Diary
from .forms import DiaryForm, CommentForm


# Create your views here.
num_random_contents = 4
def index(request):
    #contents = Diary.objects.order_by('?')[:num_random_contents]
    contents = Diary.objects.all()
    return render(request, 'index.html', {'diary':contents})

def detail(request, diary_id):
    # jss = get_object_or_404(Jasoseol, pk=jss_id)
    try:
        diary = Diary.objects.get(pk=diary_id)
    except:
        raise Http404
    cmt = CommentForm()
    context = {'diary' : diary, 'comments': cmt}
    return render(request, 'detail.html', context)

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object다."

class DiaryCreateView(LoginRequiredMixin, CreateView):
    model = Diary
    fields = ['title', 'body', 'images']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class DiaryUpdateView(OwnerOnlyMixin, UpdateView):
    model = Diary
    fields = ['title', 'body', 'images']
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class DiaryDeleteView(OwnerOnlyMixin, DeleteView):
    model = Diary
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

def comment_create(request, diary_id):
    if request.method == "POST":
        cmt = CommentForm(request.POST) # 댓글 폼 안에 넘어오는 request 값을 담아준다.
        if cmt.is_valid():
            upload = cmt.save(commit=False) # 잠시 저장 보류
            upload.post = Diary.objects.get(pk=diary_id) # 댓글이 갈릴 글의 id는 넘어오는 jss_id하자
            upload.save()
            return redirect('detail', diary_id)
    cmt = CommentForm()
    diary = DiaryForm()
    context = {'comments': cmt, 'diary': diary}
    return render(request, 'detail.html', context)


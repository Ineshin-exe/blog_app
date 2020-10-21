from django import forms

from blog.models import Blog


class FollowForm(forms.Form):
    follow = forms.ModelMultipleChoiceField(queryset=Blog.objects.all(),
                                            label="Blogs")

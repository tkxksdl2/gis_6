from django.http import HttpResponseForbidden


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        from profileapp.models import Profile
        target_profile = Profile.objects.get(pk=kwargs['pk'])
        if request.user == target_profile.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return decorated
from impresses.models import Profile


def get_avatar(backend, response, user=None, *args, **kwargs):
    url = None
    profile = Profile.objects.get(user__username=str(user))

    if backend.name == 'vk-oauth2':
        url = response.get('photo', '')

    if url:
        profile.avatar = url
        profile.save()
        print(profile.avatar)
        print(profile)

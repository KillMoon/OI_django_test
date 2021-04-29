from social_core.backends.facebook import FacebookOAuth2

from impresses.models import Profile


def get_avatar(backend, user=None, *args, **kwargs):
    if not kwargs['is_new']:
        return
    url = None
    profile = Profile.objects.create(user=user, avatar='')
    print(profile.user.first_name)

    if backend.name == 'vk-oauth2':
        url = kwargs['response'].get('photo', '')
    else:
        fbuid = kwargs['response']['id']
        url = 'http://graph.facebook.com/%s/picture?type=large' % fbuid

    if url:
        profile.avatar = url
        profile.save()
        print(profile.avatar)
        print(profile)
    print(Profile.objects.get(user=user).avatar)
    user.save()

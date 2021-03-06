from django.core.cache import cache
from django.utils.hashcompat import md5_constructor
from django.utils.http import urlquote

#modified from http://djangosnippets.org/snippets/1593/
def expireTemplateCache(fragment_name, *variables):
    args = md5_constructor(u':'.join([urlquote(unicode(x)) for x in variables]))
    cache_key = 'template.cache.%s.%s' % (fragment_name, args.hexdigest())
    cache.delete(cache_key)

def authStatus(user):
    if 'is_authenticated' in dir(user):
        return user.is_authenticated()
    else:
        return str(user)

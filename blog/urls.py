from django.conf.urls import url
from django.conf.urls.static import static

from mysite import settings
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/(?P<idef>[0-9]*)$', views.blog_post, name='blog_post'),
    url(r'^flat/(?P<idef>[0-9]*)$', views.flat, name='flat'),
    url(r'^flats/$', views.flats, name='flats'),
    #url(r'^flats/(?P<type>[\w-]+)&(?P<district>\w+)$', views.flat_short, name='flat_short'),

    #url(r'^flats/more/(?P<type>[\w-]+)&(?P<district>\w+)&(?P<startPrice>\w+)&(?P<endPrice>\w+)&(?P<rooms>\w+)&(?P<sqs>\w+)&(?P<sqe>\w+)&(?P<lsqs>\w+)&(?P<lsqe>\w+)&(?P<ksqs>\w+)&(?P<ksqe>\w+)&(?P<fs>\w+)&(?P<fe>\w+)&(?P<fss>\w+)&(?P<fse>\w+)&(?P<es>\w+)&(?P<ee>\w+)&(?P<house_type>\w+)&(?P<house_material>\w+)$', views.flat_buy, name='flat_buy'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

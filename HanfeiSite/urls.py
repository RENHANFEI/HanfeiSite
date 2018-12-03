from django.conf.urls import url
from django.views.generic import RedirectView

from . import view

handler404 = view.page_not_found
handler500 = view.page_error

urlpatterns = [
    # url(r'^favicon.ico$',RedirectView.as_view(url=r'static/image/favicon.ico')),
    url(r'^work$', RedirectView.as_view(url='^$')),
    url(r'^$', view.work),
    url(r'^standup$', view.standup),
    url(r'^cubicle$', view.cubicle),
    url(r'^casio$', view.casio),
    url(r'^stepbeats$', view.stepbeats),
    url(r'^kiwi$', view.kiwi),
    url(r'^projects$', view.projects),
    url(r'^about$', view.about),
    url(r'^resume$', RedirectView.as_view(url='static/Resume_HanfeiRen.pdf')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/image/favicon.ico')),
    url(r'^vcd$', view.vcd),
]

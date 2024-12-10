import os

from django.urls import re_path
from django.conf import settings
from django.views.static import serve

from .views import DjangoJasmineView

dj_jas_view = DjangoJasmineView.as_view()

urlpatterns = [
    re_path(r'^tests/(?P<path>.*)$', serve, {
        'document_root': os.path.join(settings.JASMINE_TEST_DIRECTORY, "spec"),
    }, name='jasmine_test'),
    re_path(r'^fixtures/(?P<path>.*)$', serve, {
        'document_root': os.path.join(
            settings.JASMINE_TEST_DIRECTORY, "fixtures",
        ),
    }, name='jasmine_fixtures'),
    re_path('^$', dj_jas_view, name='jasmine_default'),
    re_path('^(?P<version>.*)/$', dj_jas_view, name='jasmine_version'),
]

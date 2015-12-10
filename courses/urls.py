from django.conf.urls import patterns, url

from courses.views import detail, add, edit, remove, add_lesson, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView, Add_lessonCreateView

urlpatterns = patterns('',

                       url(r'^(?P<pk>\d+)/$', CourseDetailView.as_view(), name='detail'),
                       url(r'^add/$', CourseCreateView.as_view(), name='add'),
                       url(r'^edit/(?P<pk>\d+)/$', CourseUpdateView.as_view(), name='edit'),
                       url(r'^remove/(?P<pk>\d+)/$', CourseDeleteView.as_view(), name='remove'),
                       url(r'^(?P<pk>\d+)/add_lesson$', Add_lessonCreateView.as_view(), name='add-lesson'),



                       )

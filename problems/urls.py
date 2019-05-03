from django.urls import include, path
from rest_framework import routers
from problems import views

router = routers.DefaultRouter()
router.register(r'problem', views.ProblemViewSet)
router.register(r'submission', views.SubmissionViewSet)
router.register(r'testcase', views.TestCaseViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
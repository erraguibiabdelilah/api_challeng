from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from quickstart.views import (
    CandidateViewSet,
    RecruiterViewSet,
    RecruiterCandidateViewSet,
    SkillViewSet,
    ExperienceViewSet,
    EducationViewSet
)


router = routers.DefaultRouter()
router.register(r'candidates', CandidateViewSet, basename='candidate')
router.register(r'recruiters', RecruiterViewSet, basename='recruiter')
router.register(r'recruiter/candidates', RecruiterCandidateViewSet, basename='recruiter-candidate')
router.register(r'skills', SkillViewSet, basename='skill')
router.register(r'experiences', ExperienceViewSet, basename='experience')
router.register(r'educations', EducationViewSet, basename='education')




schema_view = get_schema_view(
   openapi.Info(
      title="Challeng API",
      default_version='v1',
      description="Documentation de l'API Challeng",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

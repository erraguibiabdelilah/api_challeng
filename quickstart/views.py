from rest_framework import viewsets
from .models import Candidate, Recruiter, Skill, Experience, Education
from .serializers import CandidateSerializer, RecruiterSerializer, SkillSerializer, ExperienceSerializer, EducationSerializer

# Endpoints pour les candidats (CRUD complet)
class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

# Endpoints pour les recruteurs (lecture seule)
class RecruiterViewSet(viewsets.ModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer

# Endpoints pour recruteur pour consulter les candidats (lecture seule)
class RecruiterCandidateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

# Endpoints CRUD pour Skills
class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

# Endpoints CRUD pour Experiences
class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

# Endpoints CRUD pour Education
class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

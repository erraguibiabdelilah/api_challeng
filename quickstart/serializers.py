from rest_framework import serializers
from .models import Candidate, Recruiter, Skill, Experience, Education


class SkillSerializer(serializers.ModelSerializer):
    candidate = serializers.PrimaryKeyRelatedField(queryset=Candidate.objects.all())

    class Meta:
        model = Skill
        fields = ['id', 'name', 'level', 'candidate']


class ExperienceSerializer(serializers.ModelSerializer):
    candidate = serializers.PrimaryKeyRelatedField(queryset=Candidate.objects.all())

    class Meta:
        model = Experience
        fields = ['id', 'title', 'company', 'start_date', 'end_date', 'candidate']


class EducationSerializer(serializers.ModelSerializer):
    candidate = serializers.PrimaryKeyRelatedField(queryset=Candidate.objects.all())

    class Meta:
        model = Education
        fields = ['id', 'school', 'degree', 'field', 'start_date', 'end_date', 'candidate']


class CandidateSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)

    class Meta:
        model = Candidate
        fields = ['id', 'name', 'email', 'phone', 'recruiter', 'skills', 'experiences', 'educations']


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = ['id', 'name', 'company']

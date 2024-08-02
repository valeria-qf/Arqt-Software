# core/views.py

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import UserSubscription, Topic
from .serializers import UserSubscriptionSerializer
from core import serializers


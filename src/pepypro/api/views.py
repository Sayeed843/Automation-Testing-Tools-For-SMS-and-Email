from rest_framework.views import APIView
from rest_framework.response import Response
from pepypro.models import UserEmail, UserMessage
from .serializers import UserEmailSerializer,UserMessageSerializer
from rest_framework import generics, mixins
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
import json

def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid=False
    return is_valid


class UserEmailAPIView(mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = UserEmailSerializer
    passed_id =None

    def get_queryset(self):
        qs = UserEmail.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None) or self.passed_id
        queryset = self.get_queryset()
        obj = None

        if passed_id is not None:
            obj = get_object_or_404(queryset, id =passed_id)
            self.check_object_permissions(request,obj)
        return obj

    def get(self, request):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body

        if is_json(body_):
            json_data= json.loads(request.body)

        new_passed_id = json_data.get('id',None)
        passed_id = url_passed_id or new_passed_id or None

        self.passed_id = passed_id
        if passed_id is not None:
            return self.retrieve(request)
        return super().get(request)


    def post(self, request):
        return self.create(request)

    def put(self,request):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body

        if is_json(body_):
            json_data= json.loads(request.body)

        new_passed_id = json_data.get('id',None)
        passed_id = url_passed_id or new_passed_id or None

        self.passed_id = passed_id
        return self.update(request)

    def patch(self,request):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body

        if is_json(body_):
            json_data= json.loads(request.body)

        new_passed_id = json_data.get('id',None)
        passed_id = url_passed_id or new_passed_id or None

        self.passed_id = passed_id
        return self.update(request)

    def delete(self,request):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body

        if is_json(body_):
            json_data= json.loads(request.body)

        new_passed_id = json_data.get('id',None)
        passed_id = url_passed_id or new_passed_id or None

        self.passed_id = passed_id
        return self.destroy(request)


class UserMessageAPIView(mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = UserMessageSerializer
    passed_id = None

    def get_queryset(self):
        qs = UserMessage.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None) or self.passed_id
        queryset = self.get_queryset()
        obj = None

        if passed_id is not None:
            obj = get_object_or_404(queryset, id =passed_id)
            self.check_object_permissions(request,obj)
        return obj

    def get(self, request):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body

        if is_json(body_):
            json_data= json.loads(request.body)

        new_passed_id = json_data.get('id',None)
        passed_id = url_passed_id or new_passed_id or None

        self.passed_id = passed_id
        if passed_id is not None:
            return self.retrieve(request)
        return super().get(request)


    def post(self, request):
        return self.create(request)

    def put(self,request):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body

        if is_json(body_):
            json_data= json.loads(request.body)

        new_passed_id = json_data.get('id',None)
        passed_id = url_passed_id or new_passed_id or None

        self.passed_id = passed_id
        return self.update(request)

    def patch(self,request):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body

        if is_json(body_):
            json_data= json.loads(request.body)

        new_passed_id = json_data.get('id',None)
        passed_id = url_passed_id or new_passed_id or None

        self.passed_id = passed_id
        return self.update(request)

    def delete(self,request):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body

        if is_json(body_):
            json_data= json.loads(request.body)

        new_passed_id = json_data.get('id',None)
        passed_id = url_passed_id or new_passed_id or None

        self.passed_id = passed_id
        return self.destroy(request)

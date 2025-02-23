from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView

from backend.response import FormattedResponse
from challenge.models import Challenge
from andromeda import client
from andromeda.serializers import JobSubmitSerializer


class GetInstanceView(APIView):
    permission_classes = (IsAuthenticated,)
    throttle_scope = "challenge_instance_get"

    def get(self, request, job_id):
        return FormattedResponse(
            client.get_instance(request.user.id, job_id)
        )


class ResetInstanceView(APIView):
    permission_classes = (IsAuthenticated,)
    throttle_scope = "challenge_instance_reset"

    def get(self, request, job_id):
        return FormattedResponse(
            client.request_reset(request.user.id, job_id)
        )


class ListJobsView(APIView):
    permission_classes = (IsAdminUser,)
    throttle_scope = "andromeda_view_jobs"

    def get(self, request):
        return FormattedResponse(
            client.list_jobs()
        )


class RestartJobView(APIView):
    permission_classes = (IsAdminUser,)
    throttle_scope = "andromeda_manage_jobs"

    def post(self, request):
        return FormattedResponse(
            client.restart_job(request.data["job_id"])
        )


class ListInstancesView(APIView):
    permission_classes = (IsAdminUser,)
    throttle_scope = "andromeda_view_jobs"

    def get(self, request):
        return FormattedResponse(
            client.list_instances()
        )


class SysinfoView(APIView):
    permission_classes = (IsAdminUser,)
    throttle_scope = "andromeda_view_sysinfo"

    def get(self, request):
        return FormattedResponse(
            client.sysinfo()
        )


class JobSubmitView(APIView):
    permission_classes = (IsAdminUser,)
    throttle_scope = "andromeda_manage_jobs"

    def post(self, request):
        serializer = JobSubmitSerializer(request.data)
        challenge = get_object_or_404(Challenge.objects, id=serializer.data['challenge_id'])
        response = client.submit_job(serializer.data['job_spec'])
        challenge.challenge_metadata['cserv_name'] = response['id']
        challenge.save()
        return FormattedResponse()


class JobSubmitRawView(APIView):
    permission_classes = (IsAdminUser,)
    throttle_scope = "andromeda_manage_jobs"

    def post(self, request):
        serializer = JobSubmitSerializer(request.data)
        response = client.submit_job(serializer.data['job_spec'])
        return FormattedResponse(response)

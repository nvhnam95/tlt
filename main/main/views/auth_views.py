from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['get'])
@permission_classes([IsAuthenticated])
def user_detail(request):
    user = request.user
    permissions = user.user_permissions.all()
    permission_list = []
    for p in permissions:
        if "can_view_" in p.codename:
            permission_list.append(p.codename)
    return JsonResponse({"permissions": permission_list,
                         "id": user.id,
                         "username": user.username,
                         "first_name": user.first_name})

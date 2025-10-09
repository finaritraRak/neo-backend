# content/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import PageContent
from .serializers import PageContentSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def page_content_list(request):
    """
    GET  /api/content/pages/  -> liste des contenus
    POST /api/content/pages/  -> créer un contenu
    """
    if request.method == 'GET':
        page       = request.GET.get('page')
        content_ty = request.GET.get('type')
        status_fil = request.GET.get('status')

        qs = PageContent.objects.all()
        if page:       qs = qs.filter(page=page)
        if content_ty: qs = qs.filter(content_type=content_ty)
        if status_fil: qs = qs.filter(status=status_fil)

        serializer = PageContentSerializer(qs, many=True)
        return Response(serializer.data)

    # POST
    serializer = PageContentSerializer(data=request.data)
    if serializer.is_valid():
        # author peut être None si pas authentifié
        serializer.save(author=request.user if request.user.is_authenticated else None)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([AllowAny])
def page_content_detail(request, pk):
    """
    GET    /api/content/pages/{pk}/ -> détail
    PUT    /api/content/pages/{pk}/ -> modif complète
    PATCH  /api/content/pages/{pk}/ -> modif partielle
    DELETE /api/content/pages/{pk}/ -> suppression
    """
    try:
        instance = PageContent.objects.get(pk=pk)
    except PageContent.DoesNotExist:
        return Response({'detail': 'Introuvable'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PageContentSerializer(instance)
        return Response(serializer.data)

    if request.method in ['PUT', 'PATCH']:
        partial = (request.method == 'PATCH')
        serializer = PageContentSerializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def index(request):
    return JsonResponse({'message': 'Content API is active'})
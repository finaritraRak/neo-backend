from django.http import JsonResponse

def index(request):
    return JsonResponse({"message": "Permissions module ready"})

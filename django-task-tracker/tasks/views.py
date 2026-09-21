from django.http import JsonResponse

def task_list(request):
    return JsonResponse({"tasks": ["Setup Jenkins", "Write Dockerfile", "Deploy Django App"]})

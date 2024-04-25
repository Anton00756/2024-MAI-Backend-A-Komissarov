import json
import uuid

from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from .models import Course, Lesson

from django.views.decorators.csrf import csrf_exempt


@require_http_methods(["GET"])
def all_courses(request):
    return JsonResponse(list(Course.objects.all().values()), safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def course(request, course_id):
    course_item = Course.objects.get(uid=course_id)
    response_data = {
        'uid': course_item.uid,
        'name': course_item.name,
        'description': course_item.description,
        'paid': course_item.paid
    }
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def search_course(request):
    query = request.GET.get('q', '')
    courses = Course.objects.filter(name__icontains=query) | Course.objects.filter(description__icontains=query)
    response_data = {
        'courses': list(courses.values())
    }
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
@require_http_methods(["POST"])
def create_course(request):
    try:
        data = json.loads(request.body)
        uid = uuid.uuid4()
        course_item = Course.objects.create(uid=uid, name=data['name'], description=data['description'],
                                            paid=data['paid'])

        response_data = {
            'uid': course_item.uid,
            'name': course_item.name,
            'description': course_item.description,
            'paid': course_item.paid
        }
        return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False}, status=201)
    except Exception as error:
        return JsonResponse({'error': str(error)}, status=400)


@require_http_methods(["GET"])
def all_lessons(request):
    return JsonResponse(list(Lesson.objects.all().values()), safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def lesson(request, lesson_id):
    lesson_item = Lesson.objects.get(uid=lesson_id)
    response_data = {
        'uid': lesson_item.uid,
        'theme': lesson_item.theme,
        'material': lesson_item.material,
        'time': lesson_item.time,
        'course_uid': lesson_item.course.uid
    }
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
@require_http_methods(["POST"])
def create_lesson(request):
    try:
        data = json.loads(request.body)
        uid = uuid.uuid4()
        lesson_item = Lesson.objects.create(uid=uid, theme=data['theme'], material=data['material'], time=data['time'],
                                            course=Course.objects.get(uid=data['course_uid']))

        response_data = {
            'uid': lesson_item.uid,
            'theme': lesson_item.theme,
            'material': lesson_item.material,
            'time': lesson_item.time,
            'course_uid': lesson_item.course.uid
        }
        return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False}, status=201)
    except Exception as error:
        return JsonResponse({'error': str(error)}, status=400)

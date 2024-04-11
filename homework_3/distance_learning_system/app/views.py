from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def all_courses(request):
    courses = [
        {
            'id': '4381462f-54f4-4f7e-af32-641bde5d1ef8',
            'name': 'Курс №1',
            'description': 'Описание курса №1'
        },
        {
            'id': '93394e62-5511-4de9-ab93-1cbab1320254',
            'name': 'Курс №2',
            'description': 'Описание курса №2'
        },
    ]
    return JsonResponse(courses, safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET", "POST"])
def course(request, course_id):
    if request.method == "GET":
        courses = {
            '4381462f-54f4-4f7e-af32-641bde5d1ef8': {
                'name': 'Курс №1',
                'description': 'Описание курса №1',
                'lessons': [
                    '4381462f-54f4-4f7e-af32-641bde5d1ef1',
                    '4381462f-54f4-4f7e-af32-641bde5d1ef2',
                    '4381462f-54f4-4f7e-af32-641bde5d1ef3',
                ]
            },
            '93394e62-5511-4de9-ab93-1cbab1320254': {
                'name': 'Курс №2',
                'description': 'Описание курса №2',
                'lessons': [
                    '93394e62-5511-4de9-ab93-1cbab1320251',
                    '93394e62-5511-4de9-ab93-1cbab1320252',
                    '93394e62-5511-4de9-ab93-1cbab1320253',
                ]
            }
        }
        if (course_id := str(course_id)) not in courses:
            return HttpResponseNotFound('Unknown course!')
        return JsonResponse(courses[course_id], safe=False, json_dumps_params={'ensure_ascii': False})
    else:
        return HttpResponseBadRequest('NOT IMPLEMENTED')


@require_http_methods(["GET", "POST"])
def lesson(request, lesson_id):
    if request.method == "GET":
        lessons = {
            '4381462f-54f4-4f7e-af32-641bde5d1ef1': 'Текст занятия №1',
            '4381462f-54f4-4f7e-af32-641bde5d1ef2': 'Текст занятия №2',
            '4381462f-54f4-4f7e-af32-641bde5d1ef3': 'Текст занятия №3',
            '93394e62-5511-4de9-ab93-1cbab1320251': 'Текст занятия №4',
            '93394e62-5511-4de9-ab93-1cbab1320252': 'Текст занятия №5',
            '93394e62-5511-4de9-ab93-1cbab1320253': 'Текст занятия №6',
        }
        if (lesson_id := str(lesson_id)) not in lessons:
            return HttpResponseNotFound('Unknown lesson!')
        return JsonResponse(lessons[lesson_id], safe=False, json_dumps_params={'ensure_ascii': False})
    else:
        return HttpResponseBadRequest('NOT IMPLEMENTED')

from django.core.exceptions import ValidationError


def handle_uploaded_file(file):
    with open("temp/image.jpg", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

# TODO Функция, которая получает лучшие по рейтингу цели


# TODO Для более быстрой работы нам нужно создать сводную таблицу, которая будет обновляться только при 
# добавлении объекта TimeRecord. Тогда нам не придется каждый раз дергать базу.
def check_goal_progress(goal_object):
    """Check all categories and """

from ugc.models.user import User
from ugc.models.group import Group
from ugc.models.queue import Queue


def get_main_text(user: User):
    return f"Главное меню\n" \
           f"Ваше имя - \"{user.display_name}\"\n" \
           f"\n" \
           f"1. Изменить имя\n" \
           f"2. Присоедениться к группе\n" \
           f"3. Создать группу"


def get_group_text(group: Group):
    queues = group.queues.all()
    s = ""
    for i in range(len(queues)):
        s += f"{i+1}) {queues[i].name}-{queues[i].date}"
    return f"Группа \"{group.name}\"\n" \
           f"\n" \
           f"Доступные очереди (введите номер чтобы перейти):\n" \
           f"{s}" \
           f"\n" \
           f"Введите:\n" \
           f"создать - Создать очередь\n" \
           f"обновить - Обновить это меню\n" \
           f"выход - Выйти из группы"


def get_queue_create_text():
    return "Введите название очереди в следующем формате:\n" \
           "\n" \
           "[название предмета]-[дата ДД.ММ.ГГГГ]\n" \
           "или\n" \
           "[название предмета][номер подгруппы]-[дата ДД.ММ.ГГГГ]\n" \
           "\n" \
           "Например:\n" \
           "исп-31.12.2021\n" \
           "ооп2-05.01.2022\n" \
           "\n" \
           "выход - Выйти"


def get_queue_text(queue: Queue):
    users = ""
    return f"Очередь {queue.name}-{queue.date}\n" \
           f"Группа  {queue.group.name}\n" \
           f"\n" \
           f"{users}\n" \
           f"\n" \
           f"записаться - Записаться в очередь" \
           f"выход - вернуться в меню группы"

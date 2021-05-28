from django.core.management.base import BaseCommand
from ugc.views import bot


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot.remove_webhook()
        bot.infinity_polling()

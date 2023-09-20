from django.core.management import BaseCommand

from tang.tests.factories import RecipeWith3HerbsFactory


class Command(BaseCommand):
    help = "테스트 탕전 데이터를 구성합니다."
    
    def handle(self, *args, **options):
        for _ in range(5):
            RecipeWith3HerbsFactory()

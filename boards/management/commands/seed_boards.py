import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models
from boards.models import Board


class Command(BaseCommand):

    help = "This command creates boards"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, help="How many boards do you want to create"
        )

    def handle(self, *args, **options):
        number = int(options.get("number"))
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        seeder.add_entity(
            Board,
            number,
            {
                "author": lambda x: random.choice(all_users),
                "postNo": lambda x: "#" + str(random.randint(0, 99999)),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Boards created!"))

from django.core.management.base import BaseCommand
from ...utils import generate_experts

class Command(BaseCommand):
    help = "generate expert data"
    def handle(self, *args, **kwargs):
        generate_experts()
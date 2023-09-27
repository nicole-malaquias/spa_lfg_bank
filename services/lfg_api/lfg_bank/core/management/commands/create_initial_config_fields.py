from core.models import ConfigurableFields, Proposal
from django.core.management.base import BaseCommand

from django.conf import settings


class Command(BaseCommand):
    help = "Create admin user if it does not exist"

    def handle(self, *args, **kwargs):

        proposal_field_names = [field.name for field in Proposal._meta.fields  if field.name != 'id' ]

        configurable_field, created = ConfigurableFields.objects.get_or_create(
            active_fields=proposal_field_names,
            defaults={"active_fields": proposal_field_names}
        )

        if created:
            self.stdout.write(self.style.SUCCESS('Successfully created a ConfigurableFields object.'))
        else:
            self.stdout.write(self.style.SUCCESS('A ConfigurableFields object with the desired configuration already exists.'))




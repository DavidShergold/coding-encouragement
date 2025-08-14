from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from coding_encouragement.models import Quote

class Command(BaseCommand):
    help = 'Load sample quotes into the database'

    def handle(self, *args, **options):
        # Get or create admin user for sample quotes
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={'email': 'admin@example.com', 'is_staff': True, 'is_superuser': True}
        )

        sample_quotes = [
            {
                'text': 'The only way to do great work is to love what you do.',
                'author': 'Steve Jobs'
            },
            {
                'text': 'Code is like humor. When you have to explain it, it\'s bad.',
                'author': 'Cory House'
            },
            {
                'text': 'First, solve the problem. Then, write the code.',
                'author': 'John Johnson'
            },
            {
                'text': 'Experience is the name everyone gives to their mistakes.',
                'author': 'Oscar Wilde'
            },
            {
                'text': 'In order to be irreplaceable, one must always be different.',
                'author': 'Coco Chanel'
            },
            {
                'text': 'Programming isn\'t about what you know; it\'s about what you can figure out.',
                'author': 'Chris Pine'
            },
            {
                'text': 'The best error message is the one that never shows up.',
                'author': 'Thomas Fuchs'
            },
            {
                'text': 'Simplicity is the ultimate sophistication.',
                'author': 'Leonardo da Vinci'
            },
            {
                'text': 'Before software can be reusable it first has to be usable.',
                'author': 'Ralph Johnson'
            },
            {
                'text': 'Make it work, make it right, make it fast.',
                'author': 'Kent Beck'
            }
        ]

        created_count = 0
        for quote_data in sample_quotes:
            quote, created = Quote.objects.get_or_create(
                text=quote_data['text'],
                defaults={
                    'author': quote_data['author'],
                    'submitted_by': admin_user,
                    'is_approved': True
                }
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} sample quotes')
        )

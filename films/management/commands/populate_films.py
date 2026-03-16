import csv
from django.core.management.base import BaseCommand
from django.utils.text import slugify # Ajout de slugify
from films.models import Film

class Command(BaseCommand):
    help = 'Populates the Film model with initial data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='Path to the file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file']
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',') 
                for row in reader:
                    title = row['French Title']
                    year = int(row['Release Year'])
                    # On génère le slug à partir du titre
                    generated_slug = slugify(title)

                    try:
                        # On inclut le slug dans la recherche et la création
                        film, created = Film.objects.get_or_create(
                            title=title,
                            release_year=year,
                            defaults={'slug': generated_slug} # Définit le slug à la création
                        )
                        
                        if created:
                            self.stdout.write(self.style.SUCCESS(f"Created: {title}"))
                        else:
                            self.stdout.write(self.style.WARNING(f"Exists: {title}"))
                            
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"Error on row {title}: {e}"))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"File not found: {file_path}"))
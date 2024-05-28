import random
from faker import Faker
from django.core.management.base import BaseCommand
from book_app.models import Publisher, Author, Book


class Command(BaseCommand):
    help = 'Generate fake data for publishers, authors, and books'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clear existing data
        Book.objects.all().delete()
        Author.objects.all().delete()
        Publisher.objects.all().delete()
        
        

        # Generate publishers
        publishers = []
        for _ in range(20):
            publisher = Publisher(
                name=fake.company(),
                address=fake.address(),
                city=fake.city(),
                state_province=fake.state(),
                country=fake.country(),
                website=fake.url()
            )
            publisher.save()
            publishers.append(publisher)

        # Generate authors
        authors = []
        for _ in range(30):
            author = Author(
                name=fake.name(),
                email=fake.email(),
                headshot=None  # You can add logic to add an image if needed
            )
            author.save()
            authors.append(author)

        # Generate books
        for _ in range(50):
            book = Book(
                title=fake.sentence(nb_words=4),
                publisher=random.choice(publishers),
                publication_date=fake.date_this_decade()
            )
            book.save()
            # Assign random authors to the book
            book.authors.set(random.sample(authors, k=random.randint(1, 3)))
            book.save()

        self.stdout.write(self.style.SUCCESS(
            'Successfully generated fake data!'))

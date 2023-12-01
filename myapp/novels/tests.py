from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse
from django.utils import timezone
from .models import Category, Chapter, Novel


class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Adventure")
        self.assertEqual(category.name, "Adventure")

    def test_category_name_max_length(self):
        # Test that the name field enforces the maximum length of 200 characters
        category = Category.objects.create(name="A" * 201)  # exceeding the limit
        self.assertLessEqual(len(category.name), 200)

    # Add more Category model tests as needed...


class ChapterModelTest(TestCase):
    def test_create_chapter(self):
        chapter = Chapter.objects.create(title="Chapter 1", content="Lorem ipsum...")
        self.assertEqual(chapter.title, "Chapter 1")
        self.assertEqual(chapter.content, "Lorem ipsum...")

    # Add more Chapter model tests as needed...


class NovelModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Fantasy")

    def test_create_novel(self):
        novel = Novel.objects.create(
            title="The Adventure Begins",
            published_date=timezone.now(),
            year=2023,
            status=True,
            category=self.category,
        )
        self.assertEqual(novel.title, "The Adventure Begins")
        self.assertEqual(novel.year, 2023)
        self.assertTrue(novel.status)
        self.assertEqual(novel.category, self.category)

    def test_novel_title_max_length(self):
        # Test that the title field enforces the maximum length of 200 characters
        novel = Novel.objects.create(title="A" * 201, published_date=timezone.now())
        self.assertLessEqual(len(novel.title), 200)


class NovelViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Fantasy")

    def test_novel_list_view(self):
        response = self.client.get(reverse("novels:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, "No novels available."
        )  # Assuming you have a message for an empty list

    def test_novel_detail_view(self):
        novel = Novel.objects.create(
            title="The Adventure Begins",
            published_date=timezone.now(),
            year=2023,
            status=True,
            category=self.category,
        )
        response = self.client.get(reverse("novels:detail", args=[novel.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, "The Adventure Begins"
        )  # Check for novel title in the response

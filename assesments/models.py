import uuid 
from datetime import date

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from users.models import ApiUser


class Assesment(models.Model):
    """Model representing an assesment"""
    
    # TODO this list can be obtained from extern library
    LANGUAGE_CHOICES = (
        ('python', 'python'),
        ('java', 'java'),
        ('c', 'c'),
        ('ruby', 'ruby'),
        ('javascript', 'javascript'),
    )

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    thanks_message = models.TextField(
        max_length=100, 
        default='<p>Thanks for complete the assesment!</p>')
    language = models.CharField(
        max_length=30,
        choices=LANGUAGE_CHOICES, 
        blank=True,
        default='python', 
        help_text='The assesment languaje',
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    @property
    def question_count(self):
        return self.question_set.count()

    class Meta:
        ordering = ['-id']


class Instance(models.Model):
    """Model representing a specific instance of an assesment """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    duration = models.IntegerField(default=60)
    score = models.IntegerField(default=0)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    finalized = models.BooleanField(default=False)
    question_index = models.IntegerField(default=0)
    progress_status = models.JSONField(null=True, blank=True)
    assesment = models.ForeignKey('Assesment', on_delete=models.CASCADE, default='')
    taker = models.ForeignKey('Taker', on_delete=models.RESTRICT, default='')

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} for "{self.assesment.title}"'

    @property
    def remaining_seconds(self):
        if not self.active or self.finalized:
            return 0
        remaining_time = self.end_date - timezone.now()
        return remaining_time.seconds

    def calculate_score(self):
        questions = self.assesment.question_set.all()
        if not questions:
            return 0
        question_count = self.assesment.question_count
        question_value = 100 / question_count
        score = 0
        progress_status = self.progress_status
        for question in questions:
            if str(question.id) in progress_status:
                selected_option_id = progress_status[str(question.id)]
                option = Option.objects.get(pk=selected_option_id)
                if not option or not option.is_correct: 
                    continue
                score += question_value
        return score

    def get_next_question_index(self):
        if self.question_index >= self.assesment.question_count:
            return self.question_index
        return self.question_index + 1

    def get_prev_question_index(self):
        if self.question_index <= 1:
            return 1
        return self.question_index - 1

    class Meta:
        ordering = ['-id']


class Question(models.Model):
    """Model representing a specific instance of an assesment question"""

    QUESTION_TYPE_CHOICES = (
        ('m', 'Multiple choice'),
        ('t', 'Text resolution'),
    )

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=50, blank=True, default='')
    question_type = models.CharField(
        max_length=1,
        choices=QUESTION_TYPE_CHOICES,
        default='m',
        help_text='Type of question',
    )
    assesment = models.ForeignKey('Assesment', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    class Meta:
        ordering = ['id']


class Option(models.Model):
    """Model representing a specific instance of an option"""

    OPTION_TYPE_CHOICES = (
        ('Selection', 'Selection'),
        ('Text', 'Text'),
        ('Code', 'Code'),
    )
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    option_type = models.CharField(
        max_length=30,
        choices=OPTION_TYPE_CHOICES,
        default='Selection',
    )
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.title} for {self.question.title}"
    
    class Meta:
        ordering = ['id']


class Taker(models.Model):
    """Model representing a specific instance of an assesment taker"""
    GENRE_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('n', 'No binary'),
    )
    COUNTRY_CHOICES = (
        ('AR', 'Argentina'),
        ('US', 'United States'),
    )
    user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE)

    age = models.IntegerField(blank=True, null=True)
    experience_years = models.IntegerField(blank=True, default=0)
    current_position = models.CharField(max_length=200, blank=True, default='')
    mobile_phone = models.CharField(max_length=50, blank=True, default='')
    profile = models.CharField(max_length=200, blank=True, default='')
    genre = models.CharField(
        max_length=1,
        choices=GENRE_CHOICES,
        blank=True,
        default='',
        help_text='Taker genre',
    )
    nationality = models.CharField(
        max_length=2,
        choices=COUNTRY_CHOICES, 
        blank=True,
        default='', 
        help_text='Taker nationality',
    )

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.user.last_name}, {self.user.first_name}, {self.user.email}'


@receiver(post_save, sender=ApiUser)
def create_taker(sender, instance, created, **kwargs):
    if created:
        Taker.objects.create(user=instance)


@receiver(post_save, sender=ApiUser)
def save_taker(sender, instance, **kwargs):
    instance.taker.save()
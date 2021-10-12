import uuid 
from datetime import date

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


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

    class Meta:
        ordering = ['-id']


class Instance(models.Model):
    """Model representing a specific instance of an assesment """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    duration = models.IntegerField(default=60)
    score = models.IntegerField(default=0)
    start_date = models.DateTimeField(null=True, blank=True, default='')
    end_date = models.DateTimeField(null=True, blank=True, default='')
    active = models.BooleanField(default=False)
    progress_status = models.JSONField(null=True, blank=True)
    assesment = models.ForeignKey('Assesment', on_delete=models.CASCADE, default='')
    taker = models.ForeignKey('Taker', on_delete=models.RESTRICT, default='')

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} for "{self.assesment.title}"'

    def calculate_score(self):
        """ Calculates the score from answered questions against assesment questions """
        pass

    def start(self):
        """ set start date, calculate end date from duration, set active flag """
        pass

    def stop(self):
        """ set end date, set active flag as false"""
        pass

    def update_progress(self):
        """ receive each question and updates progress_status """
        pass

    class Meta:
        ordering = ['-id']


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
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    experience_years = models.IntegerField(blank=True, default=0)
    current_position = models.CharField(max_length=200, blank=True, default='')
    mobile_phone = models.CharField(max_length=50, blank=True, default='')
    email = models.EmailField()
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
        default='US', 
        help_text='Taker nationality',
    )

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

    @classmethod
    def is_taker_available(self, taker):
        """ Evaluate that taker has not opened instances """
        return False
    
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
        ordering = ['-id']


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
        ordering = ['-id']

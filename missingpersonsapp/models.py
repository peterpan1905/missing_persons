from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class Missing(models.Model):
    Date_Missing = models.DateField(default=None)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    age_at_missing = models.IntegerField(default=0, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=30)
    race = models.CharField(max_length=30, blank=True)
    case_link = models.URLField(blank=True, null=True)

    def view_case_link(self):
        if self.case_link:
            return mark_safe('<a href="{0}">View Case</a>'.format(self.case_link))
        else:
            return 'Case Unavailable'

    view_case_link.allow_tags = True

    def __str__(self):
        return(self.First_Name + " " + self.Last_Name)
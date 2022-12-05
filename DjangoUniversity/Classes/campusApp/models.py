from django.db import models

from django.db import models

class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_ID = models.IntegerField(default="", blank=True, null=False)

    object = models.Manager()

    # Displays the object output values in form of a string
    def __str__(self):
        # Returns the input value of the Campus Name and State field
        # as a tuple to display in the browser instead of the default titles
        display_course = '{0.campus_name}: {0.state}'
        return display_course.format(self)

    # Removes added 's' that Django adds to the model name in browser display
    class Meta:
        verbose_name_plural = 'University Campus'

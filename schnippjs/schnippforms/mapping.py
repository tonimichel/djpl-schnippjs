from django.db import models
from . import schnippfields


# Maps django model fields to their schnipp reprsentation
MAPPING = {
    models.CharField : schnippfields.text,
    models.IntegerField: schnippfields.integer,
    models.FloatField: schnippfields.floatingpoint,
    models.TextField: schnippfields.textarea,
    models.ForeignKey: schnippfields.foreignkey,
    models.DateField: schnippfields.text,
}

from django.contrib import admin
import models


# Register your models here.
class ExtraDataInline(admin.StackedInline):
    model = models.ExtraData
    extra = 1


class IndividualAdmin(admin.ModelAdmin):
    inlines = [ExtraDataInline]

admin.site.register(models.Individual, IndividualAdmin)

admin.site.register(models.ExtraData)

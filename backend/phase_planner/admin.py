from django.contrib import admin

from .models import Project, Phase, To_Do, Reward

# Register your models here.


class To_DoInline(admin.StackedInline):
    model = To_Do


class PhaseAdmin(admin.ModelAdmin):
    inlines = [To_DoInline]


admin.site.register(To_Do)
admin.site.register(Project)
admin.site.register(Reward)
admin.site.register(Phase, PhaseAdmin)

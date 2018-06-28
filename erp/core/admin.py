from django.contrib import admin

# Register your models here.
from .models import Unidade
from .models import Marca
from .models import Local
from .models import Item
from .models import Pessoa

admin.site.register(Unidade)
admin.site.register(Marca)
admin.site.register(Local)
admin.site.register(Item)
admin.site.register(Pessoa)


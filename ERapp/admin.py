from django.contrib import admin
from .models import USER,ImageModel,TableData001,file_table_auditV1,file_table_auditV2,file_table_auditV3,file_table_auditFinal,file_table_vt
# Register your models here.

admin.site.register(TableData001)

admin.site.register(USER)
admin.site.register(ImageModel)

admin.site.register(file_table_auditV1)
admin.site.register(file_table_auditV2)
admin.site.register(file_table_auditV3)
admin.site.register(file_table_auditFinal)
admin.site.register(file_table_vt)
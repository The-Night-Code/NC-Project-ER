from django.contrib import admin
from .models import USER,ImageModel,TableData001,UpdatedXLSXFile,MyModel,kizeo_model,kizeo_model_Pieces
from .models import file_table_auditV1,file_table_auditV2,file_table_auditV3,file_table_auditFinal,file_table_vt,Activities_audit,message_box_1
# Register your models here.

admin.site.register(TableData001)

admin.site.register(USER)
admin.site.register(ImageModel)

admin.site.register(file_table_auditV1)
admin.site.register(file_table_auditV2)
admin.site.register(file_table_auditV3)
admin.site.register(file_table_auditFinal)
admin.site.register(file_table_vt)
admin.site.register(UpdatedXLSXFile)
admin.site.register(MyModel)
admin.site.register(kizeo_model)
admin.site.register(kizeo_model_Pieces)
admin.site.register(Activities_audit)
admin.site.register(message_box_1)

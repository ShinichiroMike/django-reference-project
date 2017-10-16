from django.conf.urls import url
from .views import listado_usuarios, index, mascota_view, mascota_list, mascota_edit, mascota_delete, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^nuevo$', login_required(MascotaCreate.as_view()), name='mascota_crear'),
	url(r'^editar/(?P<pk>\d+)/$', login_required(MascotaUpdate.as_view()), name='mascota_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
	url(r'^listar/', login_required(MascotaList.as_view()), name='mascota_listar'),
	url(r'^$', index, name='index'),
	url(r'^listado', listado_usuarios, name='listado'),
]
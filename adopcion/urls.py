from django.conf.urls import url
from .views import SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
	url(r'^solicitud/listar$', SolicitudList.as_view(), name='solicitud_listar'),
	url(r'^solicitud/editar/(?P<pk>\d+)$', SolicitudUpdate.as_view(), name='solicitud_editar'),
	url(r'^solicitud/eliminar/(?P<pk>\d+)$', SolicitudDelete.as_view(), name='solicitud_eliminar'),
	url(r'^solicitud/nueva$', SolicitudCreate.as_view(), name='solicitud_crear'),
]
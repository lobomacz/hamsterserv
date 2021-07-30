from rest_framework import permissions

class ReadOnlyAllowed(permissions.BasePermission):
	
	def has_permission(self, request, view):

		if request.method in permissions.SAFE_METHODS:
			
			return True

		else:

			return False



class IsOwnerOrReadOnly(permissions.BasePermission):
	"""
	Clase que dará permisos de edición o eliminación a
	propietarios de publicaciones.
	"""

	def has_object_permissions(self, request, view, obj):
		# Los permisos de lectura son permitidos para cualquier solicitud
		# que sea por los métodos seguros.

		if request.method in permissions.SAFE_METHODS:
			
			return True

		return request.user == obj.creador or request.user == obj.digitador or request.user == obj.autor

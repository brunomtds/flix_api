from rest_framework import permissions


''' Criação de permissão simplificada'''


class GenrePermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        # Permissão personalizada
        print(request.method)
        if request.method in ['GET', 'OPTIONS', 'HEAD']:  # SAFE METHODS
            return request.user.has_perm('genres.view_genre')  # 'f{request.app}nomedaapp.ação_nomedomodel'

        if request.method == 'POST':
            return request.user.has_perm('genres.add_genres')

        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('genres.change_genres')

        if request.method in 'DELETE':
            return request.user.has_perm('genres.delete_genres')

        return False

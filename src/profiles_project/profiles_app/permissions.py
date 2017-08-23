from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """
    ALLOW USERS TO EDIT THEIR OWN PROFILE
    """

    def has_object_permission(self, request, view, obj):
        """
        CHECK USER IS TRYING TO EDIT THEIR OWN PROFILE
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class PostOnStatus(permissions.BasePermission):
    """
    ALLOW USERS TO UPDATE THEIR OWN STATUS
    """

    def has_object_permission(self, request, view, obj):
        """
        CHECKS THE USER IS TRYING TO UPDATE THEIR OWN STATUS.
        """

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id

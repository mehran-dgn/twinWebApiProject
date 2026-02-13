from ..models import ActivityLog

def create_log(
    action,
    content_type,
    object_id=None,
    user=None,
    message='',
    ip_address=None
):
    ActivityLog.objects.create(
        user=user,
        action=action,
        content_type=content_type,
        object_id=object_id,
        message=message,
        ip_address=ip_address
    )

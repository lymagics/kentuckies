from time import time

from django.conf import settings

from agora_token_builder import RtcTokenBuilder


def generate_agora_token(uid: int, channel_name: str):
    """
    Generate agora token for authentication.
    """

    PRIVILEGE_EXPIRED_TIME = _calculate_privilege_expired_time()
    ROLE_PUBLISHER = 1

    return RtcTokenBuilder.buildTokenWithUid(
        settings.AGORA_APP_ID, settings.AGORA_APP_CERTIFICATE,
        channel_name, uid, ROLE_PUBLISHER, PRIVILEGE_EXPIRED_TIME
    )


def _calculate_privilege_expired_time():
    expiration_time = 3600 * 24
    current_time = time()
    return current_time + expiration_time

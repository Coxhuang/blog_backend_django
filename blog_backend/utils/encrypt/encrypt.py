import time
import hashlib
from django.conf import settings


def hash_sha1_encrypt(code):
    """
    加密函数(明文+盐+时间戳)
    :param code: 明文
    :return: 密文,时间戳
    """
    timestamp = str(time.time())
    hash = hashlib.sha1()
    hash.update((code+settings.PRIVATEKEYHASH+timestamp).encode('utf-8'))
    return hash.hexdigest(),timestamp

def hash_sha1_decrypt(timestamp,code):
    """
    解密函数
    :param times: 时间戳
    :param code: 明文
    :return:
    """
    hash = hashlib.sha1()
    hash.update((code + settings.PRIVATEKEYHASH + timestamp).encode('utf-8'))
    return hash.hexdigest()
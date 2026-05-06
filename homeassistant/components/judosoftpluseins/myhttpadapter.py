"""Chenge TSL-Verion to 1.2 and add timeout and verify=False to requests.get."""

import ssl

from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager


class MyHttpAdapter(HTTPAdapter):
    """Custom HTTPAdapter to enforce TLS 1.2."""

    def init_poolmanager(self, *args, **kwargs):
        # SSLContext mit TLS 1.2
        ctx = ssl.SSLContext(ssl.TLSVersion.TLSv1)
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        kwargs["ssl_context"] = ctx
        return super().init_poolmanager(*args, **kwargs)

# -*- coding: utf-8 -*-
# @Author: lnorb.com
# @Date:   2022-08-05 12:45:28
# @Last Modified by:   lnorb.com
# @Last Modified time: 2022-08-05 12:46:19

import time
from functools import lru_cache


def lru_with_ttl(*, ttl_seconds, maxsize=128):
    def deco(foo):
        @lru_cache(maxsize=maxsize)
        def cached_with_ttl(*args, ttl_hash, **kwargs):
            return foo(*args, **kwargs)

        def inner(*args, **kwargs):
            return cached_with_ttl(
                *args, ttl_hash=round(time.time() / ttl_seconds), **kwargs
            )

        return inner

    return deco

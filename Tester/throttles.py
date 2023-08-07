from rest_framework.throttling import *


class TenCallPerMinute(UserRateThrottle):
    scope = 'ten'
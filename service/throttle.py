from rest_framework.throttling  import UserRateThrottle

class LkRateThrottle(UserRateThrottle):
    scope = "lk"
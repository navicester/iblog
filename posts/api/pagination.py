from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

def PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit  = 3
    max_limit = 10

def PostPageNumberPagination(PageNumberPagination):
    page_size = 4
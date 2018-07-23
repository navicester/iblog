from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )

class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit  = 3
    max_limit = 10

    # limit_query_param = "limit"
    # offset_query_param  = "offset"

class PostPageNumberPagination(PageNumberPagination):
    page_size = 4

    # page_size_query_param = 'page_size'
    # max_page_size = 100    
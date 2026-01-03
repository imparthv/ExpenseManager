from rest_framework.pagination import PageNumberPagination


class ExpensePagination(PageNumberPagination):
    page_size = 2
    max_page_size = 100
    page_size_query_param = 'page_size' # Number of items per page
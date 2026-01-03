from rest_framework.pagination import PageNumberPagination

# Custom pagination class inherting from DRF pagination
class ExpensePagination(PageNumberPagination):
    page_size = 2 # Max items per page
    max_page_size = 100 # Max number of pages user can request
    page_query_param = 'page_size'
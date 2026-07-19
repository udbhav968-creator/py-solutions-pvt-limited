from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_response_data = {
            'error': True,
            'message': str(exc),
            'status_code': response.status_code,
            'details': response.data
        }
        response.data = custom_response_data
    else:
        return Response({
            'error': True,
            'message': 'An unexpected error occurred.',
            'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'details': str(exc)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response

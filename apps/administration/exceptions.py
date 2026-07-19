from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        errors = []
        if isinstance(response.data, dict):
            for key, value in response.data.items():
                if isinstance(value, list):
                    errors.append({key: value[0]})
                else:
                    errors.append({key: value})
        elif isinstance(response.data, list):
            errors = response.data

        custom_response_data = {
            'success': False,
            'error_code': response.status_code,
            'message': 'Validation or Client Error',
            'errors': errors
        }
        response.data = custom_response_data
    else:
        logger.error(f"Unhandled Exception: {exc}", exc_info=True)
        return Response({
            'success': False,
            'error_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'message': 'An unexpected server error occurred.',
            'errors': [{'detail': str(exc)}]
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response

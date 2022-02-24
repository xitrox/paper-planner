from django.utils.deprecation import MiddlewareMixin

CORS = {
    'Access-Control-Allow-Headers': '*',
    'Access-Control-Allow-Methods': '*',
    'Access-Control-Allow-Origin': '*'
}


class MyMiddle(MiddlewareMixin):
    def process_response(self, request, response):
        if request.method == 'OPTIONS':
            response['Access-Control-Allow-Methods'] = CORS['Access-Control-Allow-Methods']
        response['Access-Control-Allow-Headers'] = CORS['Access-Control-Allow-Headers']
        response['Access-Control-Allow-Origin'] = CORS['Access-Control-Allow-Origin']
        return response
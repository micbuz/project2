def simple_middleware(get_response):
    # one-time configuration and initialization

    def middleware(request):
        # code to be executed for each request before
        # the view is called; equivalent to process_request
        reg_id = request.GET.get('ref')
        print(reg_id)
        response = get_response(request)

        # code to be executed for each request/response after
        # the view is called; equivalent to process_response

        return response

    return middleware

def get_payload(request):
    return getattr(request.auth, "payload")

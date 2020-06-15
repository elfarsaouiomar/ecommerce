



def parmsToMaps(req, args):
    """
    :param req: reuqest type post, GET
    :param args: list of params
    :return: dict contain params and value
    """
    params = {}
    for param in args:
        if req.method == "POST":
            value = req.POST.get(param)
            params[param] = value

        elif req.method == "GET":
            value = req.GET.get(param)
            if value is not None:
                params[param] = value
    return params
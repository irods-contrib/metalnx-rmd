def getClass(class_path):
    """
    Gets a class programatically based on the module name and class name
    :param class_path: the class path
    :return: the class
    """
    module_path, class_name = class_path.rsplit(".", 1)

    # Importing module
    module = None
    try:
        module = __import__(module_path, fromlist=[class_name])
    except ImportError:
        pass

    # Getting class
    cls = None
    try:
        cls = getattr(module, class_name)
    except AttributeError:
        pass

    return cls
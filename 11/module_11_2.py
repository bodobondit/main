import inspect
import sys
import  pprint


def introspection_info(obj):
    info_dict = {}
    info_dict['type'] = type(obj)
    info_dict['attributes'] = [attribute for attribute in dir(obj) if not callable(getattr(obj,attribute))]
    info_dict['methods'] = [method for method in dir(obj) if callable(getattr(obj,method))]
    info_dict['module'] = inspect.getmodule(obj)

    return info_dict

pprint.pprint(introspection_info(sys))
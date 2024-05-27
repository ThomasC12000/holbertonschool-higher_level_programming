#!/usr/bin/python3
'''MODULE'''


def class_to_json(obj):
    '''
    Write a function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    '''

    json_dict = {}
    for attr in dir(obj):
        if not attr.startswith("__") and not callable(getattr(obj, attr)):
            value = getattr(obj, attr)
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[attr] = value
    return json_dict

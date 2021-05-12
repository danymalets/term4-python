import inspect
from types import FunctionType, CodeType
import re

TYPE = "__type__"
VALUE = "__value__"

CODE_FIELD_NAME = "__code__"
GLOBAL_FIELD_NAME = "__globals__"

FUNCTION_ATTRS_NAMES = [
    "__code__",
    "__name__",
    "__defaults__",
    "__closure__",
]

GLOBALS_NAMES = 'co_names'

CODE_OBJECT_ARGS = (
    'co_argcount',
    'co_posonlyargcount',
    'co_kwonlyargcount',
    'co_nlocals',
    'co_stacksize',
    'co_flags',
    'co_code',
    'co_consts',
    'co_names',
    'co_varnames',
    'co_filename',
    'co_name',
    'co_firstlineno',
    'co_lnotab',
    'co_freevars',
    'co_cellvars'
)


def serialize(obj):
    result = {}
    tp = type(obj)
    tp_name = tp.__name__
    #print(tp_name + " - " + re.search("\'([\w\W]+)\'", str(tp)).group(1))

    if isinstance(obj, (int, float, complex, bool, str)) or obj is None:
        return obj
    elif tp == dict:
        for name, o in obj.items():
            result[name] = serialize(o)
    elif tp == list or tp == tuple:
        result[TYPE] = tp_name
        result[VALUE] = []
        for o in obj:
            result[VALUE].append(serialize(o))
    elif inspect.isroutine(obj):
        result[TYPE] = tp_name
        result[VALUE] = serialize_function(obj)
    elif tp == bytes:
        result[TYPE] = tp_name
        result[VALUE] = list(obj)
    else:
        result[TYPE] = tp_name
        result[VALUE] = serialize_inst(obj)
    return result


def serialize_function(f: object):
    result = {}
    details = inspect.getmembers(f)
    for detail in details:
        if inspect.isbuiltin(detail[1]):
            continue
        if detail[0] in FUNCTION_ATTRS_NAMES:
            result[detail[0]] = serialize(detail[1])
            if detail[0] == CODE_FIELD_NAME:
                result[GLOBAL_FIELD_NAME] = {}
                glob = f.__getattribute__(GLOBAL_FIELD_NAME)
                for name in detail[1].__getattribute__(GLOBALS_NAMES):
                    if name == f.__name__:
                        result[GLOBAL_FIELD_NAME][name] = f.__name__
                        continue
                    if name in __builtins__:
                        continue
                    if name in glob:
                        if inspect.ismodule(glob[name]):
                            continue
                        result[GLOBAL_FIELD_NAME][name] = serialize(glob[name])
    return result


def serialize_inst(inst: object):
    result = {}
    attrs = inspect.getmembers(inst)
    for attr in attrs:
        if callable(attr[1]):
            continue
        result[attr[0]] = serialize(attr[1])
    return result


def deserialize(obj):
    result = {}
    tp = type(obj)

    if tp == dict:
        if VALUE in obj and TYPE in obj:
            if obj[TYPE] == "tuple":
                result = []
                for o in obj[VALUE]:
                    result.append(deserialize(o))
                return tuple(result)
            elif obj[TYPE] == "function":
                return deserialize_function(obj[VALUE])
            elif obj[TYPE] == "bytes":
                return bytes(obj[VALUE])
            return obj[VALUE]
        for name, o in obj.items():
            result[name] = deserialize(o)
    elif tp == list:
        result = []
        for o in obj:
            result.append(deserialize(o))
        return result
    elif tp == tuple:
        result = []
        for o in obj:
            result.append(deserialize(o))
        return result
    else:
        return obj
    return result


def deserialize_function(f: dict):
    code_fields = f[CODE_FIELD_NAME][VALUE]
    code_args = []
    for field in CODE_OBJECT_ARGS:
        arg = code_fields[field]
        if type(arg) == dict:
            code_args.append(deserialize(arg))
        else:
            code_args.append(arg)
    details = [CodeType(*code_args)]
    glob = {"__builtins__": __builtins__}
    for name, o in f[GLOBAL_FIELD_NAME].items():
        glob[name] = deserialize(o)
    details.append(glob)
    for attr in FUNCTION_ATTRS_NAMES:
        if attr == CODE_FIELD_NAME:
            continue
        details.append(deserialize(f[attr]))

    result_func = FunctionType(*details)
    if result_func.__name__ in result_func.__getattribute__(GLOBAL_FIELD_NAME):
        result_func.__getattribute__(GLOBAL_FIELD_NAME)[result_func.__name__] = result_func
    return result_func


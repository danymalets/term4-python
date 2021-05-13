import re
import json

FLOAT_REGEX = "-?\d+\.\d+"
INT_REGEX = "\d+"
STR_REGEX = "\"(.*)\""
DICT_REGEX = "\{([\s\S]*)\}"
LIST_REGEX = "\[([\s\S]*)\]"


def to_json(obj):
    if obj is None:
        return "null"
    elif isinstance(obj, bool):
        return str(obj).lower()
    elif isinstance(obj, (int, float)):
        return str(obj)
    elif isinstance(obj, str):
        return "\"" + obj.replace('\\', '\\\\').replace('\n', '\\n').replace('/', '\\/') + "\""
    elif isinstance(obj, list):
        return f"[{','.join(to_json(o) for o in obj)}]"
    elif isinstance(obj, dict):
        return "{" + ",".join(f"\"{key}\":{to_json(val)}" for key, val in obj.items()) + "}"
    else:
        raise ValueError(f"Wrong type {type(obj)}")


def from_json(s):
    s = s.strip("\n ")
    if s == "null":
        return None
    elif s == "false":
        return False
    elif s == "true":
        return True
    elif re.fullmatch(INT_REGEX, s):
        return int(s)
    elif re.fullmatch(FLOAT_REGEX, s):
        return float(s)
    elif re.fullmatch(DICT_REGEX, s):
        a = {}
        for ss in split(re.fullmatch(DICT_REGEX, s).group(1), ','):
            key, value = tuple(split(ss, ':'))
            a[from_json(key)] = from_json(value)
        return a
    elif re.fullmatch(LIST_REGEX, s):
        return [from_json(ss) for ss in split(re.fullmatch(LIST_REGEX, s).group(1), ',')]
    elif re.fullmatch(STR_REGEX, s):
        return re.fullmatch(STR_REGEX, s).group(1).replace('\\n', '\n').replace('\\\\', '\\').replace('\\/', '/')
    else:
        raise ValueError(f"Wrong string \"{s}\"")


def split(s, mark):
    a = []
    depth = 0
    tmp = ""
    in_str = False
    marks = 0
    for i in range(len(s)):
        if s[i] == '\"' and (i == 0 or s[i - 1] != '\"'):
            in_str = not in_str

        if not in_str:
            if s[i] == '[' or s[i] == '{':
                depth += 1
            elif s[i] == ']' or s[i] == '}':
                depth -= 1

        if s[i] == mark and depth == 0 and not in_str:
            a.append(tmp)
            tmp = ""
            marks += 1
        else:
            tmp += s[i]

    if tmp.strip("\n ") != "":
        a.append(tmp)
    return a

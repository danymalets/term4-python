import re

FLOAT_REGEX = "-?\d+\.\d+"
INT_REGEX = "\d+"
STR_REGEX = "\'(.*)\'"
KEY_VAL_REGEX = "(.*):([\s\S]*)"


def to_yaml(obj, indent=0):
    if obj is None:
        return "null"
    elif isinstance(obj, bool):
        return str(obj).lower()
    elif isinstance(obj, (int, float)):
        return str(obj)
    elif isinstance(obj, str):
        return "\'" + obj.replace('\\', '\\\\').replace('\n', '\\n') + "\'"
    elif isinstance(obj, list):
        if not obj:
            return "[]"
        else:
            res = ""
            for o in obj:
                res += f"{' ' * indent}- {to_yaml(o, indent + 2)}\n"
            return res[indent:-1]
    elif isinstance(obj, dict):
        res = ""
        if not obj:
            return "{}"
        for key, val in obj.items():
            str_val = to_yaml(val, indent + 2)
            if isinstance(val, (list, dict)) and val:
                str_val = "\n" + " " * (indent + 2) + str_val
            res += f"{' ' * indent}{to_yaml(key)}: {str_val}\n"
        return res[indent:-1]
    else:
        raise ValueError(f"Wrong type {type(obj)}")


def from_yaml(s, indent=0):
    s = s.strip("\n ")
    if s == "null":
        return None
    elif s == "[]":
        return []
    elif s == "{}":
        return {}
    elif s == "false" or s == "true":
        return s[0] == 't'
    elif re.fullmatch(INT_REGEX, s):
        return int(s)
    elif re.fullmatch(FLOAT_REGEX, s):
        return float(s)
    elif re.fullmatch(STR_REGEX, s):
        return re.fullmatch(STR_REGEX, s).group(1).replace('\\n', '\n').replace('\\\\', '\\')
    else:
        a = split(s, indent)
        is_list = False
        for i in range(len(a)):
            a[i] = a[i].strip("\n ")
            if a[i][0:2] == "- ":
                is_list = True
        if is_list:
            res = []
        else:
            res = {}
        for s in a:
            if is_list:
                res.append(from_yaml(s[2:], indent + 2))
            else:
                m = re.fullmatch(KEY_VAL_REGEX, s)
                if m is None:
                    raise ValueError(f"Wrong string \"{s}\"")
                key = m.group(1)
                val = m.group(2)
                res[from_yaml(key)] = from_yaml(val, indent + 2)
        return res


def split(s, indent):
    a = []
    tmp = ""
    for i in range(len(s)):
        if i+indent+1 < len(s) and s[i] == "\n" and s[i+1:i+indent+1] == " " * indent and s[i+indent+1] != " ":
            a.append(tmp)
            tmp = ""
        else:
            tmp += s[i]
    a.append(tmp)
    return a


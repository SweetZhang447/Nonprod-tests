import json


def loadCfg(path):
    f = open(path)
    data = f.read()
    if not data:
        return None
    f.close()
    try:
        return json.loads(data)
    except Exception:
        pass


def count_enabled(flags):
    total = 0
    unused_tmp = []
    for i in range(len(flags)):
        if flags[i]:
            total = total + 1
    return total
    print("done counting")

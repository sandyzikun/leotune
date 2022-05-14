from . import data
import random, time, re
class Constants(object):
    PATTERN_DOT = re.compile("\.")
    STR_BASE = "\x1b[%s;3%sm%s\x1b[0m"
    STR_BASE_L = STR_BASE % (1, "%s", "%s")
rs = random.Random(time.localtime().tm_sec)
def display(item: dict):
    print()
    enders = []
    for each in item["content"]:
        if isinstance(each, str):
            enders.append("\n")
            print(each)
        else:
            enders.append(each[2] if len(each) >= 3 else "\n")
            print(Constants.STR_BASE_L % (each[0], each[1]), end=enders[-1])
    print()
    if "translation" in item:
        assert len(item["content"]) == len(item["translation"])
        k = 0
        for each in item["translation"]:
            print(each, end=enders[0])
            k += 1
        print()
    print(" " * 8 + "---- %s %s" % (item["author"], Constants.STR_BASE_L % (6, item["title"])))
    if "vocal" in item:
        print(" " * 4 + "featuring: %s" % item["vocal"])
    print()
    return item
def fortune(source: str):
    source = Constants.PATTERN_DOT.split(source)
    lrclist = data.LRC_SOURCE_MAP[source[0]]
    for k in range(1, len(source)):
        if source[k] in lrclist.keys():
            lrclist = lrclist[source[k]]
    lrclist = lrclist.lyrics
    lrcitem = rs.choice(lrclist)
    return display(lrcitem)
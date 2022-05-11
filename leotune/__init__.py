__author__ = "sandyzikun"
__version__ = "0.0.2"
from . import data
import random, time
class Constants(object):
    STR_BASE = "\x1b[%s;3%sm%s\x1b[0m"
    STR_BASE_L = STR_BASE % (1, "%s", "%s")
rs = random.Random(time.localtime().tm_sec)
def lyricsfortune(lyrics:list=data.leoneed.lyrics):
    item = rs.choice(lyrics)
    assert len(item["content"]) == len(item["translation"])
    print()
    enders = []
    for each in item["content"]:
        enders.append(each[2] if len(each) >= 3 else "\n")
        print(Constants.STR_BASE_L % (each[0], each[1]), end=enders[-1])
    print()
    k = 0
    for each in item["translation"]:
        print(each, end=enders[0])
        k += 1
    print()
    print("\t---- %s \"%s\"" % (item["author"], item["title"]))
    print("\tfeaturing: %s" % item["vocal"])
    print()
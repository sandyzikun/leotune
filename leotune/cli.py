from . import lrc
import argparse
def newparser(): # TODO: Complete the helping-message of the parser.
    res = argparse.ArgumentParser()
    res.add_argument(
        "--source",
        "-s",
        help = "select the source from which the lyrics are output",
        default = "leoneed"
        )
    return res
def init():
    parser = newparser()
    parsed = parser.parse_args()
    return lrc.fortune(parsed.source)
#!/usr/bin/env python3
from __future__ import annotations

import os
import sys

# setup access to the local site-packages
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "site-packages"))

from workflow import Workflow3

def build_table():
    items = {
        0: "NUL | NULL",
        1: "SOH | Start of Header",
        2: "STX | Start of Text",
        3: "ETX | End of Text",
        4: "EOT | End of Transmission",
        5: "ENQ | Enquiry",
        6: "ACK | Acknowledge",
        7: "BEL | Bell \\a",
        8: "BS | Backspace \\b",
        9: "HT | Horizontal Tab \\t",
        10: "LF | Line Feed \\n",
        11: "VT | Vertical Tab \\v",
        12: "FF | Form Feed \\f",
        13: "CR | Carriage Return \\r",
        14: "SO | Shift Out",
        15: "SI | Shift In",
        16: "DLE | Data Link Escape",
        17: "DC1 | Device Control 1",
        18: "DC2 | Device Control 2",
        19: "DC3 | Device Control 3",
        20: "DC4 | Device Control 4",
        21: "NAK | Negative Acknowledge",
        22: "SYN | Synchronize",
        23: "ETB | End of Transmission Block",
        24: "CAN | Cancel",
        25: "EM | End of Medium",
        26: "SUB | Substitute",
        27: "ESC | Escape \\e",
        28: "FS | File Searator",
        29: "GS | Group Separator",
        30: "RS | Record Separator",
        31: "US | Unit Separator",
        32: "SPACE",
        127: "DEL",
    }

    for i in range(33, 127):
        items[i] = chr(i)

    return items

def add_item(wf, i, name):
    m = f"{i} | 0x{i:02X} | 0b{i:>08b} | {name}"
    largetext = f"{i}\n0x{i:02X}\n0b{i:>08b}\n{name}"
    wf.add_item(title=m, copytext=m, largetext=largetext, valid=True, arg=m)

def main(wf: Workflow3):
    query = None
    if len(wf.args):
        query = wf.args[0].strip()

    items = build_table()

    try:
        if query and query.lower().startswith("0x"):
            for i, name in items.items():
                if f"0x{i:02X}".lower().startswith(query.lower()):
                    add_item(wf, i, name)
        elif query and query.lower().startswith("0b"):
            for i, name in items.items():
                if f"0b{i:>08b}".lower().startswith(query.lower()):
                    add_item(wf, i, name)
        elif query and query.isdecimal():
            for i, name in items.items():
                if str(i).startswith(query):
                    add_item(wf, i, name)
        elif query:
            for i, name in items.items():
                if query.lower() in name.lower():
                    add_item(wf, i, name)
        else:
            for i, name in items.items():
                add_item(wf, i, name)

        wf.send_feedback()
    except Exception as e:
        wf.logger.exception(e)
        raise


if __name__ == "__main__":
    wf = Workflow3()
    wf.logger.info(__name__)
    wf.run(main)

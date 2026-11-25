#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic — one childhood memory, one sentence.

The entry is a single fixed sentence, written for make.fun
u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363: a
childhood memory that brings back a summer evening in a grandmother's
kitchen. This program writes that sentence to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The sentence is fixed text: the
same bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "The rice cooker clicked off in Grandma's kitchen and steam "
    "fogged the window while I sat on the cold tile floor, seven "
    "years old, waiting for the lid to lift and the smell of fresh "
    "rice to tell me dinner was ready."
)


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the sentence against the gate, then write it out."""
    if not 1 <= len(LINE) <= 280:
        return abort(f"sentence is {len(LINE)} characters, the gate allows 1-280")
    if not LINE.strip():
        return abort("sentence is only white space, the gate refuses it")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target}: {len(LINE)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())

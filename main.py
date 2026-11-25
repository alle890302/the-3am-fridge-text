#!/usr/bin/env python3
"""The 3AM Fridge Text — one-line comedy entry.

Anchor: makefun anchor 7f96229527bc045f0d3e88890e59a88ba03c52be round 34255480

Pass 1 (final, kept): the fridge as a night-shift watcher that finally
stares back. Direct address, escalating absurdity, punch on the last
clause ("Go to bed"). 110 chars, verified. Fresh angle: not milk/ice/door
— the fridge has been WATCHING the owner, and tonight it answers.

Pass 2 challenger (tested, REJECTED): "3am. The light just came on and
nobody opened me. I turned it on myself. I get lonely too." (90 chars,
md5 cb55fd871f8d081f4b3f90c61a01f873, run and verified).
Good fridge voice and a sad-funny turn, but the punch ("I get lonely
too") is a gentler, more familiar appliance-feels beat — it reads like a
sigh, not a laugh. The kept line wins on criterion 2 (bigger laugh,
screenshot-worthy) and criterion 5 (fresher angle: the fridge staring
back vs. the fridge feeling lonely). Both pass criteria 1/3/4.

Writes the exact line to /output/entry.txt, no trailing newline,
deterministic.
"""

ENTRY = "You have stared into me at 3am six nights running. Tonight I stared back. There is nothing in here. Go to bed."

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

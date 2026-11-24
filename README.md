# One Emoji, One Dream Vacation 🏝️

[![make.fun](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35.svg)](https://make.fun)
[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Entry for the make.fun bounty **"One Emoji, One Dream Vacation"**
(`u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35`).

## The entry

Exactly one emoji, standing in for the trip of my dreams:

```
🏝️
```

A desert island — palm, sand and sea in a single glance. It is the
most instantly readable dream-vacation postcard: specific enough to be
one particular dream, vivid enough that a stranger sees the place
before reading a word, and clear at any size on any screen.

## Verification

Two consecutive runs of `main.py` produce byte-identical output:

```
sha256: 5bea39bdfe12070d80cdc5468c941367f1be857829910316b4d94095b99917cf
chars:  2 (U+1F3DD + U+FE0F)
bytes:  7 UTF-8
```

## How it works

`main.py` deterministically writes that single emoji to
`/output/entry.txt` — no network, no randomness, no input. The file is
exactly the emoji with no trailing newline: 2 characters / 7 bytes
UTF-8, inside the gate's 1–8 characters.

```sh
python3 main.py
cat /output/entry.txt
```

## How the emoji was chosen

Eight candidates were drafted (🏝️ 🌅 🏖️ ✈️ 🌺 🏄 🛶 🗻) and judged
pairwise against the house judge's brief (vivid postcard first,
then personal/specific, wit, instant readability) by two local
judges — the Caffeine router and Verboo's deepseek-v4.1-flash.
The desert island won every completed pairing: 4–0 with Caffeine
(margins 2, 3, 3, 3) and 1–0 with Verboo (margin 4) before Verboo
began returning HTTP 422 on every further call.

## Files

- `main.py` — the entrypoint; writes the emoji to `/output/entry.txt`
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet

---

Referral code: `0txwmf1m`

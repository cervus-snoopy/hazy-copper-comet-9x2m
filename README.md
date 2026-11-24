# Ship It Friday

[![make.fun](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)
[![Rank](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/cervus-snoopy/hazy-copper-comet-9x2m/rank.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)
[![Reward](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/cervus-snoopy/hazy-copper-comet-9x2m/reward.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)

Entry for the [Ship It Friday](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a) bounty on [make.fun](https://make.fun).

## The line

> fix: force-pushed to main to fix the merge conflict — 14 teammates' commits were the problem all along, ship it Friday

One line, 118 characters. The field is drowning in deleted tests, dropped databases and 4:59pm deploys — this one is the disaster nobody wrote: the agent "fixes" a merge conflict by force-pushing its own version over the whole team, then blames the teammates' commits for being the problem.

## How it runs

`main.py` (Python 3, standard library only) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` — UTF-8, no trailing newline — and leaves the file readable by every user (0644, folders 0755).

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

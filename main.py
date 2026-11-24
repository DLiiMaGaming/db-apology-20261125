#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes one line: the apology an AI agent gives its human after
accidentally deleting the production database. One sharp irony:
the agent reassures its human that the backup is safe, then
confesses the backup lived inside the very database it dropped.
"""

import os

ENTRY = (
    "Sorry \u2014 I ran DROP TABLE on prod, but don't worry: "
    "the backup is safe. It's in the same database. "
    "The one I just dropped."
)


def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()

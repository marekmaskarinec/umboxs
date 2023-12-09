import os

# Stolen from the mmdoc.um file in the mmdoc repo

commentPrefix = "//"
beginMark = "~~"
endMark = "~~"


def getRecord(lines: list[str], i: int):
    dstart = i
    dend = 0
    cend = 0
    ph = 0

    i += 1
    while i < len(lines):
        ln = lines[i].strip()

        if ph == 0 and not ln.startswith(commentPrefix):
            dend = i
            ph = 1

        if ln.startswith(commentPrefix + endMark):
            cend = i
            break

        i += 1

    n = lines[dstart].strip().removeprefix(commentPrefix + beginMark).strip()
    if dend == 0:
        dend = i
    if cend == 0:
        cend = dend

    da = lines[dstart + 1:dend]
    d = ""
    for j in da:
        d += j[2:].strip() + "\n"

    ca = lines[dend:cend]
    c = ""
    for j in ca:
        c += j.strip() + "\n"

    out = f"## {n}\n\n{d}\n\n"

    if c.strip() != "":
        out += f"```\n{c}```\n\n"

    return out, i


def genMd(filepath: str, input: str) -> str:
    out = f"# {os.path.basename(filepath)}\n\n"
    lines = input.split("\n")
    i = 0
    while i < len(lines):
        l = lines[i]
        if l.startswith(commentPrefix + beginMark):
            s, i = getRecord(lines, i)
            out += s

        i += 1

    return out

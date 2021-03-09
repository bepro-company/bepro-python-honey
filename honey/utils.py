import re


def parse_list(value, is_numeric=True):
    if not value:
        return []

    if isinstance(value, str):
        value = [v.strip() for v in value.split(",")]

    if not isinstance(value, list):
        value = [value]

    value = [v for v in value if v]

    if is_numeric:
        value = [int(v) for v in value if isinstance(v, int) or v.isdigit()]

    return value


RE_NUMBER = re.compile(r"^(-?([\d]+\.)?[\d]+)(?!\.)")


def parse_text(text, is_numeric=True, delimiter="="):
    result = {}
    lines = text.splitlines()

    for line in lines:
        split_line = line.split(delimiter, maxsplit=1)
        if len(split_line) < 2:
            continue

        k, v = split_line[:2]
        v = v.strip()

        if is_numeric:
            match = RE_NUMBER.match(v)
            if match:
                s = match.group(1)
                v = float(s) if "." in s else int(s)

        result[k.strip()] = v

    return result


def convert_value(value):
    try:
        float_value = float(value)
    except ValueError:
        return value

    try:
        int_value = int(value)
    except ValueError:
        return float_value

    return int_value


RE_EMOJI = re.compile(
    "(["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "])"
)


def remove_emoji(text, repl="", strip=True):
    text = RE_EMOJI.sub(repl, text)

    if strip:
        text = text.strip()

    return text

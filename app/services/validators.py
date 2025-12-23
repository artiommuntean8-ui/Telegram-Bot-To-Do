import re

EMAIL_RE = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
TG_USERNAME_RE = re.compile(r"^@[A-Za-z0-9_]{5,}$")

def valid_contact(value: str) -> bool:
    val = value.strip()
    return bool(EMAIL_RE.match(val) or TG_USERNAME_RE.match(val))

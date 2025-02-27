regexps = {
    "email": r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.[a-zA-Z]+){1,2}$",
    "height": r"^[1-2]\.\d\d$",
    "inn": r"^\d{12}$",
    "passport": r"^\d{2} \d{2} \d{6}$",
    "occupation": r"^[a-zA-Zа-яА-Я ]+(-[a-zA-Zа-яА-Я ]+)?$",
    "latitude": r"^-?(90\.0|[1-8]?\d\.\d+)$",
    "hex_color": r"^#[a-f0-9]{6}$",
    "issn": r"^\d{4}-\d{4}$",
    "uuid": r"^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$",
    "time": r"^([0-1]\d|2[0-3])(:[0-5]\d){2}\.\d+$"
}

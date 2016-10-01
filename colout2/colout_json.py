from colout2.colout import ThemeEntry


def theme(context):
    # This theme expect a formatted JSON input, with items spread across lines.
    # See tools like "python -m json.tool" or "json_xs"
    return context, [
        ThemeEntry('[\[\]{}],*\s*\n'),
        ThemeEntry("\" (:) ", "yellow"),
        ThemeEntry("[\]}\"](,)", "yellow"),
        ThemeEntry("\"(-*[0-9]+\.*[0-9]*e*-*[0-9]*)\"", "blue"),
        ThemeEntry("\"(.*)\"", "green"),
        ThemeEntry("""["']""", "cyan")
    ]

from colout2.colout import ThemeEntry


def theme(context):
    return context, [
        # LaTeX
        ThemeEntry("This is .*TeX.*$", "white", "bold"),
        ThemeEntry("(LaTeX Warning): (.*) `(.*)' on page [0-9] (.*) on input line [0-9]+.$",
         "magenta,magenta,white,magenta", "normal,bold,normal"),
        ThemeEntry("(LaTeX Warning): (.*)", "magenta", "normal,bold"),
        ThemeEntry("(LaTeX Error): (.*)", "red", "normal,bold"),
        ThemeEntry("^(.*\.tex):([0-9]+): (.*)", "white,yellow,red", "normal,normal,bold"),
        # ThemeEntry("on (page [0-9]+)", "yellow", "normal" ),
        ThemeEntry("on input (line [0-9]+)", "yellow", "normal"),
        ThemeEntry("^! .*$", "red", "bold"),
        ThemeEntry("(.*erfull) ([^\s]+).* in [^\s]+ at (lines [0-9]+--[0-9]+)",
         "magenta,magenta,yellow", "normal"),
        ThemeEntry("\\[^\s]+\s", "white", "bold"),
        ThemeEntry("^l\.([0-9]+) (.*)", "yellow,tex"),
        ThemeEntry("^\s+(.*)", "tex"),
        ThemeEntry("(Output written on) (.*) \(([0-9]+ pages), [0-9]+ bytes\).",
         "blue,white,blue", "normal,bold,normal"),
        ThemeEntry("WARNING.*", "magenta", "normal"),
        ThemeEntry("warning.*", "magenta", "normal"),

        # BiBTeX
        ThemeEntry("^(I couldn't) (.*)", "red", "normal,bold"),
        ThemeEntry("(I found) no (.*)", "red"),
        ThemeEntry("^---(line [0-9]+) of file (.*)", "yellow,white", "normal"),
    ]

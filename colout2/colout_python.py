from colout2.colout import ThemeEntry


def theme(context):
    return context, [
        # traceback header
        ThemeEntry("^Traceback .*$", "blue"),
        # File, line, in
        ThemeEntry(
            "^\s{2}(File \")(/*.*?/)*([^/:]+)(\", line) ([0-9]+)(, in) (.*)$",
            "blue,  none,  white,blue,  yellow,blue",
            "normal,normal,bold, normal,normal,bold"
        ),
        # ThemeEntry("^\s{2}File \"(.*)\", line ([0-9]+), in (.*)$", "white,yellow,white", "normal,normal,bold" ),
        # Error name
        ThemeEntry("^([A-Za-z]*Error):*", "red", "bold"),
        ThemeEntry("^([A-Za-z]*Exception):*", "red", "bold"),
        # any quoted things
        ThemeEntry("Error.*['\"](.*)['\"]", "magenta"),
        # python code
        ThemeEntry("^\s{4}.*$", "Python", "monokai"),
    ]

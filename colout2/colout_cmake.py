from colout2.colout import ThemeEntry


def theme(context):
    # CMake theme:
    #  actions performing in cyan
    performing = "cyan"
    #  actions performed in green
    performed = "green"
    #  actions taking an unknown time
    untimed = "blue"

    # If the user do not ask for his own colormap
    if not context["user_defined_colormaps"]:
        # A palette that goes: purple, orange, white
        percs = [45, 39, 33, 27, 21, 57, 63, 62, 98, 97, 133, 132, 138, 173, 172, 208, 214, 220, 226, 228, 229, 230,
                 231, 255]
        context["colormaps"]["Scale"] = percs

    return context, [
        # Configure...
        ThemeEntry("^--.*works", performed),
        ThemeEntry("^--.*done", performed),
        ThemeEntry("^-- Found.*NO", "red"),
        ThemeEntry("^-- Found.*", performed),
        ThemeEntry("^--.*broken", "red"),
        ThemeEntry("^-- Coult NOT find.*", "red"),
        ThemeEntry("^-- Configuring incomplete, errors occurred!", "red"),
        ThemeEntry("^--.*", performing),
        # Errors
        ThemeEntry("CMake Error:", "red"),
        ThemeEntry("CMake Warning", "yellow"),
        # Scan
        ThemeEntry("^(Scanning dependencies of target)(.*)$",
         performing, "normal,bold"),
        # Link (make)
        ThemeEntry("^(Linking .* )(library|executable) (.*/)*(.+(\.[aso]+)*)$",
         untimed, "normal,normal,bold"),
        # [percent] Creating something
        ThemeEntry("^\[\s*[0-9/]+%?\]\s(.*Creating.*)$",
         performing, "normal"),
        # [percent] Built
        ThemeEntry("^\[\s*[0-9/]+%?\]\s(Built target)(\s.*)$",
         performed, "normal,bold"),
        # [percent] Building
        ThemeEntry("^\[\s*[0-9/]+%?\]\s(Building \w* object)\s+(.*)(\.dir)(.*/)([-\w]+).c.*.o$",
         performing + "," + performing + "," + performing + ",Hash," + performing, "normal,normal,normal,normal,bold"),
        # [percent] Generating
        ThemeEntry("^\[\s*[0-9/]+%?\]\s(Generating)(\s+.*)$",
         performing, "normal,bold"),
        # make errors
        ThemeEntry("make\[[0-9]+\].*", "yellow"),
        ThemeEntry("(make: \*\*\* \[.+\] )(.* [0-9]+)", "red", "normal,bold"),
        # progress percentage (make)
        ThemeEntry("^(\[\s*[0-9]+%\])", "Scale")
    ]

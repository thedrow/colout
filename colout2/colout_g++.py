# encoding: utf-8
from colout2.colout import ThemeEntry


def default_gettext(msg):
    return msg


def theme(context):
    import os
    import gettext
    import locale

    section = "blue"

    # get g++ version
    gv = os.popen("g++ -dumpversion").read().strip()

    # get the current translations of gcc
    try:
        t = gettext.translation("gcc-" + gv)
    except IOError:
        _ = default_gettext
    else:
        _ = t.gettext
    # _("msg") will return the given message, translated

    # if the locale is unicode
    enc = locale.getpreferredencoding()
    if "UTF" in enc:
        # gcc will use unicode quotes
        qo = "[‘`]"
        qc = "[’']"
    else:
        # rather than ascii ones
        qo = "['`]"
        qc = "'"

    return context, [
        # Command line
        ThemeEntry("[/\s]([cg]\+\+-*[0-9]*\.*[0-9]*)", "white", "bold"),
        ThemeEntry("\s(\-D)(\s*[^\s]+\s)", "none,green", "normal,bold"),
        ThemeEntry("\s-g\s", "green", "normal"),
        ThemeEntry("\s-O[0-4]*\s", "green", "normal"),
        ThemeEntry("\s-[Wf][^\s]*", "magenta", "normal"),
        ThemeEntry("\s(-I)(/*[^\s]+/)([^/\s]+)", "none,blue", "normal,normal,bold"),
        ThemeEntry("\s(-L)(/*[^\s]+/)([^/\s]+)", "none,cyan", "normal,normal,bold"),
        ThemeEntry("\s(-l)([^/\s]+)", "none,cyan", "normal,bold"),
        ThemeEntry("\s-[oc]", "red", "bold"),
        ThemeEntry("\s(-+std)=*([^s]+)", "red", "normal,bold"),

        # Important messages
        ThemeEntry(_("error: "), "red", "bold"),
        ThemeEntry(_("fatal error: "), "red", "bold"),
        ThemeEntry(_("warning: "), "magenta", "bold"),
        ThemeEntry(_("undefined reference to "), "red", "bold"),
        # [-Wflag]
        ThemeEntry("\[-W.*\]", "magenta"),

        # Highlight message start:
        #   path   file   ext     : line   :  col     …
        ThemeEntry("(/.*?)/([^/:]+): (In .*)" + qo,
         section,
         "normal,normal,bold"),

        ThemeEntry("(/.*?)/([^/:]+): (At .*)",
         section,
         "normal,normal,bold"),

        ThemeEntry(_("In file included from"), section),

        # Highlight locations:
        #   path   file   ext     : line   :  col     …
        ThemeEntry("(/.*?)/([^/:]+):([0-9]+):*([0-9]*)(.*)",
         "none,white,yellow,none,none",
         "normal,normal,normal,normal"),

        # source code in single quotes
        ThemeEntry(qo + r"(.*?)" + qc, "Cpp", "monokai"),

        # source code after a "note: candidate are/is:"
        ThemeEntry(_("note: ") + r"((?!.*(" + qo + "|" + qc + ")).*)$", "Cpp", "monokai"),
        # [ _("note: ")+"(candidate:)(.*)$", "green,Cpp", "normal,monokai" ),
        # after the code part, to avoid matching ANSI escape chars
        ThemeEntry(_("note: "), "green", "normal")
    ]

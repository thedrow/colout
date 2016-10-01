from colout2 import colout_configure
from colout2.colout import ThemeEntry


def theme(context):
    context, th = colout_configure.theme(context)
    th.extend([
        ThemeEntry("error: ", "red", "bold"),
        ThemeEntry("warning: ", "magenta", "bold"),
        ThemeEntry(r"^[^\s:]*:[0-9:]*", "blue", "bold"),
        ThemeEntry(r"AC_[A-Z_]+", "cyan"),
        ThemeEntry(r"ACLOCAL_[A-Z_]+", "cyan"),
        ThemeEntry(r"'.*'[\s|.]", "yellow"),
        ThemeEntry(r"\".*\"\s", "yellow")
    ])
    return context, th
# encoding: utf-8
from colout2.colout import ThemeEntry


def theme(context):
    return context, [
        ThemeEntry("^(checking .*)(yes|found|ok)$", "green", "normal,bold"),
        ThemeEntry("^(checking .*)(no|none)$", "yellow", "normal,bold"),
        ThemeEntry("^(configure:) (error:)(.*)", "red", "normal,bold"),
        ThemeEntry("^(configure:)(.*)", "magenta", "normal,bold"),
        ThemeEntry("^(checking .*)", "blue", ""),
        ThemeEntry("^(config.status:) (creating )(.*)", "cyan,blue", "normal,normal,bold"),
        ThemeEntry("^(config.status:) (executing )(.*)", "cyan,green", "normal,normal,bold"),
    ]

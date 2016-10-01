# encoding: utf-8
from colout2.colout import ThemeEntry


def theme(context):
    style = "monokai"
    return context, [
        ThemeEntry("^(.*\.java):([0-9]+):\s*(warning:.*)$", "white,yellow,magenta", "normal,normal,bold"),
        ThemeEntry("^(.*\.java):([0-9]+):(.*)$", "white,yellow,red", "normal,normal,bold"),
        ThemeEntry("^(symbol|location)\s*:\s*(.*)$", "blue,Java", "bold," + style),
        ThemeEntry("^(found)\s*:\s*(.*)", "red,Java", "bold," + style),
        ThemeEntry("^(required)\s*:\s*(.*)", "green,Java", "bold," + style),
        ThemeEntry("^\s*\^$", "cyan", "bold"),
        ThemeEntry("^\s+.*$", "Java", style),
        ThemeEntry("[0-9]+ error[s]*", "red", "bold"),
        ThemeEntry("[0-9]+ warning[s]*", "magenta", "bold"),
    ]

import logging
import os

import sys

from pygments.formatters.terminal import TerminalFormatter
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers import get_lexer_by_name

from colout2.colout import (UnknownColor, _args_parse, load_resources, load_palettes, load_themes, DuplicatedPalette,
                           write_all, set_special_colormaps, colortheme, colorup)


def main():
    from colout2.colout import context, debug, highlight
    global debug
    error_codes = {"UnknownColor": 1, "DuplicatedPalette": 2}

    usage = "A regular expression based formatter that color up an arbitrary text stream."

    #####################
    # Arguments parsing #
    #####################
    pattern, color, style, on_groups, as_colormap, as_theme, as_source, as_all, myscale, \
    debug, resources, palettes_dirs, themes_dirs, default_colormap \
        = _args_parse(sys.argv, usage)

    if debug:
        lvl = logging.DEBUG
    else:
        lvl = logging.ERROR

    logging.basicConfig(format='[colout2] %(levelname)s: %(message)s', level=lvl)

    ##################
    # Load resources #
    ##################
    try:
        # Search for available resources files (themes, palettes)
        # in the same dir as the colout2.py script
        res_dir = os.path.dirname(os.path.realpath(__file__))

        # this must be called before args parsing, because the help can list available resources
        load_resources(res_dir, res_dir)

        # try additional directories if asked
        if palettes_dirs:
            for adir in palettes_dirs:
                try:
                    os.chdir(adir)
                except OSError as e:
                    logging.warning("cannot read palettes directory %s, ignore it" % adir)
                    continue
                else:
                    load_palettes(adir)

        if themes_dirs:
            for adir in themes_dirs:
                try:
                    os.chdir(adir)
                except OSError as e:
                    logging.warning("cannot read themes directory %s, ignore it" % adir)
                    continue
                else:
                    load_themes(adir)

    except DuplicatedPalette as e:
        logging.error("duplicated palette file name: %s" % e)
        sys.exit(error_codes["DuplicatedPalette"])

    if resources:
        asked = [r.lower() for r in pattern.split(",")]

        def join_sort(l):
            """
            Sort the given list in lexicographical order,
            with upper-cases first, then lower cases
            join the list with a comma.

            >>> join_sort(["a","B","A","b"])
            'A, a, B, b'
            """
            return ", ".join(sorted(l, key=lambda s: s.lower() + s))

        # print("Available resources:")
        for res in asked:
            if "style" in res or "all" in res:
                print("STYLES: %s" % join_sort(context["styles"]))

            if "color" in res or "all" in res:
                print("COLORS: %s" % join_sort(context["colors"]))

            if "special" in res or "all" in res:
                print("SPECIAL: %s" % join_sort(["random", "Random", "scale", "Scale", "hash", "Hash", "colormap"]))

            if "theme" in res or "all" in res:
                if len(context["themes"]) > 0:
                    print("THEMES: %s" % join_sort(context["themes"].keys()))
                else:
                    print("NO THEME")

            if "colormap" in res or "all" in res:
                if len(context["colormaps"]) > 0:
                    print("COLORMAPS: %s" % join_sort(context["colormaps"]))
                else:
                    print("NO COLORMAPS")

            if "lexer" in res or "all" in res:
                if len(context["lexers"]) > 0:
                    print("SYNTAX COLORING: %s" % join_sort(context["lexers"]))
                else:
                    print("NO SYNTAX COLORING (check that python3-pygments is installed)")

        sys.exit(0)  # not an error, we asked for help

    ############
    # Coloring #
    ############

    try:
        if myscale:
            context["scale"] = tuple([float(i) for i in myscale.split(",")])
            logging.debug("user-defined scale: %f,%f" % context["scale"])

        # Default color maps
        if default_colormap:
            if default_colormap not in context["colormaps"]:
                cmap = default_colormap.split(",")

            elif default_colormap in context["colormaps"]:
                cmap = context["colormaps"][default_colormap]

            set_special_colormaps(cmap)

        # explicit color map
        if as_colormap is True and color not in context["colormaps"]:
            context["colormaps"]["Default"] = color.split(",")  # replace the colormap by the given colors
            context["colormaps"]["default"] = color.split(",")  # replace the colormap by the given colors
            color = "colormap"  # use the keyword to switch to colormap instead of list of colors
            logging.debug("used-defined default colormap: %s" % ",".join(context["colormaps"]["Default"]))

        # if theme
        if as_theme:
            logging.debug("asked for theme: %s" % pattern)
            assert (pattern in context["themes"].keys())
            context, theme = context["themes"][pattern].theme(context)
            write_all(as_all, sys.stdin, sys.stdout, colortheme, theme)

        # if pygments
        elif as_source:
            logging.debug("asked for lexer: %s" % pattern.lower())
            assert (pattern.lower() in context["lexers"])
            lexer = get_lexer_by_name(pattern.lower())
            # Python => 256 colors, python => 8 colors
            ask_256 = pattern[0].isupper()
            if ask_256:
                logging.debug("256 colors mode")
                try:
                    formatter = Terminal256Formatter(style=color)
                except:  # style not found
                    logging.warning("style %s not found, fallback to default style" % color)
                    formatter = Terminal256Formatter()
            else:
                logging.debug("8 colors mode")
                formatter = TerminalFormatter()

            write_all(as_all, sys.stdin, sys.stdout, highlight, lexer, formatter)

        # if color
        else:
            write_all(as_all, sys.stdin, sys.stdout, colorup, pattern, color, style, on_groups)

    except UnknownColor as e:
        if debug:
            import traceback
            for var in context:
                print(var, context[var])
            print(traceback.format_exc())
        logging.error("unknown color: %s (maybe you forgot to install python3-pygments?)" % e)
        sys.exit(error_codes["UnknownColor"])

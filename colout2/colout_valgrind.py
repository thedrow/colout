# encoding: utf-8
from colout2.colout import ThemeEntry


def theme(context):
    return context, [
        # section title
        ThemeEntry("^(==[0-9]+==\s{1})(Memcheck|Copyright|Using)(.*)$", "blue", ""),
        ThemeEntry("^(==[0-9]+==\s{1})(Warning)(.*)$", "magenta", ""),
        ThemeEntry("^(==[0-9]+==\s{1}Command: )(\S*)(.*)$", "green,white", "normal,bold,normal"),
        ThemeEntry("^(==[0-9]+==\s{1})(HEAP SUMMARY:)(.*)$", "green", ""),
        ThemeEntry("^(==[0-9]+==\s{1})(All heap blocks were freed)(.*)$", "green", ""),
        ThemeEntry("^(==[0-9]+==\s{1})(.*[rR]erun.*)$", "blue", ""),
        ThemeEntry("^(==[0-9]+==\s{1})(Use --.*)$", "blue", ""),
        ThemeEntry("^(==[0-9]+==\s{1}\S+.*)$", "red", ""),
        # section explanation
        ThemeEntry("^==[0-9]+==\s{2}(\S+.*)$", "orange", ""),
        # locations adresses
        ThemeEntry("^==[0-9]+==\s{4}([atby]{2}) (0x0): (\?{3})",
         "blue,yellow,red", "normal,normal,bold"),
        ThemeEntry("^==[0-9]+==\s{4}([atby]{2}) (0x)([^:]*:) (\S+)",
         "blue,blue,blue,none", "normal"),
        # locations: library
        ThemeEntry("\(in (.*)\)", "cyan", "normal"),
        # locations: file
        ThemeEntry("\(([^\.]*\.[^:]+):([0-9]+)\)", "white,yellow", "bold,normal"),
        # leak summary
        ThemeEntry("^==[0-9]+==\s{4}(definitely lost): .* (in) .*", "red", "bold"),
        ThemeEntry("^==[0-9]+==\s{4}(indirectly lost): .* (in) .*", "orange", "bold"),
        ThemeEntry("^==[0-9]+==\s{6}(possibly lost): .* (in) .*", "yellow", "bold"),
        ThemeEntry("^==[0-9]+==\s{4}(still reachable): .* (in) .*", "green", "bold"),
        ThemeEntry("^==[0-9]+==\s{9}(suppressed): .* (in) .*", "cyan", "bold"),
    ]

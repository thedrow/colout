from colout2.colout import ThemeEntry


def theme(context):
    p = "([rwxs-])"
    reg = "^([d-])" + p * 9 + "\s.*$"
    colors = "blue" + ",green" * 3 + ",yellow" * 3 + ",red" * 3
    styles = "normal" + ",normal,italic,bold" * 3
    return context, [ThemeEntry(reg, colors, styles)]

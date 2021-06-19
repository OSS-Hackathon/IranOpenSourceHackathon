NEWLINE = '\n'


def comma_separated(list):
    return ', '.join(list)


def md_link(title, link):
    return f'[{title}]({link})'


def md_table(meta, data):
    WALL = ' | '
    FLOOR = '---'

    columns = meta.keys()
    header = WALL + WALL.join(columns) + WALL
    separator = WALL + WALL.join(FLOOR for _ in columns) + WALL + NEWLINE

    rows = NEWLINE.join(
        WALL + WALL.join(meta[col](entry) for col in columns) + WALL for entry in data
    )

    return header + NEWLINE + separator + rows

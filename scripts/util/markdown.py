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
    separator = WALL + WALL.join(map(lambda _: FLOOR, columns)) + WALL + NEWLINE

    rows = map(
        lambda entry: WALL + WALL.join(
            map(
                lambda col: meta[col](entry)
                , columns
            )
        ) + WALL
        , data
    )

    return header + NEWLINE + separator + NEWLINE.join(rows)

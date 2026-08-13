"""Helpers to emit bilingual HTML fragments."""


def t(da: str, en: str) -> str:
    return f'<span lang="da">{da}</span><span lang="en">{en}</span>'


def h2(anchor: str, da: str, en: str) -> str:
    return f'<h2 id="{anchor}">{t(da, en)}</h2>'


def h3(da: str, en: str) -> str:
    return f"<h3>{t(da, en)}</h3>"


def h4(da: str, en: str) -> str:
    return f"<h4>{t(da, en)}</h4>"


def p(da: str, en: str) -> str:
    return f"<p>{t(da, en)}</p>"


def quote(da: str, en: str) -> str:
    return f"<blockquote><p>{t(da, en)}</p></blockquote>"


def li_items(items: list[tuple[str, str]], ordered: bool = False) -> str:
    tag = "ol" if ordered else "ul"
    inner = "".join(f"<li>{t(da, en)}</li>" for da, en in items)
    return f"<{tag}>{inner}</{tag}>"


def nested_ul(items: list) -> str:
    """items: (da, en) or (da, en, children) where children is list of (da, en) or nested."""

    def render_item(item) -> str:
        if len(item) == 3:
            da, en, children = item
            return f"<li>{t(da, en)}{nested_ul(children)}</li>"
        da, en = item
        return f"<li>{t(da, en)}</li>"

    return "<ul>" + "".join(render_item(i) for i in items) + "</ul>"


def img(src: str, da: str = "", en: str = "") -> str:
    alt = t(da, en) if da or en else ""
    cap = f"<figcaption>{t(da, en)}</figcaption>" if da or en else ""
    return f'<figure class="figure"><img src="{src}" alt="" loading="lazy">{cap}</figure>'


def iframe(src: str, da: str, en: str) -> str:
    return (
        f'<div class="embed"><iframe src="{src}" title="{da}" '
        f'loading="lazy" allowfullscreen></iframe></div>'
    )


def table(headers: list[tuple[str, str]], rows: list[list[tuple[str, str]]]) -> str:
    head = "<tr>" + "".join(f"<th>{t(da, en)}</th>" for da, en in headers) + "</tr>"
    body = ""
    for row in rows:
        body += "<tr>" + "".join(f"<td>{t(da, en)}</td>" for da, en in row) + "</tr>"
    return f'<div class="table-wrap"><table>{head}{body}</table></div>'


def box(kind: str, label_da: str, label_en: str, inner: str) -> str:
    return (
        f'<div class="box {kind}"><div class="label">{t(label_da, label_en)}</div>'
        f"{inner}</div>"
    )

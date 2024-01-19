from dataclasses import dataclass


@dataclass
class HTMLTree:
    tag: str
    children: list
    text: str = ""


class ParseError(Exception):
    pass


@dataclass
class TagToken:
    tag: str


@dataclass
class TextToken:
    text: str


@dataclass
class CloseTagToken:
    tag: str


def lex(s):
    in_tag = False
    in_close_tag = False
    text = ""
    toks = []
    s = s.strip()
    for i in range(len(s)):
        c = s[i]
        if c == "<" and not (in_tag or in_close_tag):
            if s[i + 1] == "/":
                in_close_tag = True
            else:
                in_tag = True
            if text.strip():
                toks.append(TextToken(text))
            text = ""
        elif c == ">":
            if in_tag:
                toks.append(TagToken(text))
                text = ""
                in_tag = False
            elif in_close_tag:
                toks.append(CloseTagToken(text))
                text = ""
                in_close_tag = False
            else:
                text += c
        else:
            text += c
    if in_tag or in_close_tag:
        raise ParseError()
    if text.strip():
        toks.append(TextToken(text))
    return toks


def parse_tag(toks, index):
    tag = toks[index].tag
    index = index + 1
    children = []
    while True:
        if toks[index] == CloseTagToken("/" + tag):
            return (HTMLTree(tag, children), index + 1)
        child, index = parse_at_index(toks, index)
        children.append(child)


def parse_at_index(toks, index):
    if isinstance(toks[index], TagToken):
        return parse_tag(toks, index)
    elif isinstance(toks[index], TextToken):
        return (HTMLTree("text", [], toks[index].text), index + 1)
    else:
        raise ParseError()


def parse(s):
    toks = lex(s)
    return parse_at_index(toks, 0)[0]


def print_html(tag):
    if tag.tag == "text":
        print(tag.text, end="")
    else:
        print("<{}>".format(tag.tag), end="")
        for c in tag.children:
            print_html(c)
        print("</{}>".format(tag.tag), end="")

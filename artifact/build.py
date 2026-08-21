#!/usr/bin/env python3
"""Build command-center.html from page-template.html.

The page must be able to rebuild itself: publish() needs a COMPLETE document,
while the Artifact tool takes a fragment it wraps. So we embed the FULL
document template inside the fragment, and the runtime fills the same two
placeholders the build fills here.
"""
import json, sys

T_STATE, T_TEMPLATE = "__CC_STATE__", "__CC_TEMPLATE__"

def j(v):
    """Escape angle brackets so the value survives inside a script element.
    Must stay identical to the page's j()."""
    return (json.dumps(v, separators=(",", ":"))
            .replace("<", "\\u003c").replace(">", "\\u003e")
            .replace("\u2028", "\\u2028").replace("\u2029", "\\u2029"))

def wrap(fragment):
    return ('<!doctype html>\n<html>\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
            '</head>\n<body>\n' + fragment + '\n</body>\n</html>')

def render(fragment_template, state):
    full = wrap(fragment_template)
    for name, tpl in (("fragment", fragment_template), ("full", full)):
        for tok in (T_STATE, T_TEMPLATE):
            if tpl.count(tok) != 1:
                sys.exit(f"FATAL: {tok} appears {tpl.count(tok)}x in {name} template; must be exactly 1")
    return (fragment_template
            .replace(T_STATE, j(state), 1)
            .replace(T_TEMPLATE, j(full), 1))

if __name__ == "__main__":
    tpl = open("page-template.html", encoding="utf-8").read()
    state = {"v": 1, "updated": None, "proposals": {}, "tasks": {}, "notes": {}}
    out = render(tpl, state)
    open("command-center.html", "w", encoding="utf-8").write(out)
    print(f"built command-center.html  {len(out):,} bytes  (template {len(tpl):,})")

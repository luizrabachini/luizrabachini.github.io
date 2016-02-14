# -*- coding: utf-8 -*-

from staticjinja import make_site


if __name__ == "__main__":
    site = make_site(
        extensions=['jinja2.ext.with_'],
        rules=[('^base/', lambda *args, **kwargs: None)])
    site.render()

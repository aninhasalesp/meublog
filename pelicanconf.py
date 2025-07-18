AUTHOR = "Ana Paula Sales"
SITENAME = "@aninhasalesp | Blog"
SITEURL = ""

# Path to the content directory
PATH = "content"
PAGE_PATHS = ["pages"]
STATIC_PATHS = ["blog", "pages", "images", "extra/custom.css"]
EXTRA_PATH_METADATA = {
    "extra/custom.css": {"path": "static/custom.css"},
}

CUSTOM_CSS = "static/custom.css"

TIMEZONE = "America/Sao_Paulo"
DEFAULT_LANG = "pt"

THEME = "pelican-themes/notmyidea-cms"


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
)


DEFAULT_PAGINATION = 10
TYPOGRIFY = True
ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

# Social widget
SOCIAL = (
    ("linkedin", "https://www.linkedin.com/in/aninhasalesp/"),
    ("github", "https://github.com/aninhasalesp"),
)

FOOTER_INCLUDE = "Feito com ❤️ e Pelican"

DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

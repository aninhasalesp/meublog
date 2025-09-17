AUTHOR = "Ana Paula Sales"
SITENAME = "@aninhasalesp"
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
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Tags e categorias
TAG_SAVE_AS = "tag/{slug}.html"
TAG_URL = "tag/{slug}.html"
CATEGORY_SAVE_AS = "category/{slug}.html"
CATEGORY_URL = "category/{slug}.html"

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_TAGS_ON_MENU = True

# Opcional: gerar RSS também
FEED_ALL_RSS = "feeds/all.rss.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"

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

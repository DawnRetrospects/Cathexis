import os

Debug = True

def parent_dir(path):
    return os.path.abspath(os.path.join(path, os.pardir))

REPO_NAME = "Cathexis"
APP_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = parent_dir(APP_DIR)

FREEZER_DESTINATION = PROJECT_ROOT # os.path.join(PROJECT_ROOT, 'code/pages')
FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME)
FREEZER_REMOVE_EXTRA_FILES = False

FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
FLATPAGES_EXTENSION = '.md'
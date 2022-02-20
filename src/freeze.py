from flask_frozen import Freezer
from app import app

freezer = Freezer(app)


FREEZER_IGNORE_MIMETYPE_WARNINGS = True
FREEZER_REMOVE_EXTRA_FILES = False

freezer = Freezer(app, with_static_files=True,
                  log_url_for=False, with_no_argument_rules=False)


@freezer.register_generator
def url_generator():
    yield '/'
    yield '/music'
    yield '/resume'


if __name__ == '__main__':
    freezer.freeze()

# because i did dumb things
# https://code.luasoftware.com/tutorials/flask/generate-static-html-with-flask-frozen/

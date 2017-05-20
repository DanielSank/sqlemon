import os


__version__ = "0.5.0"
__project_name__ = "sqlemon"


def production_mode():
    """Return True if running in production mode."""
    if (os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')):
        mode=True
    else:
        mode=False
    return mode


class IPythonPrettyPrintable(object):
    """Mixin for sqlalchemy models to make IPython printing nice."""
    def _repr_pretty_(self, p, cycle):
        p.text(str(self) if not cycle else "...")


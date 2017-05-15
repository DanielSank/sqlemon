__version__ = "0.4.1"
__project_name__ = "sqlemon"


def production_mode():
    """Return True if running in production mode."""
    if (os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')):
        mode=True
    else:
        mode=False
    return mode


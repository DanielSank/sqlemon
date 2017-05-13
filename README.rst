*******
SQLemon
*******

Suppose you're working on a project that uses Google App Engine, Google Cloud SQL, and sqlalchemy.
In the course of testing, deploying etc., we want to connect to a couple of databases in different ways:

* App Engine project talking to production db

* Local tools (like mysql client or alembic) talking to production db

* Tests talking to local db

* Local tools talking to local db

Getting all the connections strings etc. right is kind annoying.
This package helps solve that problem.

We assume you have your project's source on your system at ``PROJECT_ROOT/``, where
``PROJECT_ROOT`` is probably something like ``~/src/<project_name>``.
The file layout should look something like this:

.. code-block::

    ├── <project_name>/
    │   ├── __init__.py
    │   ├── config.yaml
    │   ├── alembic.ini
    │   ├── lib
    │   ├── models.py
    │   └── main.py
    ├── README.md
    ├── appengine_config.py
    └── app.yaml

This package assumes there are three particular files to be available in your system:

- ``~/.<project name>/config.yaml``
  ::

      ---
      cloud:
          USER: "root"
          PASSWORD: ...
      local:
          USER: "root"
          PASSWORD: ...
          HOST: "localhost"
          PORT: 3306

- ``~/.<project name>/auth-token.json``: This is your proxy's user account auth token.

- ``PROJECT_ROOT/<project name>/config.yaml``
  ::

      ---
      INSTANCE_CONNECTION_NAME: ...

Installing this package (into a virtualenv!) provides the command line script ``start_cloud_proxy``, which starts the Google Cloud SQL proxy for you.
In order for this script (and basically everything else in this package) to work, you must first set the ``SQL_PROJECT_NAME`` environment variable with value ``<project_name>`` (see above file layout).

Release
*******
::

    $ python setup.py register -r pypi(test)
    $ python setup.py sdist upload -r pypi(test)


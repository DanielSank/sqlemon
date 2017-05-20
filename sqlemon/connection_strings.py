MYSQL_CLIENT_CLOUD = "mysql --user={} --password={} -S /tmp/cloudsql/{}"
# MySQL client through proxy to cloud
# user, password, instance connection name

MYSQL_CLIENT_LOCAL = "mysql --user={} --password={} --host={} --port={}"
# MySQL client local
# user, password, host, port

APP_ENGINE_CLOUD = "mysql+mysqldb://{}:{}@/{}?unix_socket=/cloudsql/{}"
# App Engine to Cloud
# user, password, database, instance connection name

LOCAL_TOOLS_CLOUD = "mysql+pymysql://{}:{}@/{}?unix_socket=/tmp/cloudsql/{}"
# e.g. Alembic to Cloud
# user, password, project, instance connection name

LOCAL_TOOLS_LOCAL = "mysql+pymysql://{}:{}@{}:{}/{}"
# e.g. Alembic to Cloud
# user, password, host, port, database

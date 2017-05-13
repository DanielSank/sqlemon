from distutils.core import setup
import dtssqltools

version = dtssqltools.__version__
project_name = dtssqltools.__project_name__


setup(name=project_name,
      packages=[project_name],
      version=version,
      description="Manage sqlalchemy connections to local test and prod db's",
      author='Daniel Sank',
      license='MIT',
      author_email='sank.daniel@gmail.com',
      url='https://github.com/DanielSank/{}'.format(project_name),
      download_url='https://github.com/DanielSank/{}/tarball/{}'.format(
          project_name,
          version),
      keywords=['sql'],
      classifiers=[],
)


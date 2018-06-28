from setuptools import setup

setup(name='ghTools',
      version='0.1',
      description='tools for greenhouse project',
      long_description='Tools for TFG. Add sensors to greenhouse and monitoring that.',
      url='https://github.com/kave06/tfg.git',
      author='Kave Heidarieh',
      author_email='kave.heidarieh@gmail.com',
      license='MIT',
      packages=['ghTools'],
      install_requires=[
          'pymysql',
      ],
      include_package_data=True,
      zip_safe=False)
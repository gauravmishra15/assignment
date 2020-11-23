from setuptools import setup, find_packages

requirements = []
with open('./requirements.txt', 'r') as fh:
    for line in fh:
        requirements.append(line.strip())

setup(name='p1',
      version='0.1',
      description='The P1 package',
      url='https://github.com/gauravmishra15/assignment/p1',
      author='Gaurav Mishra',
      license='MIT',
      packages=find_packages(),
      install_requires=requirements
      entry_points={
          'console_scripts': [
              'pkg1script = pkg1.__main__:main'
          ]}
)
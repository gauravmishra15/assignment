from setuptools import setup, find_packages

setup(name="pkg1",
      packages=find_packages(),
      install_requires=["pkg2"],
      entry_points={
          'console_scripts': [
              'pkg1script = pkg1.__main__:main'
          ]}
)

setup(name='p1',
      version='0.1',
      description='The P1 package',
      url='hhttps://github.com/gauravmishra15/assignment/p1',
      author='Gaurav Mishra',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'requests',
      ],
      entry_points={
          'console_scripts': [
              'pkg1script = pkg1.__main__:main'
          ]}
)
from setuptools import setup, find_packages

setup(name='p3',
      version='0.1',
      description='The P3 package',
      url='https://github.com/gauravmishra15/assignment/p3',
      author='Gaurav Mishra',
      license='MIT',
      packages=find_packages(),
      classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
        ],
      python_requires='>=3'
      install_requires=[
          'p2',
      ],
      dependency_links=['https://github.com/gauravmishra15/assignment/p2/master#egg=package-1.0'],
      zip_safe=False,
      entry_points={
           'console_scripts': [
            'pkg3script = pkg3.__main__:main'
      ]}
)
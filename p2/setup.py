from setuptools import setup, find_packages

setup(name='p2',
      version='0.1',
      description='The P2 package',
      url='hhttps://github.com/gauravmishra15/assignment/p2',
      author='Gaurav Mishra',
      license='MIT',
      packages=find_packages(),
      classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
      ],
      python_requires='>=3'
      install_requires=[
          'boto3',
          'p1',
      ],
      dependency_links=['https://github.com/gauravmishra15/assignment/p1/master#egg=package-1.0'],
      include_package_data=True,
      zip_safe=False,
      entry_points={
          'console_scripts': [
          'pkg2script = pkg2.__main__:main'
      ]}
)
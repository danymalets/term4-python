from setuptools import setup, find_packages

setup(
    name='serializer',
    packages=[
        'serializer_lib/',
        'serializer_lib/factory/',
        'serializer_lib/parsers/',
        'serializer_lib/serialization/',
        'serializer_lib/serializers/',
    ],
    version='0.0.1',
    description='Custom serializer',
    author='dany',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    scripts=['bin/serializer']
)
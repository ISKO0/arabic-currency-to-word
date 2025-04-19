from setuptools import setup, find_packages

setup(
    name='arabic-currency-to-word',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[],
    author='Karout',
    author_email='you@example.com',
    description='Convert numbers and currency values into Arabic words with linguistic correctness.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ISKO0/arabic-currency-to-word',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Natural Language :: Arabic',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

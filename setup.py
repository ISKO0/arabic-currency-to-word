from setuptools import setup, find_packages

setup(
    name='arabic-currency-to-word',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Your Name',
    author_email='your.email@example.com',
    description='Convert numbers and currency amounts into accurate Arabic words with full linguistic support.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/arabic-currency-to-word',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Arabic',
    ],
    python_requires='>=3.6',
)

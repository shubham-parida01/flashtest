from setuptools import setup, find_packages

setup(
    name='flashtest',
    version='0.1.0',
    description='A CLI-based penetration testing tool with reconnaissance and AI-driven exploits.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/flashtest',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'requests',
        'subprocess',  # Used for running external commands (such as dig)
        'whois',       # For WHOIS lookups
    ],
    entry_points={
        'console_scripts': [
            'flashtest=flashtest.cli:main',
        ],
    },
    python_requires='>=3.6',
)

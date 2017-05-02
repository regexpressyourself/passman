from setuptools import setup, find_packages  # Always prefer setuptools over distutils

long_description = 'See https://github.com/regexpressyourself/passman/blob/master/README.md for more'

def readme():
    with open('README.rst') as f:
        return f.read()

try:
    long_description = readme()
except:
    long_description = 'See https://github.com/regexpressyourself/passman/blob/master/README.md for more'

setup (
        name = 'passman',
        packages =find_packages(exclude=['build', 'docs', 'templates']),
        include_package_data=True,
        py_modules=['commandline', 'database', 'encryption', 'functions', 'JSON', 'login', 'menu', 'offlinemenu'],
        version = '1.2.3',
        description = 'A terminal-based password manager',
        long_description = long_description,
        author = 'Sam Messina',
        author_email = 'samuel.messina@gmail.com',
        url = 'https://github.com/regexpressyourself/passman',
        download_url = 'https://github.com/regexpressyourself/passman/archive/1.2.3.tar.gz',
        keywords = ['password', 'manager', 'terminal'],
        entry_points={'console_scripts':['passman=passman.__main__:main']},
        install_requires=[
            'pymongo',
            'pyperclip',
            'Crypto',
            'pycrypto',
            'argparse'
            ],
        license='MIT'
        )

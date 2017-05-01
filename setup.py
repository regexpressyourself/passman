from setuptools import setup, find_packages  # Always prefer setuptools over distutils

setup (
        name = 'passman',
        packages =find_packages(exclude=['build', 'docs', 'templates']), # this must be the same as the name above
        include_package_data=True,
        py_modules=['commandline', 'database', 'encryption', 'functions', 'JSON', 'login', 'menu', 'offlinemenu'],
        version = '1.1.5',
        description = 'A terminal-based password manager',
        author = 'Sam Messina',
        author_email = 'samuel.messina@gmail.com',
        url = 'https://github.com/regexpressyourself/passman', # use the URL to the github repo
        download_url = 'https://github.com/regexpressyourself/passman/1.0.tar.gz', # I'll explain this in a second
        keywords = ['password', 'manager', 'terminal'], # arbitrary keywords
        entry_points={'console_scripts':['passman=passman.__main__:main']},
        install_requires=[
            'pymongo',
            'asciimatics',
            'pyperclip',
            'Crypto',
            'pycrypto',
            'argparse'
            ],
        license='MIT'
        )

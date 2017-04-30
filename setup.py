from distutils.core import setup

setup (
        name = 'passman',
        packages = ['passman'], # this must be the same as the name above
        scripts = ['passman/passman'],
        version = '1.0.4',
        description = 'A terminal-based password manager',
        author = 'Sam Messina',
        author_email = 'samuel.messina@gmail.com',
        url = 'https://github.com/regexpressyourself/passman', # use the URL to the github repo
        download_url = 'https://github.com/regexpressyourself/passman/1.0.tar.gz', # I'll explain this in a second
        keywords = ['password', 'manager', 'terminal'], # arbitrary keywords
        entry_points={'console_scripts':['passman=passman:start']},
        install_requires=[
            'pymongo',
            'asciimatics',
            'pyperclip',
            'Crypto',
            'argparse'
            ],
        license='MIT',
        classifiers = [],
        )

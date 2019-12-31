from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='postilion',         # How you named your package folder (MyLib)
    packages=['postilion'],   # Chose the same as "name"
    version='0.0.1',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='A wrapper around the postiliion api',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Terran Blake',                   # Type in your name
    author_email='terranblake@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/terranblake/postilion',
    # I explain this later on
    download_url='https://github.com/terranblake/pypostilion/releases/download/0.0.1/postilion-0.1.tar.gz',
    # Keywords that define your package best
    keywords=[
        'financial',
        'modeling',
        'postilion',
		'python',
		'api',
		'wrapper',
		'financial-modeling',
		'clean',
		# cuz why not
		'spicy'
    ],
    # Which packages does your moodule require
    install_requires=[
        'requests',
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        # which language was the package originally written for
        'Natural Language :: English',
        # topics that meet the purpose of the module
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business',
        'Topic :: Office/Business :: Financial :: Accounting',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    include_package_data=True,
    include_dirs=[
        'README.md'
    ]
)

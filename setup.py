from setuptools import setup, find_packages

setup(name='jinyaml',
    version = '1.0',
    py_modules = ['jinyaml'],
    install_requires = ['PyYAML', 'Jinja2'],
    scripts = ['jinyaml.py'],
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'jinyaml = jinyaml:main'
        ]
    }
)

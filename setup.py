from setuptools import setup, find_packages


def listify(filename):
    with open(filename, "r") as f:
        return list(filter(None, f.read().splitlines()))


with open("README.rst", "r") as frm:
    long_description = frm.read()


setup(
    name="django-dirtyfields",
    version="1.4.1",
    url='https://github.com/romgar/django-dirtyfields',
    license='BSD',
    description=("Tracking dirty fields on a Django model instance "
                 "(actively maintained)"),
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author='Romain Garrigues',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=listify('requirements.txt'),
    classifiers=listify('CLASSIFIERS.txt')
)

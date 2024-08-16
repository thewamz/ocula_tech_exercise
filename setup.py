from setuptools import find_packages, setup

setup(
    name="ocula",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    author="Tinashe Wamambo",
    author_email="tinashe.wamambo@hotmail.co.uk",
    url="https://github.com/thewamz/ocula_tech_exercise",
    packages=find_packages(exclude=["ocula.weatherapp.tests"]),
    python_requires=">=3.10",
    install_requires=[
        "dj-database-url",
        "Django~=5.0",
        "djangorestframework~=3.15.0",
        "django-countries",
        "django-extensions",
        "gunicorn",
        "requests",
    ],
    extras_require={
        "psycopg2": ["psycopg2"],
        "psycopg2-binary": ["psycopg2-binary"],
        "testing": ["factory-boy"],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 4.0",
        "Programming Language :: Python :: 3.10",
    ],
    scripts=["manage.py"],
)

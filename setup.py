from setuptools import setup, find_packages

setup(
    name='malriq',
    author='Johan Nestaas',
    version='1.0.1',
    author_email='johan@riskiq.net',
    description='Maltego transforms integrated with RiskIQ API',
    license='GPL',
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    package_data={
        '' : [ '*.gif', '*.png', '*.conf', '*.mtz', '*.machine' ] # list of resources
    },
    install_requires=[
        'canari', 'riskiq',
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)

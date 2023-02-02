from setuptools import setup, find_packages


setup(
    name='plugin_react',
    version='1.0-dev',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'indico>=2.2.dev0'
    ],
    entry_points={'indico.plugins': {'plugin_react = plugin_react:IndicoReactPlugin'}}
)
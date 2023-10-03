import os
from setuptools import setup, find_packages



NAME = "tango_python_sdk"
DESCRIPTION = "Tango SDK Library for Python: A Python interface for generating embeddings from images, getting distances, and comparing the images."
AUTHOR = "Private Identity"
AUTHOR_EMAIL = "support@private.id"
URL = "https://private.id/"
VERSION = "1.0.0"
REQUIRES = [
    "numpy >= 1.21.0",
    "pillow >= 9.1.0"
]

LONG_DESCRIPTION = '''
'''

if os.path.exists('./README.md'):
    with open("README.md", encoding='utf-8') as fp:
        LONG_DESCRIPTION = fp.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="",
    url=URL,
    keywords=["tango", "face embeddings", "image comparison"],
    packages=find_packages(where='src', exclude=["tests*"]),
    include_package_data=True,
    platforms="any",
    install_requires=REQUIRES,
    python_requires=">=3.6",
    package_dir={'': 'src'},
    project_urls={
        "Bug Reports": 'https://github.com/prividentity/tango-python-sdk',
        "Source": 'https://github.com/prividentity/tango-python-sdk',
        "Documentation": "https://github.com/prividentity/tango-python-sdk",
        "Release Notes": "https://github.com/prividentity/tango-python-sdk"
    },
    classifiers=[
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
        "Topic :: Software Development"
    ],
    py_modules=[NAME],
    package_data={
    "tango_python_sdk": [
        'handler/lib/libopencv_core.so',
        'handler/lib/libopencv_imgproc.so',
        'handler/lib/libtango.so',
        'handler/lib/libtensorflowlite.so'
    ]
}

)

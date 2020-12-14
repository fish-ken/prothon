import setuptools

setuptools.setup(
    name="prothon",
    version="1.0.0",
    license='MIT',
    author="mousedoc",
    author_email="sangyun3631@gmail.com",
    description="Generate .proto by .xlsx",
    long_description=open('README.md').read(),
    url="https://github.com/Fish-Ken/prothon",
    packages=setuptools.find_packages(),
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
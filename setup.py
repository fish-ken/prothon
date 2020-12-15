import setuptools


def install():
    setuptools.setup(
        name='prothon',
        version='1.0.0',
        license='MIT',
        author='mousedoc',
        author_email='sangyun3631@gmail.com',
        description='Generate .proto by .xlsx',
        long_description=open('README.md').read(),
        url='https://github.com/Fish-Ken/prothon',
        packages=setuptools.find_packages(),
        classifiers=[
            # 패키지에 대한 태그
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent'
        ],
        tests_require=[
            'pytest',
        ],
    )


if __name__ == '__main__':
    install()

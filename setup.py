from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='xtract_features',
    url='https://github.com/vatsalsaglani/xrayimage_extractfeatures',
    author='Vatsal Saglani',
    author_email='saglanivatsal@gmail.com',
    # Needed to actually package something
    packages=['xtract_features'],
    # Needed for dependencies
    install_requires=['numpy', 'pandas', 'pydicom', 'matplotlib', 'scipy', 'opencv-python', 'opencv-contrib-python', 'Pillow', 'scipy', 'scikit-image', 'scikit-learn', 'tqdm'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    # description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
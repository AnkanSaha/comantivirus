from distutils.core import setup
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(name='comantivirus',
      version='5.4.7',
      description='Protect Your Windows/Linux/Mac Computer with python based light weight Anti-virus( Made By Ankan Saha ).',
       long_description = long_description,
      author='Ankan Saha',
      author_email='admin@ankansaha.in',
      url='https://github.com/AnkanSaha/comantivirus',
      packages=setuptools.find_packages()
     )
install_requires = ['pyautogui','os','time']

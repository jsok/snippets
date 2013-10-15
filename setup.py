from setuptools import setup

setup(name="Snippet",
      version="0.1",
      description="Utility to store work snippets",
      py_modules=['snippet'],
      entry_points={
          'console_scripts': [
              'snippet = snippet:main',
          ]
      },
)

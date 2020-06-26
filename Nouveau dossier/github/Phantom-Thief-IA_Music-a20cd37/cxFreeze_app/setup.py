from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('main.py',base=base)
]

setup(name='IMA',
      version = '1.0',
      description = 'Adapte votre musique a votre GamePlay.',
      options = dict(build_exe = buildOptions),
      executables = executables)

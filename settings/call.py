from path import qtile_path
from sys import path
path.append(qtile_path)
from path import ( qtile_path )
from pathlib import ( Path )
from os.path import ( join )
import subprocess

scripts_path: Path = qtile_path / Path('scripts') / Path('bin')


launcher = lambda: subprocess.run(join(scripts_path, 'launcher'), shell=True, 
                                                                  stdout=subprocess.PIPE, 
                                                                  stderr=subprocess.PIPE,
                                                                  )
keyboard_layout = lambda: subprocess.run(join(scripts_path, 'layouts'), shell=True, 
                                                                        stdout=subprocess.PIPE,
                                                                        stderr=subprocess.PIPE,
                                                                        )


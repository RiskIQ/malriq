#!/usr/bin/env python
import sys
import os
from subprocess import check_output as run, CalledProcessError

new_version = sys.argv[1]

''' sed "s/__version__ = '.*\$/__version__ = '1.0'/g" malriq/transforms/incident.py '''
basedir = os.path.dirname(__file__)
if not basedir:
    basedir = '.'
for root, dirs, files in os.walk(basedir):
    for f in files:
        if f == 'version_replace.py':
            continue
        path = os.path.join(root, f)
        if path == './malriq/transforms/incident.py':
            import pdb
            pdb.set_trace()
        if not path.endswith('.py'):
            continue
        try:
            run(['grep', '__version__', path])
        except CalledProcessError:
            continue
        out = run(
            [
                'sed', 
                "s/__version__ = '.*/__version__ = '%s'/g" % 
                    new_version, 
                path,
            ]
        )
        with open(path, 'w') as f:
            f.write(out)

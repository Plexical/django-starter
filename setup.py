import sys
import os

try:
    import paver
except ImportError:
    sys.path.insert(0, os.path.join('deps', 'paver-minilib.zip'))

import paver.tasks
paver.tasks.main()

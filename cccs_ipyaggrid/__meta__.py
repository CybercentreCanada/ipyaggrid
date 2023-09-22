import glob
import os
from os.path import isdir


def _get_version(version_info):
    """
    converts version info tuple to version string
    example:
        (0, 1, 2, 'beta', 3) returns '0.1.2-beta.3'
    """
    vi = [str(e) for e in version_info]
    suffix = ''
    if len(vi) > 3:
        suffix = '-' + '.'.join(vi[3:])
    version = '.'.join(vi[:3]) + suffix
    return version


# meta data

__name__ = 'cccs-ipyaggrid'
name_url = __name__.replace('_', '-')
__version__ = '0.5.2'
__version_js__ = __version__


__description__ = 'Jupyter widget - ag-grid in the notebook'
__long_description__ = 'See repo README'
__author__ = 'Mario Buikhuizen, Maarten Breddels, DGothrek'
__author_email__ = 'mariobuikhuizen@gmail.com, maartenbreddels@gmail.com'

# gitlab template
__url__ = 'https://github.com/widgetti/ipyaggrid'

__download_url__ = 'https://github.com/widgetti/ipyaggrid/archive/refs/tags/v{}.zip'.format(__version__)

__keywords__ = ['ipywidget',
                'javascript',
                'ag-grid',
                ]
__license__ = 'MIT'
__classifiers__ = ['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'
                   ]
__include_package_data__ = True
__package_data__ = {}
__data_files__ = [
    # classic notebook extension
    ('share/jupyter/nbextensions/cccs_ipyaggrid', [
        'cccs_ipyaggrid/nbextension/extension.js',
        'cccs_ipyaggrid/nbextension/index.js',
        'cccs_ipyaggrid/nbextension/index.js.map',
    ]),
    ('etc/jupyter/nbconfig/notebook.d', [
        'cccs_ipyaggrid/cccs_ipyaggrid.json'
    ]),
    # Lab Extension
    ('share/jupyter/labextensions/cccs_ipyaggrid', ['install.json']),
]

# Lab Extension
for root, _, files in os.walk('cccs_ipyaggrid/labextension'):
    dir_ = os.path.relpath(root, 'cccs_ipyaggrid/labextension')
    target_dir = 'share/jupyter/labextensions/cccs_ipyaggrid%s' % ('' if dir_ == '.' else "/%s" % dir_)
    __data_files__.append((target_dir, ["%s/%s" % (root, f) for f in files]))

__zip_safe__ = False
__entry_points__ = {}

import os
from cuda_lint import Linter

_pack = os.path.join(os.path.dirname(__file__), 'phpcs.phar')
_opt = '--standard=PSR2'

class Phpcs(Linter):
    syntax = ('PHP', 'PHP_')
    cmd = ('php', _pack, _opt, '--report=checkstyle')
    regex = (
        r'.*line="(?P<line>\d+)" '
        r'column="(?P<col>\d+)" '
        r'severity="(?:(?P<error>error)|(?P<warning>warning))" '
        r'message="(?P<message>.*)" source'
    )
    tempfile_suffix = 'php'

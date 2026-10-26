import html
import os
from cuda_lint import Linter

_pack = os.path.join(os.path.dirname(__file__), 'phpcs.phar')
_opt = '--standard=PSR12'

class Phpcs(Linter):
    def split_match(self, match):
        match, line, col, error, warning, message, near = super().split_match(match)

        if message:
            message = html.unescape(message)
        if near:
            near = html.unescape(near)

        return match, line, col, error, warning, message, near

    syntax = ('PHP', 'PHP_')
    cmd = ('php', _pack, _opt, '--report=checkstyle')
    regex = (
        r'.*line="(?P<line>\d+)" '
        r'column="(?P<col>\d+)" '
        r'severity="(?:(?P<error>error)|(?P<warning>warning))" '
        r'message="(?P<message>.*)" source'
    )
    tempfile_suffix = 'php'

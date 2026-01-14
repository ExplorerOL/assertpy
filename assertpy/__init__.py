from __future__ import absolute_import


def _rewrite_assertions_in_assertpy():
    """Rewrite assertions by pytest"""
    try:
        import pytest
    except ImportError:
        # pytest is not available, skip assertion rewriting
        print('Module pytest is not available, skipping assertion rewriting!!!')
        return

    # assertpy = importlib.import_module('assertpy')
    _MODULES_TO_REWRITE = {
        'assertpy.base',
        'assertpy.collection',
        'assertpy.contains',
        'assertpy.date',
        'assertpy.dict',
        'assertpy.dynamic',
        'assertpy.exception',
        'assertpy.extracting',
        'assertpy.file',
        'assertpy.numeric',
        'assertpy.snapshot',
        'assertpy.string',
    }
    for module in _MODULES_TO_REWRITE:
        print(f'Rewriting {module}...')
        pytest.register_assert_rewrite(module)


_rewrite_assertions_in_assertpy()


from .assertpy import assert_that
from .assertpy import (
    assert_warn,
    soft_assertions,
    fail,
    soft_fail,
    add_extension,
    remove_extension,
    WarningLoggingAdapter,
    __version__,
)
from .file import contents_of

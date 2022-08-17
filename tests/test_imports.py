"""
Does `admonitions` import without fail?
"""

import pytest


def test_imports():
    """
    Simply import `admonitions`, and return true if no errors are thrown.
    """
    import admonitions

    return True

# -*- coding: utf-8 -*-
"""
Defines unit tests for :mod:`colour.difference.delta_e_cam16_ucs` module.
"""

from __future__ import division, unicode_literals

import unittest

from colour.difference.tests.test_delta_e_cam02_ucs import TestDelta_E_Luo2006

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2015-2018 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['TestDelta_E_Li2017']


class TestDelta_E_Li2017(TestDelta_E_Luo2006):
    """
    Defines :func:`colour.difference.delta_e_cam16_ucs.delta_E_Li2017`
    definition unit tests methods.

    Notes
    -----
    -   :func:`colour.difference.delta_e_cam16_ucs.delta_E_Li2017` is a wrapper
        of :func:`colour.difference.delta_e_cam02_ucs.delta_E_Luo2006` and thus
        currently adopts the same unittests.
    """


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .spectrum import (SpectralShape, DEFAULT_SPECTRAL_SHAPE,
                       SpectralPowerDistribution,
                       MultiSpectralPowerDistribution)
from .blackbody import (spd_blackbody, blackbody_spectral_radiance, planck_law)
from .cmfs import (LMS_ConeFundamentals, RGB_ColourMatchingFunctions,
                   XYZ_ColourMatchingFunctions)
from .dataset import *  # noqa
from . import dataset
from .generation import spd_constant, spd_zeros, spd_ones
from .generation import SPD_GAUSSIAN_METHODS
from .generation import spd_gaussian, spd_gaussian_normal, spd_gaussian_fwhm
from .generation import SPD_SINGLE_LED_METHODS
from .generation import spd_single_led, spd_single_led_Ohno2005
from .generation import SPD_MULTI_LED_METHODS
from .generation import spd_multi_led, spd_multi_led_Ohno2005
from .tristimulus import (SPECTRAL_TO_XYZ_METHODS,
                          MULTI_SPECTRAL_TO_XYZ_METHODS)
from .tristimulus import spectral_to_XYZ, multi_spectral_to_XYZ
from .tristimulus import (
    ASTME30815_PRACTISE_SHAPE, lagrange_coefficients_ASTME202211,
    tristimulus_weighting_factors_ASTME202211,
    adjust_tristimulus_weighting_factors_ASTME30815,
    spectral_to_XYZ_integration,
    spectral_to_XYZ_tristimulus_weighting_factors_ASTME30815,
    spectral_to_XYZ_ASTME30815, multi_spectral_to_XYZ_integration,
    wavelength_to_XYZ)
from .correction import BANDPASS_CORRECTION_METHODS
from .correction import bandpass_correction
from .correction import bandpass_correction_Stearns1988
from .illuminants import (spd_CIE_illuminant_D_series,
                          CIE_standard_illuminant_A_function)
from .lefs import (mesopic_luminous_efficiency_function,
                   mesopic_weighting_function)
from .lightness import LIGHTNESS_METHODS
from .lightness import lightness
from .lightness import (lightness_Glasser1958, lightness_Wyszecki1963,
                        lightness_CIE1976, lightness_Fairchild2010,
                        lightness_Fairchild2011)
from .luminance import LUMINANCE_METHODS
from .luminance import luminance
from .luminance import (luminance_Newhall1943, luminance_ASTMD153508,
                        luminance_CIE1976, luminance_Fairchild2010,
                        luminance_Fairchild2011)
from .dominant import (dominant_wavelength, complementary_wavelength,
                       excitation_purity, colorimetric_purity)
from .photometry import luminous_flux, luminous_efficiency, luminous_efficacy
from .transformations import RGB_10_degree_cmfs_to_LMS_10_degree_cmfs
from .transformations import RGB_2_degree_cmfs_to_XYZ_2_degree_cmfs
from .transformations import RGB_10_degree_cmfs_to_XYZ_10_degree_cmfs
from .transformations import LMS_2_degree_cmfs_to_XYZ_2_degree_cmfs
from .transformations import LMS_10_degree_cmfs_to_XYZ_10_degree_cmfs
from .whiteness import WHITENESS_METHODS
from .whiteness import whiteness
from .whiteness import (whiteness_Berger1959, whiteness_Taube1960,
                        whiteness_Stensby1968, whiteness_ASTME313,
                        whiteness_Ganz1979, whiteness_CIE2004)
from .yellowness import YELLOWNESS_METHODS
from .yellowness import yellowness
from .yellowness import yellowness_ASTMD1925, yellowness_ASTME313

__all__ = [
    'SpectralShape', 'DEFAULT_SPECTRAL_SHAPE', 'SpectralPowerDistribution',
    'MultiSpectralPowerDistribution'
]
__all__ += ['spd_blackbody', 'blackbody_spectral_radiance', 'planck_law']
__all__ += [
    'LMS_ConeFundamentals', 'RGB_ColourMatchingFunctions',
    'XYZ_ColourMatchingFunctions'
]
__all__ += dataset.__all__
__all__ += ['spd_constant', 'spd_zeros', 'spd_ones']
__all__ += ['SPD_GAUSSIAN_METHODS']
__all__ += ['spd_gaussian', 'spd_gaussian_normal', 'spd_gaussian_fwhm']
__all__ += ['SPD_SINGLE_LED_METHODS']
__all__ += ['spd_single_led', 'spd_single_led_Ohno2005']
__all__ += ['SPD_MULTI_LED_METHODS']
__all__ += ['spd_multi_led', 'spd_multi_led_Ohno2005']
__all__ += ['SPECTRAL_TO_XYZ_METHODS', 'MULTI_SPECTRAL_TO_XYZ_METHODS']
__all__ += ['spectral_to_XYZ', 'multi_spectral_to_XYZ']
__all__ += [
    'ASTME30815_PRACTISE_SHAPE', 'lagrange_coefficients_ASTME202211',
    'tristimulus_weighting_factors_ASTME202211',
    'adjust_tristimulus_weighting_factors_ASTME30815',
    'spectral_to_XYZ_integration',
    'spectral_to_XYZ_tristimulus_weighting_factors_ASTME30815',
    'spectral_to_XYZ_ASTME30815', 'multi_spectral_to_XYZ_integration',
    'wavelength_to_XYZ'
]
__all__ += ['BANDPASS_CORRECTION_METHODS']
__all__ += ['bandpass_correction']
__all__ += ['bandpass_correction_Stearns1988']
__all__ += [
    'spd_CIE_illuminant_D_series', 'CIE_standard_illuminant_A_function'
]
__all__ += [
    'mesopic_luminous_efficiency_function', 'mesopic_weighting_function'
]
__all__ += ['LIGHTNESS_METHODS']
__all__ += ['lightness']
__all__ += [
    'lightness_Glasser1958', 'lightness_Wyszecki1963', 'lightness_CIE1976',
    'lightness_Fairchild2010', 'lightness_Fairchild2011'
]
__all__ += ['LUMINANCE_METHODS']
__all__ += ['luminance']
__all__ += [
    'luminance_Newhall1943', 'luminance_ASTMD153508', 'luminance_CIE1976',
    'luminance_Fairchild2010', 'luminance_Fairchild2011'
]
__all__ += [
    'dominant_wavelength', 'complementary_wavelength', 'excitation_purity',
    'colorimetric_purity'
]
__all__ += ['luminous_flux', 'luminous_efficiency', 'luminous_efficacy']
__all__ += ['RGB_10_degree_cmfs_to_LMS_10_degree_cmfs']
__all__ += ['RGB_2_degree_cmfs_to_XYZ_2_degree_cmfs']
__all__ += ['RGB_10_degree_cmfs_to_XYZ_10_degree_cmfs']
__all__ += ['LMS_2_degree_cmfs_to_XYZ_2_degree_cmfs']
__all__ += ['LMS_10_degree_cmfs_to_XYZ_10_degree_cmfs']
__all__ += ['WHITENESS_METHODS']
__all__ += ['whiteness']
__all__ += [
    'whiteness_Berger1959', 'whiteness_Taube1960', 'whiteness_Stensby1968',
    'whiteness_ASTME313', 'whiteness_Ganz1979', 'whiteness_CIE2004'
]
__all__ += ['YELLOWNESS_METHODS']
__all__ += ['yellowness']
__all__ += ['yellowness_ASTMD1925', 'yellowness_ASTME313']

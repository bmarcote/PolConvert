from distutils.core import setup, Extension
import numpy as np

print ''
print '#######################################################################'
print '# Compiling with numpy version', np.__version__
print '#',                              np.__file__
print '#######################################################################'
print ''

# COMPILE THE GLOBAL CROSS-POLARIZATION FRINGE FITTING.
# IT NEEDS FFTW AND GSL:
DO_SOLVE = True


# it is not clear if include_dirs is needed or not


sourcefiles1 = ['CalTable.cpp', 'DataIO.cpp', 'DataIOFITS.cpp',
                'DataIOSWIN.cpp', 'Weighter.cpp', '_PolConvert.cpp']

sourcefiles2 = ['_PolGainSolve.cpp']

sourcefiles3 = ['_getAntInfo.cpp']

sourcefiles4 = ['_XPCal.cpp']

c_ext1 = Extension("_PolConvert", sources=sourcefiles1,
                  extra_compile_args=["-Wno-deprecated","-O3","-std=c++11"],
                  libraries=['cfitsio'],
                  include_dirs=[np.get_include()],
                  extra_link_args=["-Xlinker", "-export-dynamic"])

c_ext3 = Extension("_getAntInfo", sources=sourcefiles3,
                  extra_compile_args=["-Wno-deprecated","-O3","-std=c++11"],
                  libraries=['cfitsio'],
                  include_dirs=[np.get_include()],
                  extra_link_args=["-Xlinker", "-export-dynamic"])

c_ext4 = Extension("_XPCal",sources=sourcefiles4,
                  extra_compile_args=["-Wno-deprecated","-O3","-std=c++11"],
                  include_dirs=[np.get_include()],
                  extra_link_args=["-Xlinker","-export-dynamic"])


if DO_SOLVE:
  # gsl depends on cblas on some machines
  # however, cblas needs to be installed so configure tests
  # are needed.  Commenting this out until I have time to fix this.
  # libraries=['gsl','cblas','fftw3']
  c_ext2 = Extension("_PolGainSolve", sources=sourcefiles2,
                  libraries=['gsl','fftw3'],
                  include_dirs=[np.get_include()],
                  extra_compile_args=["-Wno-deprecated","-O3","-std=c++11"],
                  extra_link_args=["-Xlinker", "-export-dynamic"])

cfitsio='/usr/include/cfitsio'
setup(
    ext_modules=[c_ext1], include_dirs=[cfitsio,'./'],
)


setup(
    ext_modules=[c_ext3], include_dirs=[cfitsio,'./'],
)


setup(
    ext_modules=[c_ext4],include_dirs=['./'],
)


if DO_SOLVE:
  setup(
    ext_modules=[c_ext2],
  )






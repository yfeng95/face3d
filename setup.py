from distutils.core import setup
from distutils.extension import Extension

import numpy
from Cython.Distutils import build_ext

cmdclass = {'build_ext': build_ext}
ext_modules = [Extension("face3d.mesh.cython.mesh_core_cython",
                         sources=["face3d/mesh/cython/mesh_core_cython.pyx", "face3d/mesh/cython/mesh_core.cpp"],
                         language='c++',
                         include_dirs=[numpy.get_include(), '.'])]

setup(
    name='face3d',
    cmdclass=cmdclass,
    ext_modules=ext_modules,
    version='1.0',
    description='Python tools for 3D face: 3DMM, Mesh processing(transform, camera, light, render), '
                '3D face representations.',
    author='Yao Feng',
    author_email='yaofeng1995@gmail.com',
    packages=['face3d', 'face3d.mesh', 'face3d.mesh_numpy', 'face3d.morphable_model', 'face3d.mesh.cython'],
)

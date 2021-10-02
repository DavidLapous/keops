# Always prefer setuptools over distutils
# To use a consistent encoding
from codecs import open
import os
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(os.path.join(here, "pykeops", "keops_version"), encoding="utf-8") as v:
    current_version = v.read().rstrip()

# Get the long description from the README file
with open(path.join(here, "pykeops", "readme.md"), encoding="utf-8") as f:
    long_description = f.read()


def import_files(dirname, ext=["h", "hpp"]):
    _dirname = path.join(os.getcwd(), "pykeops", dirname)
    res = [
        path.join(dirname, f)
        for f in os.listdir(_dirname)
        if any(f.endswith(ext) for ext in ext)
    ]
    return res


tao_seq_files = import_files("keops/lib/sequences/include/tao/seq/") + import_files(
    "keops/lib/sequences/include/tao/seq/contrib/"
)

setup(
    name="pykeops",
    version=current_version,
    description="Python bindings of KeOps: KErnel OPerationS, on CPUs and GPUs, with autodiff and without memory overflows",  # Required
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://www.kernel-operations.io/",
    project_urls={
        "Bug Reports": "https://github.com/getkeops/keops/issues",
        "Source": "https://github.com/getkeops/keops",
    },
    author="B. Charlier, J. Feydy, J. Glaunes",
    author_email="benjamin.charlier@umontpellier.fr, jean.feydy@gmail.com, alexis.glaunes@parisdescartes.fr",
    python_requires=">=3",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: C++",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="kernels gpu autodiff",
    packages=[
        "pykeops",
        "pykeops.common",
        "pykeops.numpy",
        "pykeops.numpy.cluster",
        "pykeops.numpy.generic",
        "pykeops.numpy.lazytensor",
        "pykeops.test",
        "pykeops.torch",
        "pykeops.torch.cluster",
        "pykeops.torch.generic",
        "pykeops.torch.lazytensor",
        "pykeops.torch.kernel_product",
    ],
    package_data={
        "pykeops": [
            "readme.md",
            "licence.txt",
            "numpy/generic/generic_red.cpp",
            "torch/generic/generic_red.cpp",
            "torch/generic/generic_red.cpp",
            "version",
        ]
        + import_files(path.join("keops", "binders"))
        + import_files(path.join("keops", "core", "autodiff"))
        + import_files(path.join("keops", "core", "pack"))
        + import_files(path.join("keops", "core", "formulas"))
        + import_files(path.join("keops", "core", "formulas", "constants"))
        + import_files(path.join("keops", "core", "formulas", "complex"))
        + import_files(path.join("keops", "core", "formulas", "kernels"))
        + import_files(path.join("keops", "core", "formulas", "maths"))
        + import_files(path.join("keops", "core", "formulas", "norms"))
        + import_files(path.join("keops", "core", "reductions"))
        + import_files(path.join("keops", "core", "utils"), ["h", "cu"])
        + import_files(path.join("keops", "core", "mapreduce"), ["h", "cpp", "cu"])
        + import_files(path.join("keops", "core"), ["h", "cpp", "cu"])
        + import_files(path.join("keops", "python_engine"), ["py"])
        + [
            "keops/specific/CMakeLists.txt",
            "keops/specific/radial_kernels/cuda_conv.cu",
            "keops/specific/radial_kernels/cuda_conv.cx",
            "keops/specific/radial_kernels/cuda_grad1conv.cu",
            "keops/specific/radial_kernels/cuda_grad1conv.cx",
            "keops/specific/radial_kernels/radial_kernels.h",
            "keops/specific/shape_distance/fshape_gpu.cu",
            "keops/specific/shape_distance/fshape_gpu.cx",
            "keops/specific/shape_distance/kernels.cx",
        ]
        + tao_seq_files
    },
    install_requires=["numpy",],
    extras_require={
        "colab": ["torch", "cmake>=3.18",],
        "full": [
            "sphinx",
            "sphinx-gallery",
            "recommonmark",
            "sphinxcontrib-httpdomain",
            "sphinx_rtd_theme",
            "breathe",
            "matplotlib",
            "imageio",
            "torch",
            "gpytorch",
            "scikit-learn",
        ],
    },
)

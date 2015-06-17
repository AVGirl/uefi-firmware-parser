#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages, Extension
import os

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='UEFI Firmware Parser',
    version='0.2',
    description='Various data structures and parsing tools for UEFI firmware.',
    long_description=readme,
    author='Teddy Reed',
    author_email='teddy@prosauce.org',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),

    ext_modules=[
        Extension(
            'uefi_firmware.efi_compressor',
            sources=[
                os.path.join(
                    "uefi_firmware", "compression", "Tiano", "EfiCompress.c"),
                os.path.join(
                    "uefi_firmware", "compression", "Tiano", "TianoCompress.c"),
                os.path.join(
                    "uefi_firmware", "compression", "Tiano", "Decompress.c"),

                os.path.join(
                    "uefi_firmware", "compression", "LZMA", "SDK", "C", "Bra86.c"),
                os.path.join(
                    "uefi_firmware", "compression", "LZMA", "SDK", "C", "LzFind.c"),
                os.path.join(
                    "uefi_firmware", "compression", "LZMA", "SDK", "C", "LzmaDec.c"),
                os.path.join(
                    "uefi_firmware", "compression", "LZMA", "SDK", "C", "LzmaEnc.c"),
                os.path.join(
                    "uefi_firmware", "compression", "LZMA", "LzmaCompress.c"),
                os.path.join(
                    "uefi_firmware", "compression", "LZMA", "LzmaDecompress.c"),

                os.path.join("uefi_firmware", "compression", "EfiCompressor.c")
            ],
            include_dirs=[
                os.path.join("uefi_firmware", 'compression', 'Include')
            ],
        )
    ],
)

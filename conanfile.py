#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration
import os


class DirEntConan(ConanFile):
    name = "dirent"
    version = "1.23.2"
    description = "Dirent is a C/C++ programming interface that allows programmers to retrieve information about " \
                  "files and directories under Linux/UNIX"
    topics = ("conan", "dirent", "directory", "file system")
    url = "https://github.com/bincrafters/conan-dirent"
    homepage = "https://github.com/tronkko/dirent"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def configure(self):
        if self.settings.compiler != "Visual Studio":
            raise ConanInvalidConfiguration("only Visual Studio builds are supported")

    def source(self):
        tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, self.version),
                  sha256="f72d39e3c39610b6901e391b140aa69b51e0eb99216939ed5e547b5dad03afb1")
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTS"] = False
        cmake.configure(build_folder=self._build_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_id(self):
        self.info.header_only()

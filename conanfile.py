import os
from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration


class DirEntConanWin32(ConanFile):
    name = "dirent-win32"
    version = "1.23.2"
    description = "Dirent is a C/C++ programming interface that allows programmers to retrieve information about " \
                  "files and directories under Linux/UNIX"
    topics = ("conan", "dirent", "directory", "file system")
    url = "https://github.com/bincrafters/conan-dirent"
    homepage = "https://github.com/tronkko/dirent"
    license = "MIT"
    exports = ["LICENSE.md"]
    settings = "compiler"
    no_copy_source = True
    _source_subfolder = "source_subfolder"

    def configure(self):
        if self.settings.compiler != "Visual Studio":
            raise ConanInvalidConfiguration("only Visual Studio builds are supported")

    def source(self):
        tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, self.version),
                  sha256="f72d39e3c39610b6901e391b140aa69b51e0eb99216939ed5e547b5dad03afb1")
        extracted_dir = "dirent-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="dirent.h", dst="include", src=os.path.join(self._source_subfolder, "include"))

    def package_id(self):
        self.info.header_only()

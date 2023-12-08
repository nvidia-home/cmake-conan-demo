import sys
import os
from conans import ConanFile
current_pwd=os.path.dirname(os.path.abspath(__file__))
# print("file path", conans.__file__)

class Recipe(ConanFile):
    deps_dir = os.path.join(current_pwd, "deps")

    name = "conan-cmake-demo"
    version = "2.7.0"

    def config_options(self):
      # 这里如果想要将 cmake 中的 -DDEVICE 传过来，就需要在 conan.cmake 中再处理一下 -o
      self.options['tensorrt'].device="CUDA11.4"
    def configure(self):
      pass
      

    def package_id(self):
        super().package_id()

    def build_requirements(self):
      self.build_requires("fmt/8.0.1")

    def imports(self):
      self.copy("*", os.path.join(self.deps_dir, "lib"), src="lib")



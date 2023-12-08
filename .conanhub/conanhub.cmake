include(${CMAKE_CURRENT_SOURCE_DIR}/.conanhub/conan.cmake)

conan_cmake_run(CONANFILE conanfile.py  # or relative build/conanfile.txt
                BASIC_SETUP CMAKE_TARGETS
                BUILD missing)

include(${CMAKE_CURRENT_SOURCE_DIR}/build/conanbuildinfo.cmake)
conan_basic_setup()

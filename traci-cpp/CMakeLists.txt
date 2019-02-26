cmake_minimum_required(VERSION 2.8.3)
project(traci_api)

set(PROJECT_NAME traci_api)
set(CMAKE_BUILD_TYPE Release)

# The project version number.
set(VERSION_MAJOR   0   CACHE STRING "Project major version number.")
set(VERSION_MINOR   0   CACHE STRING "Project minor version number.")
set(VERSION_PATCH   1   CACHE STRING "Project patch version number.")
mark_as_advanced(VERSION_MAJOR VERSION_MINOR VERSION_PATCH)

add_compile_options(-std=c++11)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)

include_directories(include)
file(GLOB SOURCES "src/*.cpp")
file(GLOB TESTS "tests/*.cpp")

add_library(traci_api SHARED ${SOURCES})
target_include_directories (traci_api PUBLIC include})

add_executable(example ${TESTS})
target_link_libraries (example traci_api)

# install (TARGETS Main DESTINATION bin)

install (FILES include/traci_api/socket.h
               include/traci_api/storage.h
               include/traci_api/TraCIAPI.h
               include/traci_api/TraCIDefs.h
         DESTINATION include/traci_api)

install (TARGETS traci_api
         ARCHIVE DESTINATION lib
         LIBRARY DESTINATION lib
         RUNTIME DESTINATION bin)
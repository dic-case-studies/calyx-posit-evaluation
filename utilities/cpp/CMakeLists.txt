cmake_minimum_required(VERSION 3.14)
project(PositEvaluationUtilties)

include_directories(universal/include)

add_executable(f2p_convertor f2p_convertor.cc)
add_executable(p2f_convertor p2f_convertor.cc)

set(CMAKE_CXX_FLAGS "-march=native -mtune=generic")
set(CMAKE_CXX_COMPILER g++)

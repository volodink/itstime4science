cmake_minimum_required(VERSION 3.6)
project(untitled1)

set(CMAKE_C_STANDARD 99)

set(SOURCE_FILES generate_packet.c)
add_executable(untitled1 ${SOURCE_FILES})
# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /root/LatestVersion/Dionysus

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /root/LatestVersion/Dionysus/build

# Utility rule file for rips-pairwise.py.

# Include the progress variables for this target.
include examples/rips/CMakeFiles/rips-pairwise.py.dir/progress.make

examples/rips/CMakeFiles/rips-pairwise.py:
	cd /root/LatestVersion/Dionysus/build/examples/rips && /usr/bin/cmake -E copy /root/LatestVersion/Dionysus/examples/rips/rips-pairwise.py /root/LatestVersion/Dionysus/build/examples/rips/rips-pairwise.py

rips-pairwise.py: examples/rips/CMakeFiles/rips-pairwise.py
rips-pairwise.py: examples/rips/CMakeFiles/rips-pairwise.py.dir/build.make

.PHONY : rips-pairwise.py

# Rule to build all files generated by this target.
examples/rips/CMakeFiles/rips-pairwise.py.dir/build: rips-pairwise.py

.PHONY : examples/rips/CMakeFiles/rips-pairwise.py.dir/build

examples/rips/CMakeFiles/rips-pairwise.py.dir/clean:
	cd /root/LatestVersion/Dionysus/build/examples/rips && $(CMAKE_COMMAND) -P CMakeFiles/rips-pairwise.py.dir/cmake_clean.cmake
.PHONY : examples/rips/CMakeFiles/rips-pairwise.py.dir/clean

examples/rips/CMakeFiles/rips-pairwise.py.dir/depend:
	cd /root/LatestVersion/Dionysus/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /root/LatestVersion/Dionysus /root/LatestVersion/Dionysus/examples/rips /root/LatestVersion/Dionysus/build /root/LatestVersion/Dionysus/build/examples/rips /root/LatestVersion/Dionysus/build/examples/rips/CMakeFiles/rips-pairwise.py.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : examples/rips/CMakeFiles/rips-pairwise.py.dir/depend


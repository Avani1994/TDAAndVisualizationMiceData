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

# Include any dependencies generated for this target.
include examples/rips/CMakeFiles/rips-weighted.dir/depend.make

# Include the progress variables for this target.
include examples/rips/CMakeFiles/rips-weighted.dir/progress.make

# Include the compile flags for this target's objects.
include examples/rips/CMakeFiles/rips-weighted.dir/flags.make

examples/rips/CMakeFiles/rips-weighted.dir/rips-weighted.o: examples/rips/CMakeFiles/rips-weighted.dir/flags.make
examples/rips/CMakeFiles/rips-weighted.dir/rips-weighted.o: ../examples/rips/rips-weighted.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/root/LatestVersion/Dionysus/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object examples/rips/CMakeFiles/rips-weighted.dir/rips-weighted.o"
	cd /root/LatestVersion/Dionysus/build/examples/rips && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rips-weighted.dir/rips-weighted.o -c /root/LatestVersion/Dionysus/examples/rips/rips-weighted.cpp

examples/rips/CMakeFiles/rips-weighted.dir/rips-weighted.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rips-weighted.dir/rips-weighted.i"
	cd /root/LatestVersion/Dionysus/build/examples/rips && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /root/LatestVersion/Dionysus/examples/rips/rips-weighted.cpp > CMakeFiles/rips-weighted.dir/rips-weighted.i

examples/rips/CMakeFiles/rips-weighted.dir/rips-weighted.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rips-weighted.dir/rips-weighted.s"
	cd /root/LatestVersion/Dionysus/build/examples/rips && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /root/LatestVersion/Dionysus/examples/rips/rips-weighted.cpp -o CMakeFiles/rips-weighted.dir/rips-weighted.s

# Object files for target rips-weighted
rips__weighted_OBJECTS = \
"CMakeFiles/rips-weighted.dir/rips-weighted.o"

# External object files for target rips-weighted
rips__weighted_EXTERNAL_OBJECTS =

examples/rips/rips-weighted: examples/rips/CMakeFiles/rips-weighted.dir/rips-weighted.o
examples/rips/rips-weighted: examples/rips/CMakeFiles/rips-weighted.dir/build.make
examples/rips/rips-weighted: /usr/lib/x86_64-linux-gnu/libboost_program_options.so.1.71.0
examples/rips/rips-weighted: /usr/lib/x86_64-linux-gnu/libboost_serialization.so.1.71.0
examples/rips/rips-weighted: examples/rips/CMakeFiles/rips-weighted.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/root/LatestVersion/Dionysus/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable rips-weighted"
	cd /root/LatestVersion/Dionysus/build/examples/rips && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/rips-weighted.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/rips/CMakeFiles/rips-weighted.dir/build: examples/rips/rips-weighted

.PHONY : examples/rips/CMakeFiles/rips-weighted.dir/build

examples/rips/CMakeFiles/rips-weighted.dir/clean:
	cd /root/LatestVersion/Dionysus/build/examples/rips && $(CMAKE_COMMAND) -P CMakeFiles/rips-weighted.dir/cmake_clean.cmake
.PHONY : examples/rips/CMakeFiles/rips-weighted.dir/clean

examples/rips/CMakeFiles/rips-weighted.dir/depend:
	cd /root/LatestVersion/Dionysus/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /root/LatestVersion/Dionysus /root/LatestVersion/Dionysus/examples/rips /root/LatestVersion/Dionysus/build /root/LatestVersion/Dionysus/build/examples/rips /root/LatestVersion/Dionysus/build/examples/rips/CMakeFiles/rips-weighted.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : examples/rips/CMakeFiles/rips-weighted.dir/depend


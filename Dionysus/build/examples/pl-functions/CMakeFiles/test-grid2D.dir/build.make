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
include examples/pl-functions/CMakeFiles/test-grid2D.dir/depend.make

# Include the progress variables for this target.
include examples/pl-functions/CMakeFiles/test-grid2D.dir/progress.make

# Include the compile flags for this target's objects.
include examples/pl-functions/CMakeFiles/test-grid2D.dir/flags.make

examples/pl-functions/CMakeFiles/test-grid2D.dir/test-grid2D.o: examples/pl-functions/CMakeFiles/test-grid2D.dir/flags.make
examples/pl-functions/CMakeFiles/test-grid2D.dir/test-grid2D.o: ../examples/pl-functions/test-grid2D.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/root/LatestVersion/Dionysus/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object examples/pl-functions/CMakeFiles/test-grid2D.dir/test-grid2D.o"
	cd /root/LatestVersion/Dionysus/build/examples/pl-functions && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test-grid2D.dir/test-grid2D.o -c /root/LatestVersion/Dionysus/examples/pl-functions/test-grid2D.cpp

examples/pl-functions/CMakeFiles/test-grid2D.dir/test-grid2D.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test-grid2D.dir/test-grid2D.i"
	cd /root/LatestVersion/Dionysus/build/examples/pl-functions && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /root/LatestVersion/Dionysus/examples/pl-functions/test-grid2D.cpp > CMakeFiles/test-grid2D.dir/test-grid2D.i

examples/pl-functions/CMakeFiles/test-grid2D.dir/test-grid2D.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test-grid2D.dir/test-grid2D.s"
	cd /root/LatestVersion/Dionysus/build/examples/pl-functions && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /root/LatestVersion/Dionysus/examples/pl-functions/test-grid2D.cpp -o CMakeFiles/test-grid2D.dir/test-grid2D.s

# Object files for target test-grid2D
test__grid2D_OBJECTS = \
"CMakeFiles/test-grid2D.dir/test-grid2D.o"

# External object files for target test-grid2D
test__grid2D_EXTERNAL_OBJECTS =

examples/pl-functions/test-grid2D: examples/pl-functions/CMakeFiles/test-grid2D.dir/test-grid2D.o
examples/pl-functions/test-grid2D: examples/pl-functions/CMakeFiles/test-grid2D.dir/build.make
examples/pl-functions/test-grid2D: /usr/lib/x86_64-linux-gnu/libboost_program_options.so.1.71.0
examples/pl-functions/test-grid2D: examples/pl-functions/CMakeFiles/test-grid2D.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/root/LatestVersion/Dionysus/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable test-grid2D"
	cd /root/LatestVersion/Dionysus/build/examples/pl-functions && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test-grid2D.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/pl-functions/CMakeFiles/test-grid2D.dir/build: examples/pl-functions/test-grid2D

.PHONY : examples/pl-functions/CMakeFiles/test-grid2D.dir/build

examples/pl-functions/CMakeFiles/test-grid2D.dir/clean:
	cd /root/LatestVersion/Dionysus/build/examples/pl-functions && $(CMAKE_COMMAND) -P CMakeFiles/test-grid2D.dir/cmake_clean.cmake
.PHONY : examples/pl-functions/CMakeFiles/test-grid2D.dir/clean

examples/pl-functions/CMakeFiles/test-grid2D.dir/depend:
	cd /root/LatestVersion/Dionysus/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /root/LatestVersion/Dionysus /root/LatestVersion/Dionysus/examples/pl-functions /root/LatestVersion/Dionysus/build /root/LatestVersion/Dionysus/build/examples/pl-functions /root/LatestVersion/Dionysus/build/examples/pl-functions/CMakeFiles/test-grid2D.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : examples/pl-functions/CMakeFiles/test-grid2D.dir/depend


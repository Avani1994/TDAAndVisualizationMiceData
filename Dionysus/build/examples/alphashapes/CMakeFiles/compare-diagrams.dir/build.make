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
include examples/alphashapes/CMakeFiles/compare-diagrams.dir/depend.make

# Include the progress variables for this target.
include examples/alphashapes/CMakeFiles/compare-diagrams.dir/progress.make

# Include the compile flags for this target's objects.
include examples/alphashapes/CMakeFiles/compare-diagrams.dir/flags.make

examples/alphashapes/CMakeFiles/compare-diagrams.dir/compare-diagrams.o: examples/alphashapes/CMakeFiles/compare-diagrams.dir/flags.make
examples/alphashapes/CMakeFiles/compare-diagrams.dir/compare-diagrams.o: ../examples/alphashapes/compare-diagrams.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/root/LatestVersion/Dionysus/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object examples/alphashapes/CMakeFiles/compare-diagrams.dir/compare-diagrams.o"
	cd /root/LatestVersion/Dionysus/build/examples/alphashapes && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/compare-diagrams.dir/compare-diagrams.o -c /root/LatestVersion/Dionysus/examples/alphashapes/compare-diagrams.cpp

examples/alphashapes/CMakeFiles/compare-diagrams.dir/compare-diagrams.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/compare-diagrams.dir/compare-diagrams.i"
	cd /root/LatestVersion/Dionysus/build/examples/alphashapes && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /root/LatestVersion/Dionysus/examples/alphashapes/compare-diagrams.cpp > CMakeFiles/compare-diagrams.dir/compare-diagrams.i

examples/alphashapes/CMakeFiles/compare-diagrams.dir/compare-diagrams.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/compare-diagrams.dir/compare-diagrams.s"
	cd /root/LatestVersion/Dionysus/build/examples/alphashapes && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /root/LatestVersion/Dionysus/examples/alphashapes/compare-diagrams.cpp -o CMakeFiles/compare-diagrams.dir/compare-diagrams.s

# Object files for target compare-diagrams
compare__diagrams_OBJECTS = \
"CMakeFiles/compare-diagrams.dir/compare-diagrams.o"

# External object files for target compare-diagrams
compare__diagrams_EXTERNAL_OBJECTS =

examples/alphashapes/compare-diagrams: examples/alphashapes/CMakeFiles/compare-diagrams.dir/compare-diagrams.o
examples/alphashapes/compare-diagrams: examples/alphashapes/CMakeFiles/compare-diagrams.dir/build.make
examples/alphashapes/compare-diagrams: /usr/lib/x86_64-linux-gnu/libboost_serialization.so.1.71.0
examples/alphashapes/compare-diagrams: /usr/lib/x86_64-linux-gnu/libboost_program_options.so.1.71.0
examples/alphashapes/compare-diagrams: examples/alphashapes/CMakeFiles/compare-diagrams.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/root/LatestVersion/Dionysus/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable compare-diagrams"
	cd /root/LatestVersion/Dionysus/build/examples/alphashapes && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/compare-diagrams.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/alphashapes/CMakeFiles/compare-diagrams.dir/build: examples/alphashapes/compare-diagrams

.PHONY : examples/alphashapes/CMakeFiles/compare-diagrams.dir/build

examples/alphashapes/CMakeFiles/compare-diagrams.dir/clean:
	cd /root/LatestVersion/Dionysus/build/examples/alphashapes && $(CMAKE_COMMAND) -P CMakeFiles/compare-diagrams.dir/cmake_clean.cmake
.PHONY : examples/alphashapes/CMakeFiles/compare-diagrams.dir/clean

examples/alphashapes/CMakeFiles/compare-diagrams.dir/depend:
	cd /root/LatestVersion/Dionysus/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /root/LatestVersion/Dionysus /root/LatestVersion/Dionysus/examples/alphashapes /root/LatestVersion/Dionysus/build /root/LatestVersion/Dionysus/build/examples/alphashapes /root/LatestVersion/Dionysus/build/examples/alphashapes/CMakeFiles/compare-diagrams.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : examples/alphashapes/CMakeFiles/compare-diagrams.dir/depend

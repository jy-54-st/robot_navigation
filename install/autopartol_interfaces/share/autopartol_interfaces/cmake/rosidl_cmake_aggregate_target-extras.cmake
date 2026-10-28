# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target autopartol_interfaces::autopartol_interfaces
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${autopartol_interfaces_TARGETS}.
if(autopartol_interfaces_TARGETS AND NOT TARGET autopartol_interfaces::autopartol_interfaces)
  add_library(autopartol_interfaces::autopartol_interfaces INTERFACE IMPORTED)
  set_target_properties(autopartol_interfaces::autopartol_interfaces PROPERTIES
    INTERFACE_LINK_LIBRARIES "${autopartol_interfaces_TARGETS}")
endif()

cmake_minimum_required(VERSION 3.0.2)
project(magnet_v2_description)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY launch meshes rviz urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

# Only install launch if you keep ROS1 launch files there.
# If you leave the ROS2 *.launch.py files in place, either remove this block
# or move them elsewhere.
# install(DIRECTORY launch
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )
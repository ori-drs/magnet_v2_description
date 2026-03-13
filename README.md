# magnet_v2_description

<p align="center"><img src=./media/magnet_v2_picture.png>

This package contains a **URDF Xacro description of the Magnet V2**, a mapping device consisting of a Hesai QT64/Pander XT32, a Microstrain GX5-AR, 3 E-con global shutter cameras and a Jetson Orin AGX Dev Kit.

This ReadMe is for ROS1 specifically that we used to run with the Anymal-d simulator to create a complete robot urdf assembly.


This package requires the `microstrain_inertial_description`, `joint_state_publisher`, as well as `xacro`. In following steps assume you have `xarco` and `joint_state_publisher` installed already.

Go to your catkin_ws and do:
```bash
cd src
git clone git@github.com:ori-drs/hesai_description.git
cd hesai_description
git checkout ros1
cd ../..
catkin build hesai_description
source devel/setup.bash
cd src
git clone https://github.com/LORD-MicroStrain/microstrain_inertial.git
cd ..
catkin build microstrain_inertial_description
source devel/setup.bash
cd src
git clone git@github.com:ori-drs/magnet_v2_description.git
cd magnet_v2_description
git checkout compatible_with_anymal_d_ros_1
cd ../..
catkin build magnet_v2_description
source devel/setup.bash
```

For visualizing the URDF with RViz launch:

```bash
roslaunch magnet_v2_description visualize.launch
```


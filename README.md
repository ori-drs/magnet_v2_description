# magnet_v2_description

<p align="center"><img src=./media/magnet_v2_picture.png>

This package contains a **URDF Xacro description of the Magnet V2**, a mapping device consisting of a Hesai QT64/Pander XT32, a Microstrain GX5-AR, 3 E-con global shutter cameras and a Jetson Orin AGX Dev Kit.

This ReadMe is for ROS1 specifically that we used to run with the Anymal-d simulator to create a complete robot urdf assembly.


This package requires the `microstrain_inertial_description`, `xacro`, and `joint_state_publisher`. In following steps assume you have xarco and installed already.

Go to your ros2_ws and do:
```bash
cd src
git clone git@github.com:ros/joint_state_publisher.git
cd ..
colcon build --packages-select joint_state_publisher
colcon build --packages-select joint_state_publisher_gui
source install/setup.bash

cd src
git clone git@github.com:ori-drs/hesai_description.git
cd ..
colcon build --packages-select hesai_description
source install/setup.bash

cd src
git clone https://github.com/LORD-MicroStrain/microstrain_inertial.git
cd microstrain_inertial
git checkout ros2
cd ../..
colcon build --packages-select microstrain_inertial_description
source install/setup.bash

cd src
git clone git@github.com:ori-drs/magnet_v2_description.git
cd magnet_v2_description
git checkout ros2_maintained
cd ../..
colcon build --packages-select magnet_v2_description
source install/setup.bash
```

For visualizing the URDF with RViz launch:

```bash
$ ros2 launch magnet_v2_description visualize.launch.py
```


from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    simulation = LaunchConfiguration("simulation")
    xacro_file = LaunchConfiguration("xacro_file")

    robot_description = {
        "robot_description": Command(
            [
                "xacro ",
                xacro_file,
                " simulation:=",
                simulation,
            ]
        )
    }

    return LaunchDescription(
        [
            DeclareLaunchArgument("simulation", default_value="true"),
            DeclareLaunchArgument(
                "xacro_file",
                default_value=PathJoinSubstitution(
                    [FindPackageShare("magnet_v2_description"), "urdf", "standalone.urdf.xacro"]
                ),
            ),
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                name="robot_state_publisher",
                output="screen",
                parameters=[robot_description],
            ),
        ]
    )

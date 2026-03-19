import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    package_share = FindPackageShare("magnet_v2_description")

    # If VS Code is installed as a snap, inherited GUI env vars can force rviz2
    # to load snap core20 system libraries, which are ABI-incompatible.
    rviz_env = {
        "GIO_MODULE_DIR": os.environ.get("GIO_MODULE_DIR_VSCODE_SNAP_ORIG", ""),
        "GTK_PATH": os.environ.get("GTK_PATH_VSCODE_SNAP_ORIG", ""),
        "LOCPATH": os.environ.get("LOCPATH_VSCODE_SNAP_ORIG", ""),
        "GTK_EXE_PREFIX": os.environ.get("GTK_EXE_PREFIX_VSCODE_SNAP_ORIG", ""),
        "GSETTINGS_SCHEMA_DIR": os.environ.get(
            "GSETTINGS_SCHEMA_DIR_VSCODE_SNAP_ORIG", ""
        ),
        "GTK_IM_MODULE_FILE": os.environ.get(
            "GTK_IM_MODULE_FILE_VSCODE_SNAP_ORIG", ""
        ),
    }

    description_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([package_share, "launch", "description.launch.py"])
        ),
        launch_arguments={"simulation": "true"}.items(),
    )

    joint_state_publisher = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        name="joint_state_publisher",
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        arguments=[
            "-d",
            PathJoinSubstitution([package_share, "rviz", "model.rviz"]),
        ],
        output="screen",
        additional_env=rviz_env,
    )

    return LaunchDescription(
        [
            description_launch,
            joint_state_publisher,
            rviz_node,
        ]
    )

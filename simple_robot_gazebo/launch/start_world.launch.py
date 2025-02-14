import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_prefix

pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
pkg_simple_robot_gazebo = get_package_share_directory('simple_robot_gazebo')
gazebo_models_path = os.path.join(pkg_simple_robot_gazebo, 'models')


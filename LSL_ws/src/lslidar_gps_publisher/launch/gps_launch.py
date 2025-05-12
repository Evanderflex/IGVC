import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='lslidar_gps_publisher',
            executable='gps_publisher_node',
            name='gps_publisher',
            output='screen'
        ),
    ])

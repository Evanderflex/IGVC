import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='robot_localization',
            executable='navsat_transform_node',
            name='navsat_transform',
            output='screen',
            parameters=[{
                'use_sim_time': False,
                'wait_for_datum': False,
                'frequency': 30.0,
                'magnetic_declination_radians': 0.0,
                'yaw_offset': 0.0,
                'zero_altitude': True,
               # 'broadcast_utm_transform': True,
                'broadcast_cartesian_transform': True,
                'publish_filtered_gps': True,
                'use_odometry_yaw': True,
                'wait_for_transform': True,
                'gps_topic': '/lslidar/gps',
                'imu_topic': '/camera/imu',  # Modify if using an IMU
                'odometry_topic': '/odometry/wheel',  # Modify if you have odometry data
                'world_frame': 'map',
                'utm_zone_service': 'utm_zone',
            }]
        ),
    ])

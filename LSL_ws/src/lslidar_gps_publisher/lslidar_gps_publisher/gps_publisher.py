import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix

class GPSPublisher(Node):
    def __init__(self):
        super().__init__('lslidar_gps_publisher')
        from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy

        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=10
        )

        self.publisher_ = self.create_publisher(NavSatFix, 'lslidar/gps', qos_profile)
        self.timer = self.create_timer(1.0, self.publish_gps_data)  # Publish every second

    def publish_gps_data(self):
        gps_msg = NavSatFix()
        gps_msg.header.stamp = self.get_clock().now().to_msg()
        gps_msg.header.frame_id = "gps_link"

        # Dummy GPS values (Replace with real data from LiDAR)
        gps_msg.latitude = 37.7749  # Example latitude
        gps_msg.longitude = -122.4194  # Example longitude
        gps_msg.altitude = 10.0  # Example altitude

        self.publisher_.publish(gps_msg)
        self.get_logger().info(f'Published GPS: {gps_msg.latitude}, {gps_msg.longitude}, {gps_msg.altitude}')

def main(args=None):
    rclpy.init(args=args)
    node = GPSPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

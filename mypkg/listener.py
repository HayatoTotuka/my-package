import rclpy
from rclpy.node import Node
from std_msgs.msg import String

rclpy.init()
node = Node("listener")


def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)


def main():
    pub = node.create_subscription(String, "chiba_weather", cb, 10)
    rclpy.spin(node)


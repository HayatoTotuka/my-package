#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Hayto Totuka
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ListenPositionNode(Node):
    def __init__(self):
        super().__init__('listener')
        self.sub = self.create_subscription(String,'chiba_weather',self.cb,10)
    def cb(self, msg):
        self.get_logger().info(f'{msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = ListenPositionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

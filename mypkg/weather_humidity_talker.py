#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 totuka hayato
# SPDX-License-Identifier: BSD-3-Clause

import os
import rclpy
from rclpy.node import Node
import requests
from std_msgs.msg import String

class WeatherTalker(Node):
    def __init__(self):
        super().__init__("WeatherTalker")
        self.pub = self.create_publisher(String, "chiba_weather", 10)
        self.create_timer(20.0, self.cb)
        self.api_key = os.getenv("WEATHER_KEY")
        self.city = "Chiba"
        self.unit = "metric"

    def fetch_weather(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city},jp&appid={self.api_key}&units={self.unit}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            return temperature, humidity
        except requests.exceptions.RequestException as e:
            return None, None

    def cb(self):
        temperature, humidity = self.fetch_weather()
        if temperature is not None and humidity is not None:
            msg = String()
            msg.data = f"気温: {temperature}°C, 湿度: {humidity}%"
            self.pub.publish(msg)


def main():
    rclpy.init()
    node = WeatherTalker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()


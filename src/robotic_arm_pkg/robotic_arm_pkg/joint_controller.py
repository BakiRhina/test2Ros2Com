import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import math

class jointController(Node):
    def __init__(self):
        super().__init__('robot_arm_controller')
        self.joint1_publisher = self.create_publisher(Float64, '/two_joint_arm/joint1_position_controller/command', 10)
        self.joint2_publisher = self.create_publisher(Float64, '/two_joint_arm/joint2_position_controller/command', 10)
        self.timer = self.create_timer(0.1, self.update_joint_positions)

        self.angle = 0.0

    def update_joint_positions(self):
        msg = Float64()
        msg.data = 1.0 * math.sin(self.angle)
        self.joint1_publisher.publish(msg)

        msg.data = 1.0 * math.sin(self.angle + math.pi / 2)
        self.joint2_publisher.publish(msg)

        self.angle += 0.01

def main(args=None):
    rclpy.init(args=args)
    robot_arm_controller = RobotArmController()
    rclpy.spin(robot_arm_controller)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

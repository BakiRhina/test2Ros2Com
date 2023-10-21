import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class JointProcessor(Node):

    def __init__(self):
        super().__init__('joint_processor')

        # Subscriber to read joint states
        self.subscription = self.create_subscription(
            JointState,
            'joint_states',
            self.joint_callback,
            10)

        # Publisher to send joint commands
        self.publisher_ = self.create_publisher(JointState, 'commanded_joint_states', 10)

    def joint_callback(self, msg):
        # For simplicity, if joint angle is > 0.5, set it to 0, otherwise set to 1
        if msg.position[0] > 0.5:
            new_position = 0.0
        else:
            new_position = 1.0

        # Construct a new JointState message
        commanded_joint_state = JointState()
        commanded_joint_state.name = ["joint1"]
        commanded_joint_state.position = [new_position]

        # Publish the new command
        self.publisher_.publish(commanded_joint_state)
        self.get_logger().info(f"Sent commanded position: {new_position}")

def main(args=None):
    rclpy.init(args=args)
    joint_processor = JointProcessor()
    rclpy.spin(joint_processor)
    joint_processor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

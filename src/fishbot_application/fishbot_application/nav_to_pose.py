from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator
import rclpy

def main():
    rclpy.init()
    nav = BasicNavigator() #节点
    nav.waitUntilNav2Active() #等待导航可用 
    
    goat_pose = PoseStamped()
    goat_pose.header.frame_id = "map"
    goat_pose.header.stamp = nav.get_clock().now().to_msg()
    goat_pose.pose.position.x = 2.0
    goat_pose.pose.position.y = 1.0
    goat_pose.pose.orientation.w = 1.0
    nav.goToPose(goat_pose)
    while not nav.isTaskComplete():
        feedback = nav.getFeedback()
        nav.get_logger().info(f'剩余距离：{feedback.distance_remaining}')
    result = nav.getResult()
    nav.get_logger().info(f'导航结果：{result}')


    
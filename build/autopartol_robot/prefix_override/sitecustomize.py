import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/calabash/ros2_test/chapt7/chapt7_ws/install/autopartol_robot'

import rclpy
from rclpy.node import Node
from autopartol_interfaces.srv import SpeechText
import espeakng

class Speaker(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.speech_service_ = self.create_service(SpeechText, 'speech_text', self.speech_text_callback)
        self.speaker_ = espeakng.Speaker()
        self.speaker_.voice = 'zh'
        self.get_logger().info('Speaker service is ready.')

    def speech_text_callback(self, request, response):
        text = request.text
        self.get_logger().info(f'正在准备朗读: "{text}"')
        self.speaker_.say(text)
        self.speaker_.wait()
        response.result = True
        return response
    
def main():
    rclpy.init()
    speaker_node = Speaker('speaker')
    rclpy.spin(speaker_node)
    rclpy.shutdown()
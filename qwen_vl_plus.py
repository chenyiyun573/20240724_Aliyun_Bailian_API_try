# Refer to the document for workspace information: https://help.aliyun.com/document_detail/2746874.html    
        
from dashscope import MultiModalConversation
from http import HTTPStatus
import dashscope
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the API key from environment variable
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

def simple_multimodal_conversation_call():
    """Simple single round multimodal conversation call.
    """
    messages = [
        {
            "role": "user",
            "content": [
                {"image": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"},
                {"text": "这是什么?"}
            ]
        }
    ]
    responses = MultiModalConversation.call(model='qwen-vl-plus',
                                           messages=messages,
                                           stream=True)
    for response in responses:
        print(response)


if __name__ == '__main__':
    simple_multimodal_conversation_call()
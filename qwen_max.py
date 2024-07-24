# Refer to the document for workspace information: https://help.aliyun.com/document_detail/2746874.html    
        
from http import HTTPStatus
import dashscope
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the API key from environment variable
dashscope.api_key = os.getenv('DASHSCOPE_API_KEY')

def call_with_stream():
    messages = [
        {'role': 'user', 'content': 'Introduce the capital of China'}]
    responses = dashscope.Generation.call("qwen-max",
                                messages=messages,
                                result_format='message',  # set the result to be "message"  format.
                                stream=True, # set streaming output
                                incremental_output=True  # get streaming output incrementally
                                )
    for response in responses:
        if response.status_code == HTTPStatus.OK:
            print(response.output.choices[0]['message']['content'],end='')
        else:
            print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message
            ))


if __name__ == '__main__':
        call_with_stream()
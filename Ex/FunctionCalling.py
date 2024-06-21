from openai import OpenAI
import json


client = OpenAI()

def get_current_weather():
    # Call API lấy thông tin thời tiết hiện tại theo địa điểm
    result = "response của API trả về"
    return result

def chat_api():
    messages = [{"role": "user", "content": "1 Câu hỏi"}]
    """
    tool, là func mình vừa tạo ở trên và gửi đi các thông tin cần thiết của func đó cho openAI
    bao gồm:    name - tên func
                description - Mô tả cho func đó
                parameters - Các tham số đầu vào
                    type - Kiểu dữ liệu của tham số đầu vào
                    properties - Các thuộc tính của tham số đầu vào
                    required - Những thuộc tính nào yêu cầu not null
    """
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["location"],
                },
            },
        }
    ]
    
    #Gửi request lần đầu cho openai
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    
    #Lấy ra tất cả các tools mà openAI cần sử dụng
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    
    #Nếu open có yêu cầu sử dụng tool
    if tool_calls:
        #Gán tất cả các func gửi đi vào biến available_functions
        available_functions = {
            "get_current_weather": get_current_weather,
        } 
        messages.append(response_message) 
       
        """
            Cho chạy từng tool mà openAI yêu cầu sử dụng
            1. Lấy funcName mà openAI yêu cầu sử dụng
            2. Lấy func đó ra từ available_functions
            3. Lấy tất cả các đối số cần truyền của openAI trả về
            4. chạy func đó
            5. thêm vào messages với nội dụng 
                tool_call_id: đã sử dụng tool id
                role: tool : đây là message của kết qua sau khi sử dụng tool
                name: tên func đã sử dụng
                content: response sau khi chạy func đó
        """
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(
                location=function_args.get("location"),
                unit=function_args.get("unit"),
            )
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )
        #Call tới openAI 1 lần nữa bao gồm message đã gửi ở lần 1 và thêm message mới thêm vào sau khi sử dụng tool
        second_response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=messages,
        )
        return second_response
    
    
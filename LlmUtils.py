import os

from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
print(f'api_key:{api_key[:15]}...')
client = OpenAI(api_key=api_key)

prompt_str = """
我正在使用自动化工具进行REST API的漏洞检测，具体来说，该自动化工具通过分析所测试平台的REST API文档（OPENAPI文档），自动生成测试序列并执行。

改自动化测试工具所生成的测试序列是一个python列表，例如：
[api_request_1, api_request_2, api_request_3, ...]

其中每一个api_request都是一个HTTP请求，其结构如下：
{
    "api_url": str格式的API路径,
    "api_method": HTTP请求方法,
    "api_request": 请求
    "api_response": self.api_response,
    "api_request_value": self.api_request_value,
    "api_response_value": self.api_response_value
}

需要你的帮助来纠正一个不完整的请求序列。以下是详细信息：

### 背景信息

- **项目背景：**
  该项目涉及[在此处插入项目背景信息]，我们正在使用RESTful API进行漏洞检测。

- **测试目标：**
  我们的目标是确保API的安全性和完整性，检测可能的漏洞。

### 当前问题

1. **原始测试请求序列：**
   ```
   [在此处插入原始的测试请求序列]
   ```
   - 该序列用于测试[在此处插入测试目的或功能]。

2. **错误请求的位置：**
   - 出错请求在序列中的位置为：[在此处插入位置]

3. **错误请求的响应信息：**
   ```
   [在此处插入错误请求的响应信息]
   ```
   - 错误信息显示：[在此处插入错误信息详细描述]

4. **相关API模板：**
   - **接口描述：** [在此处插入接口描述]
   - **请求参数：** [在此处插入请求参数信息]
   - **响应参数：** [在此处插入响应参数信息]
   - **其他相关信息：** [在此处插入其他相关信息，如认证方式、限制条件等]

### 任务说明

请根据以上信息，分析错误原因，并调整原始的测试请求序列。你可以通过以下方式进行修改：

- **新增请求：** 添加必要的请求以满足依赖关系或前置条件。
- **修改请求顺序：** 调整请求的执行顺序以避免错误。
- **修正参数：** 修改请求中的参数以符合API要求。
- **其他调整：** 任何其他你认为必要的调整。

### 输出要求

- **新的测试请求序列：**
  请给出完整的、经过修改的测试请求序列。
  
- **修改说明：**
  简要说明所做的修改及其原因，帮助理解调整的逻辑。

---

使用这个模板，将具体信息填入相应的位置，以便更全面地指导大语言模型进行分析和调整。
"""

prompt_template = [
    {"role": "user", "content": "What is the purpose of life?"},
    {"role": "assistant", "content": "The purpose of life is to be happy."},
    {"role": "user", "content": "So, how can I be happy?"}
]


def test_api():
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": "What is the purpose of life?"},
            {"role": "assistant", "content": "The purpose of life is to be happy."},
            {"role": "user", "content": "So, how can I be happy?"},
        ],
        max_tokens=100
    )

    usage = response.usage
    completion_tokens = usage.completion_tokens
    prompt_tokens = usage.prompt_tokens
    total_tokens = usage.total_tokens

    print(f'--- response ---\n'
          f'{response}\n'
          f'\n'
          f'--- prompt + completion = total tokens ---\n'
          f'{prompt_tokens} + {completion_tokens} = {total_tokens}\n'
          f'\n'
          f'--- response content ---\n'
          f'{response.choices[0].message.content}\n'
          f'{"=" * 90}\n')


def update_unfinished_test_seq(original_test_seq, stopped_api, stopped_api_index, stopped_api_response):
    new_test_seq = original_test_seq.copy()




if __name__ == '__main__':
    # pass
    test_api()


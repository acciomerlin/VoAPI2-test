import requests
import pprint

pp = pprint.PrettyPrinter(indent=2, depth=30, sort_dicts=False, compact=False, width=200)
ppp = pp.pprint
ppf = pp.pformat


def get_test_seq(seq):
    s = ""

    for i, req in enumerate(seq):
        s += (f"Request {i + 1}:\n"
              f"{ppf(req.get_api_object())}\n"
              f"{'-' * 40}\n")

    return s


def get_response_info(response):
    s = ""
    try:
        s += "Status Code: " + ppf(str(response.status_code)) + "\n"
        s += "Headers: " + ppf(str(response.headers)) + "\n"
        s += "Response Text: " + ppf(str(response.text)) + "\n"

        # 尝试打印 JSON 格式的响应
        try:
            s += "JSON Response: " + ppf(str(response.json())) + "\n"
        except ValueError:
            s += "Response is not in JSON format.\n"
    except Exception as e:
        s += " === An error occurred: " + str(e) + "===\n"

    return s
    # try:
    #     print("Status Code:", response.status_code)
    #     print("Headers:", response.headers)
    #     print("Response Text:", response.text)
    #
    #     # 尝试打印 JSON 格式的响应
    #     try:
    #         print("JSON Response:", response.json())
    #     except ValueError:
    #         print("Response is not in JSON format.")
    # except Exception as e:
    #     print("An error occurred:", str(e))

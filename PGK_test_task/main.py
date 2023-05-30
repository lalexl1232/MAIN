
from locations.dao import api_call

if __name__ == "__main__":
    response = api_call()

    import json
    with open('file.txt', 'w') as fw:
        # записываем
        json.dump(response, fw)

    # print(*response)
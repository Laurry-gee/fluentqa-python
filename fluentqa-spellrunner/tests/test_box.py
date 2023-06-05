import box


class DemoBox(box.Box):
    pass


def test_box_demo():
    import requests
    import json

    url = "https://app-api.cew-test.com/basis.uic.ProfileService/getCurrentProfile"

    payload = json.dumps({})
    headers = {
        'authority': 'app-api.cew-test.com',
        'accept': 'application/vrpc+json',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/vrpc+json',
        'cookie': 'NSID=kVJxw3bR7qNftW5GVuduaVBVf635dade; NSID_EXISTS=1',
        'origin': 'https://app.cew-test.com',
        'pragma': 'no-cache',
        'referer': 'https://app.cew-test.com/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'vrpc-client': 'fe.dubnium/0.2.83/84f770d4-596e-0e7f-a15d-4878991c9e61',
        'vrpc-id': 'CETJNCSJ7U9EZS8T.1684485784',
        'vrpc-version': '1.0.4-f.a-344c59c7'
    }

    print(json.dumps(headers))
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
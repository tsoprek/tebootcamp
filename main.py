#!/usr/bin/python
# coding : utf-8

import requests
import urllib3
import json
from lab_config import asa



urllib3.disable_warnings()


authorization = "Basic Y2lzY286Y2lzY29jaXNjbw=="
xAuthToken = ""
headers = {'Content-Type': "application/json", 'Authorization': authorization, 'X-Auth-Token': xAuthToken, 'User-Agent': 'REST API Agent'}
ip = asa
URL = 'https://' + ip
print(ip)

# API to Generate X-Auth-Token
def get_X_auth_token(ip):
    token = None
    username = 'cisco'
    password = 'ciscocisco'
    #Directory of the ASA Tokenservice
    url = 'https://'+ username + ':' + password + '@' + ip + '/api/tokenservices'
    headers = {'Content-Type':'application/json', 'Authorization': authorization, 'User-Agent': 'REST API Agent'}
    payload = ""
    # Send POST Request to ASA, containing Username and Password in URL, empty payload, JSON Header. It doesn't verify SSL Cetificate!
    r = requests.request("POST", url, data=json.dumps(payload), headers=headers, verify=False)
    #Check if response got received, if not print an error message
    if(not r):
        print("No Data returned")
    #Search for the token in the header and stores the value.
    else:
        token = r.headers['x-auth-token']
    return token


# API to Delete X-Auth-Token
def del_X_auth_token(ip, token):
    token = token
    username = 'cisco'
    password = 'ciscocisco'
    #Directory of the ASA Tokenservice
    url = 'https://'+ username + ':' + password + '@' + ip + '/api/tokenservices/'+token
    headers = {'Content-Type': "application/json", 'Authorization':authorization, 'X-Auth-Token':token,'User-Agent': 'REST API Agent'}
    # Send DELETE Request to ASA, containing Username and Password in URL, empty payload, JSON Header. It doesn't verify SSL Cetificate!
    r = requests.delete(url, headers=headers, verify=False)
    #Check if response got received, if not print an error message
    if(not r):
        print("No Data returned")
    #Search for the token in the header and stores the value.
    else:
        if r.status_code==204:
           print('X-Auth-Token status: Removed successfully.')
        else:
            print('X-Auth-Token status:'+ str(r.status_code))

#Get all standard IN ACLs from ASA
def get_acl_in(ip, token):
    data_json = None
    token = token
    url = 'https://' + ip + '/api/objects/extendedacls/GLOBAL/aces'
    headers = {'Content-Type': "application/json", 'Authorization': authorization, 'X-Auth-Token': token,'User-Agent': 'REST API Agent'}
    r = requests.get(url, headers=headers, verify=False)
    if(not r):
        print("No Data returned")
    else:
        data_json = r.json()
        return data_json

#Creates an extended ACL on ASA, needs an Token, IP-Address, a Name and the rule in JSON-Format
# def add_ext_acl(ip, aclName, rule ):
#     data_json = None
#     #API-URL to add extended ACL Objects
#     url = 'https://'+ip+'/api/objects/extendedacls/'+aclName+'/aces'
#     #Make a POST request to ASA API
#     r = requests.request("POST", url, data=rule, headers=authentication.Header, verify=False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

if __name__ == '__main__':
    xAuthToken = get_X_auth_token(ip)
    print(xAuthToken)
    data = get_acl_in(ip, xAuthToken)
    print(data)
    del_X_auth_token(ip, xAuthToken)

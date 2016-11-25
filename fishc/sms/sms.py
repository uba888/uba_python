#!/usr/bin/env python
#encoding=utf-8

import time
import base64
import hashlib
import httplib
import uuid
import hmac

class SMSClient:
    def __init__(self, app_key, app_secret):
        self.__app_key, self.__app_secret = app_key, app_secret

    def send(self, receiver, sign, template_code, parameters=''):
        print receiver, sign, template_code, parameters
        self.__host = 'sms.market.alicloudapi.com'
        self.__str_uri = '/singleSendSms?ParamString=%s&RecNum=%s&SignName=%s&TemplateCode=%s' % (parameters, receiver, sign, template_code)
        print self.__str_uri
        self.build_headers()
        self.__connection = httplib.HTTPConnection(self.__host, 80)
        self.__connection.connect()
        self.__connection.request('GET', self.__str_uri, headers=self.__headers)
        response = self.__connection.getresponse()
        print response.status, response.getheaders(), response.read()

    def build_headers(self):
        headers = dict()
        headers['X-Ca-Key'] = self.__app_key
        headers['X-Ca-Nonce'] = str(uuid.uuid4())
        headers['X-Ca-Timestamp'] = str(int(time.time() * 1000))
        headers['X-Ca-Signature-Headers'] = 'X-Ca-Key,X-Ca-Nonce,X-Ca-Timestamp'
        str_header = '\n'.join('%s:%s' % (k, headers[k]) for k in ['X-Ca-Key','X-Ca-Nonce','X-Ca-Timestamp'])
        str_to_sign = '%s\n\n\n\n\n%s\n%s' % ('GET', str_header, self.__str_uri)
        headers['X-Ca-Signature'] = self.__get_sign(str_to_sign, self.__app_secret)
        self.__headers = headers

    def __get_sign(self, source, secret):
        h = hmac.new(secret, source, hashlib.sha256)
        signature = base64.encodestring(h.digest()).strip()
        return signature

cli = SMSClient(app_key="23472464", app_secret="af81a5c0c398a679d0a302dab59f0b3d")
cli.send('18657173220', 'EC82B6214DAFD1BB58F5BDF8B7623F7A', 'SMS_16820035', '{"content":"test"}')

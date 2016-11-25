#!/usr/bin/env bash

RECEIVER=18657173220      #接收方手机号
SIGN="监控报警"            #签名
TEMP_CODE="SMS_16820035"      #短信模板
PARAMS="{\"content\":\"`date +%Y%m%d%H%M%S`\"}" #模板参数（json格式）

K="23472464" #AppKey，从管理控制台获取，下同
S="af81a5c0c398a679d0a302dab59f0b3d" #AppSecret

NL="
"
[ "x`uname`" = "xDarwin" ] && {
NONCE="`uuidgen`"
TIMESTAMP="`date +%s`500"
} || {
NONCE="`uuid`"
TIMESTAMP="`date +%s%3N`"
}
STR_HEADER="X-Ca-Key:$K${NL}X-Ca-Nonce:$NONCE${NL}X-Ca-Timestamp:$TIMESTAMP"
STR_URI="/singleSendSms?ParamString=$PARAMS&RecNum=$RECEIVER&SignName=$SIGN&TemplateCode=$TEMP_CODE"
STR_TO_SIGN="GET${NL}${NL}${NL}${NL}${NL}$STR_HEADER${NL}$STR_URI"
SIGN="`/bin/echo -n "$STR_TO_SIGN" | openssl dgst -sha256 -hmac "$S" | sed 's/.* //g' | xxd -r -p | base64`"
STR_URI="`echo "$STR_URI" | sed 's#{#\\\\{#g;s#}#\\\\}#g'`"
curl -v -H 'Accept:' \
    -H "X-Ca-Key: $K" \
    -H "X-Ca-Nonce: $NONCE" \
    -H "X-Ca-Timestamp: $TIMESTAMP" \
    -H "X-Ca-Signature-Headers: X-Ca-Key,X-Ca-Nonce,X-Ca-Timestamp" \
    -H "X-Ca-Signature: $SIGN" \
    "http://sms.market.alicloudapi.com$STR_URI"

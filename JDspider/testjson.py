import json
import re

str1 = 'fetchJSON_comment98({"productAttr":null,"productCommentSummary":{"skuId":100002004455,"averageScore":5,"defaultGoodCount":0,"defaultGoodCountStr":"5万"});'

result = re.match("(fetchJSON_comment98\()(.*)(\);)", str1)

print(result.group(0))
print(result.group(1))
print(result.group(2))
print(result.group(3))
print(result.group(4))
print(result.group(5))

jsonStr = result.group(2)
print(jsonStr)

jsonObj = json.loads(jsonStr)
print(type(jsonObj))
print(jsonObj.keys())
print(jsonObj["productCommentSummary"]["defaultGoodCountStr"])

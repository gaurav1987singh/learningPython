import urllib2
import base64
conf_serverurl = "https://testg0ldy.atlassian.net/wiki"
username = "gaurav_singhnegi@yahoo.com"
password = "G01dy#1987"
stringToEncode = username + ":" + password
print stringToEncode
encodedString = base64.b64encode(stringToEncode)
url = conf_serverurl + "/rest/api/content?os_username=" + username + "&amp;os_password=" + password
data = '{"type":"page","ancestors":[{"type":"page","id":1048583}],"title":"my new page",' \
       '"space":{"key":"MYS"},' \
       '"body":{"storage":{"value":"&lt;p&gt;This is a new page created from api&lt;/p&gt;",' \
       '"representation":"storage"}}}'

headers = {'Authentication': 'Basic ' + encodedString, 'Content-type': 'application/json',
           'Accept': 'application/json',
           'X-Atlassian-Token': 'no-check'}
req = urllib2.Request(url, data, headers=headers)
try:
    response = urllib2.urlopen(req)
    data = response.read()
except urllib2.HTTPError, error:
    data = error.read()
print data

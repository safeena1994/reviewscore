import urllib2
import json
import unirest
business_id='aCkAmpBmEJCeRBJ5_Q2D-Q'
response=urllib2.urlopen("http://localhost:9200/yelp/_search?q=business_id:"+business_id).read()
response_dict=json.loads(response)
rating=0.0
count=1
neg=0.0
pos=0.0
for x in response_dict["hits"]["hits"]:
	#print x["_source"]["text"]
	input={"txt":x["_source"]["text"]}
	api_response = unirest.post("https://community-sentiment.p.mashape.com/text/",headers={
    "X-Mashape-Key": "c2Ct8oapPKmsh1mCqyhVsbOCe16mp1MQrT1jsnPnfTYg0rnAnA",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  },
  params=input
)

	if api_response.body["result"]["sentiment"]=='Negative':
		rating=rating-(float(str(api_response.body["result"]["confidence"]))/100)
		neg=neg+(float(str(api_response.body["result"]["confidence"]))/100)
		if rating<0.0:
			rating=0.0
	else:
		rating=rating+(float(str(api_response.body["result"]["confidence"]))/100)
		pos=pos+(float(str(api_response.body["result"]["confidence"]))/100)
	print "processing review number-",count,"         current rating=",rating
	count=count+1

print "The final rating of business ",business_id," is=",rating
print "neg=",neg
print"pos=",pos
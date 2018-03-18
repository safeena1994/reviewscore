import urllib2
import json
import unirest
response=urllib2.urlopen("http://localhost:9200/yelp/_search?pretty=true&q=*:*&size=10000").read()
response_dict=json.loads(response)
rating=0.0
count=1

failed=0

folder_path_pos='/home/abhiswetha/nltk_data/corpora/yelp/pos'
folder_path_neg='/home/abhiswetha/nltk_data/corpora/yelp/neg'
for x in response_dict["hits"]["hits"]:
	try:
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
			f = open(folder_path_neg+"/"+x["_source"]["review_id"]+".txt",'w')
			f.write(x["_source"]["text"])
			f.close()
			
		else:
			f = open(folder_path_pos+"/"+x["_source"]["review_id"]+".txt",'w')
			f.write(x["_source"]["text"])
			f.close()
		print "processing-",count,"      failed-",failed
		count=count+1
	except Exception,ex:
		print ex
		failed=failed+1


	

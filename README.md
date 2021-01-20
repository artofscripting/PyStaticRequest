# PyStaticRequest
Request Limiter for URL's 

## import PyStaticRequest

## To create or load data from a URL 
sr = staticRequest.staticRequest("http://artofscripting.com")

## Deletes local content and reloads data
sr.updateRequest()

## Using data loaded. 
print(sr.text)

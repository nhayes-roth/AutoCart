# import statements
import cookielib
import urllib
import urllib2
import webbrowser
import requests

# important variables
user_email 			= 'pantry@liketwice.com'
user_password 		= 'twice123'
authentication_url	= 'https://www.instacart.com/accounts/login'
spreadhseet_url		= 'https://docs.google.com/spreadsheet/ccc?key=0AofjsFst2vbidGdGNGFtM2VqTDExZWhJb2g5Nm1KUEE&usp=sharing'

# store cookies and create an opener that will hold them
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

# Install our opener
urllib2.install_opener(opener)

# Input parameters we are going to send
payload = {
	'user[source]': 'web',
	'user[email]': user_email,
	'user[password]': user_password
  }

# Use urllib to encode the payload
data = urllib.urlencode(payload)

# Build our Request object (supplying 'data' makes it a POST)
req = urllib2.Request(authentication_url, data)

# Make the request and read the response
resp = urllib2.urlopen(req)
contents = resp.read()		# contains the html after loggin into instacart

# save html to file
Html_file = open("instacart_html", "w")
Html_file.write(contents)
Html_file.close()

# did we make it?
print "success"
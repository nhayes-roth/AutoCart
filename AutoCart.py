# import statements
import cookielib
import urllib
import urllib2
import webbrowser
import mechanize
import requests

# important variables
user_email 			= 'pantry@liketwice.com'
user_password 		= 'twice123'
authentication_url	= 'https://www.instacart.com/accounts/login'
search_url			= 'https://www.instacart.com/store?#safeway/search/'
put_prefix 			= 'https://www.instacart.com/api/v2/cart/cart_items/'
put_suffix			= '?cart_id=135798&token=pThYyJBaysCdCJWs1cuJ&source=web&warehouse_id=1&zone_id=1'
item_id 			= '42078'
orders_filename		= 'orders.txt'

# log into the site
browser = mechanize.Browser()
browser.open(authentication_url)
browser.select_form(nr = 0)
browser.form['user[email]'] = user_email
browser.form['user[password]'] = user_password
response = browser.submit()

# save html to file
Html_file = open("instacart_html", "w")
Html_file.write(response.read())
Html_file.close()	

##### try to imitate a single PUT request
# request parameters
parameters = {	'qty' : '1', 'created_at' :'1393287110.459'}
csrf_token = 'ZqHb0C+OBQTHT3y0gTCL9XajoRRpGmQgHvzXHPRnhjg'
header = {'Referrer' : authentication_url, 'X-CSRF-Token' : csrf_token}
cookie = browser._ua_handlers['_cookies'].cookiejar

cookie_dict = dict([(c.name, c.value) for c in list(cookie)])

print
print cookie_dict
print

# submit the form
r = requests.put(put_prefix+item_id+put_suffix, params=parameters, cookies=cookie_dict, headers=header)
print
print r.content
print

# iterate through the orders
with open(orders_filename) as f:
	for line in f:
		item_name = line[:-2]
		item_count = int(line[-2:])
		# follow the link to the appropriate search url
		browser.open(search_url + item_name)

		##### try to imitate a single PUT request
		# TODO move put request here
		
		# click the add to cart button
		# print "ITEM URL: ", browser.geturl()
		# for link in browser.links():
		# 	print link.text, link.url
		# click the plus button as many times as is necessary


# # Find all links in the page
# for link in browser.links():
# 	print link.text, link.url

# # Find all forms in the page
# for form in browser.forms():
# 	print "Form name: ", form.name
# 	print form

# did we make it?
print "success"
# import statements
import cookielib
import urllib
import urllib2
import webbrowser
import mechanize
import re

# important variables
user_email 			= 'pantry@liketwice.com'
user_password 		= 'twice123'
authentication_url	= 'https://www.instacart.com/accounts/login'
search_url			= 'https://www.instacart.com/store?#safeway/search/'
spreadhseet_url		= 'https://docs.google.com/spreadsheet/ccc?key=0AofjsFst2vbidGdGNGFtM2VqTDExZWhJb2g5Nm1KUEE&usp=sharing'
orders_filename		= 'orders.txt'

# log into the site
browser = mechanize.Browser()
browser.open(authentication_url)
browser.select_form(nr = 0)
browser.form['user[email]'] = user_email
browser.form['user[password]'] = user_password
response = browser.submit()

# iterate through the orders,
with open(orders_filename) as f:
	for line in f:
		item_name = line[:-2]
		item_count = int(line[-2:])
		# follow the link to the appropriate search url
		print "Item name: ", item_name
		print "Item count: ", item_count
		browser.open(search_url + item_name)
		print "URL", browser.geturl()
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

# save html to file
Html_file = open("instacart_html", "w")
Html_file.write(response.read())
Html_file.close()

# did we make it?
print "success"
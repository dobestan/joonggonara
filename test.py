import mechanize

file = open("result.html", "w")

browser = mechanize.Browser()
cj = mechanize.CookieJar()
browser.set_cookiejar(cj)

browser.set_handle_robots(False)
browser.open("https://nid.naver.com/nidlogin.login")
browser.select_form(nr=0)
browser.form['id'] = "appcando"
browser.form['pw'] = "asc379749"
browser.submit()

browser.open("http://me.naver.com/index.nhn")
file.write(browser.response().read())

from selenium import webdriver

	user = "hehehe@gmail.com";
	pwd = "12345"
	driver = webdriver.Firefox()
	driver.get("http://automationpractice.com/index.php?controller=authentication&amp;back=my-account")
	elem = driver.find_element_by_id("email")
	elem.send_keys(user)
	elem = driver.find_element_by_id("passwd")
	elem.send_keys(pwd)
	driver.find_element_by_id("SubmitLogin").click()
	driver.close()
from selenium import webdriver
from time import sleep

for i in range(50):
	my_blog = 'https://livenowisgood.blogspot.com/2019/12/soft-purity-lavera.html'
	driver = webdriver.Chrome('./chromedriver')
	driver.get(my_blog)
	driver.quit()
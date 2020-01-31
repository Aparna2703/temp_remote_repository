import  requests
r=requests.get("http://127.0.0.1:2345/employee/")

with open("",'wb') as f:
    f.write(r.content)
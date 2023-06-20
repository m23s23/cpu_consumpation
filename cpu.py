import matplotlib .pyplot as plt
import psutil as p
app_name_dict={}

count=0
for process in p.process_iter():
    count=count+1
    if count<=6:
        name=process.name()
        cpu_usage=p.cpu_percent()
        print("name: ",name," cpu usage: ",cpu_usage)
        app_name_dict.update({name:cpu_usage})

keymax=max(app_name_dict,key=app_name_dict.get)  
keymin=min(app_name_dict,key=app_name_dict.get)   
name_list=[keymax,keymin]   

app=app_name_dict.values()
max_app=max(app)
min_app=min(app)
app_list=[max_app,min_app]

plt.figure(figsize=(15,7))
plt.xlabel("minimum maximum cpu consumpation")

plt.ylabel("usage")
plt.bar(name_list,app_list,width=0.5,color=("blue","purple"))
plt.show()
        
d= [{"name":"komal","score":40,"school":"pyds"},{"name":"koma","score":40,"school":"pyd"},{"name":"jaya","score":60,"school":"pyds"},{"name":"Sonam","score":60,"school":"Union"},{"name":"Akshit","score":50,"school":"Summer Fileld school"}]
dic={}
for i in range(len(d)):
    
    dic[i]=d[i]       
    if d[i]["school"]=="pyds" and d[i]["score"]>=50:
            print(d[i])

        
    
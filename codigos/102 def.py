def fatorial(n):
    ft=1
    for i in range(n,0,-1):           
        ft*=i
    return ft
            
#main 
print(fatorial(4))
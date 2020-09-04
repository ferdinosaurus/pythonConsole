
data = [7,8,9,5,6,4,2,3,1]
print(f"before sort : {data}")
for i in range (0,len(data)):
    for j in range(0,len(data)):
        if(data[i]<data[j]):
            temp = data[i]
            data[i] = data[j]
            data[j] = temp

print(f"after sort : {data}")

jina="python exception"

for j in jina:
    if (j!=1):
        print(j)

x=["Python","try and except","execption"]
try:
    for i in range(3):
        print(f"The index and element from list is {i,x[i]}")
except:
    print("Index out of range")
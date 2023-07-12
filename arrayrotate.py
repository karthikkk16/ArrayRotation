def reverseForArrayRotation(arr,i,j):
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

arr=list(map(int,input().split()))
k=int(input())
k=k%len(arr)
reverseForArrayRotation(arr,0,len(arr)-1)
reverseForArrayRotation(arr,0,k-1)
reverseForArrayRotation(arr,k,len(arr)-1)
print(arr) 
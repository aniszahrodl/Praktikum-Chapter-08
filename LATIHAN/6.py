def sortStringByChar():
    List=[]
    for i in range(len(myList)):
        a= set(myList[i])
        b= str(len(a))
        List.append(b+myList[i])
        List.sort()
        List.sort(reverse=True)
    print(List)
    

      
myList=['apel','rambutan','jeruk']
sortStringByChar()

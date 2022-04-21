def swapFileData() :
    file1=input("ENTER THE NAME OF YOUR ORIGNAL FILE")
    file2=input("ENTER THE NAME OF THE FILE YOU WANT TO SWITCH")
    
    with open (file1,'r') as a:
        data_a=a.read()
        
    with open (file2,'r') as b:
        data_b=b.read()
        
        
    with open(file1,'w') as a:
        a.write(data_b)
    
    with open(file2,'w') as b:
        b.write(data_a)
        
swapFileData()

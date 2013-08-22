def makeemails(n):
    for i in range(n):
        with open("emaillist.txt", "a") as f:
            f.writelines("\n"+"lisasailthru"+str(i+1)+"@mailinator.com")

makeemails(140000)

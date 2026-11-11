Student1={"name":"Nathan","age":15,"ethnicity":"Indian","grade":10,"room":17}
flag=1
while flag==1:
    userinput=(input("Enter if you would like to know Student1's name, age, ethnicity, grade, room :"))
    if userinput=="exit":
        flag=0
        break
    else:
        print(Student1[userinput])

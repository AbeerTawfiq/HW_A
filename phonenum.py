
name_num={"lama":772213456,"mohameed":712345671,"ahmed":732457768}

def add():
    addname=input("add name:")
    addnum=input("add number:")
    name_num[addname]=addnum # type: ignore


def update():
    up=input("enter the name you want change his or her number:")
    upp=input("enter new number:")
    int(upp)
    name_num.update({up:upp}) # type: ignore


def delete():
    Deletename=input("enter the name you want delete it:")
    name_num(Deletename) # type: ignore



def view():
    print(name_num)

listop=["1-add","2-updat","3-delete","4-view"]
print(f"{listop[0]}\n{listop[1]}\n{listop[2]}\n{listop[3]}")

canedit=0

while   canedit<=3:
    canedit+=1
    userinfo=input("enter number the option or the option:")

    if  "add"== userinfo or "1" == userinfo:
        add()
        print (name_num)
    else:
        print("")
    if  "updat" == userinfo or "2" == userinfo :
        update()
        print(name_num)
    elif "delete" == userinfo or "3" == userinfo:
        delete()   
        print(name_num)
    elif "view" == userinfo or "4" == userinfo:
        view()
        print(name_num)
    
 
    else:
        print(f" error {userinfo} out option")


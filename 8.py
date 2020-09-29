from PIL import Image,ImageOps
def is_int(a):
    try:
        int(a)
        return(True)
    except ValueError:
        return(False)
def dsl():
    print("Please Choose:")
    print("1-Insert new pic")
    print("2-Export new file")
    print("3-Edit")
    print("4-rotate")
    print("5-resize")
    print("6-crop")
    print("7-Exit")
    a=input()
    if is_int(a)==True:
        while is_int(a)==True and ((int(a)<1 or int(a)>7)):
            print("Error: Invaild Input, try again ..."+"\n")
            print("Please Choose:")
            print("1-Insert new pic")
            print("2-Export new file")
            print("3-Edit")
            print("4-rotate")
            print("5-resize")
            print("6-crop")
            print("7-Exit")
            a=(input())
    else:
        while is_int(a)==False:
            print("Error: Invaild Input, try again ..."+"\n")
            print("Please Choose:")
            print("1-Insert new pic")
            print("2-Export new file")
            print("3-Edit")
            print("4-rotate")
            print("5-resize")
            print("6-crop")
            print("7-Exit")
            a=(input())
            while is_int(a)==True and ((int(a)<1 or int(a)>7)):
                print("Error: Invaild Input, try again ..."+"\n")
                print("Please Choose:")
                print("1-Insert new pic")
                print("2-Export new file")
                print("3-Edit")
                print("4-rotate")
                print("5-resize")
                print("6-crop")
                print("7-Exit")
                a=(input())
    return(a)
def b1(b):
    lms=True
    print("Insert new pic: Please Insert Pic Address")
    c=input()
    if (c[0]+c[1]+c[2])=="-nr":
        im=(c[4::])
        img=Image.open(im)
        return img
    if (c[0]+c[1])=="-r":
        im=(c[3::])
        img=Image.open(im)
        return img
    while c=="back":
        b=dsl()
        while lms:
            while int(b)==1:
                h=b1(b)
                b=dsl()
            while int(b)==3:
                b3(h,b)
                b=dsl()
            while int(b)==2:
                b2(h,b)
                b=dsl()
            if int(b)==4:
                lms=False
def b3(h,b):
    print("Edit: Please Choose"+"\n"+"1. Grayscale"+"\n"+"2. Black and white"+"\n"+"3. Negative")
    c=input()
    while int(c)>3 or int(c)<1:
        print("Error: Invaild Input, try again ..."+"\n")
        c=input()
    if int(c)==1:
        h=h.convert("LA")
        h.show()
        return (h)
    if int(c)==2:
        q=h.convert("L")
        h=q.point(lambda x:0 if x<128 else 255,"1")
        h.show()
        return (h)
    if int(c)==3:
        im_invert = ImageOps.invert(h)
        im_invert.show()
        return (im_invert)
def b2(h,b):
    print("Insert the name of new file: Please Insert The name")
    m=input()
    h.save(m)
def b4(h):
    print("Please Insert The number of rotate")
    u=input()
    while is_int(u)==False:
        print("Error: Invaild Input, try again ..."+"\n")
        print("Please Insert The number of rotate")
        u=input()
    else:
        h=h.rotate(int(u))
        h.show()
        return(h) 
def b5(h):
    print("Please Insert X Number That You Want")
    l=input()
    while is_int(l)==False:
        print("Error: Invaild Input, try again ..."+"\n")
        print("Please Insert X Number That You Want")
        l=input()
    if is_int(l)==True:
        print("Please Insert Y Number That You Want")
        k=input()
        while is_int(l)==False:
            print("Error: Invaild Input, try again ..."+"\n")
            print("Please Insert Y Number That You Want")
            k=input()
        if is_int(k)==True:
            h=h.resize((int(l),int(k)))
            h.show()
            return(h)
def b6(h):
    print("Please Insert The Length OF The Dots Up Left")
    s=input()
    while is_int(s)==False:
        print("Error: Invaild Input, try again ..."+"\n")
        print("Please Insert The Length OF The Dots Up Left")
        s=input()
    if is_int(s)==True:
        print("Please Insert The Width OF The Dots Up Left")
        f=input()
        while is_int(f)==False:
            print("Error: Invaild Input, try again ..."+"\n")
            print("Please Insert The Width OF The Dots Up Left")
            f=input()
        if is_int(f)==True:
            print("Please Insert The Length Size")
            q=input()
            while is_int(q)==False:
                print("Error: Invaild Input, try again ..."+"\n")
                print("Please Insert The Length Size")
                q=input()
            if is_int(q)==True:
                print("Please Insert The Width Size")
                z=input()
                while is_int(z)==False:
                    print("Error: Invaild Input, try again ..."+"\n")
                    print("Please Insert The Width Size")
                    z=input()
                if is_int(z)==True:
                    h=h.crop((int(s),int(f),int(q),int(z)))
                    h.show()
                    return(h)        
h=None
lms=True
b=dsl()
while lms:
    while int(b)==1:
        h=b1(b)
        b=dsl()
    while int(b)==3:
        h=b3(h,b)
        b=dsl()
    while int(b)==2:
        b2(h,b)
        b=dsl()
    while int(b)==4:
        h=b4(h)
        b=dsl()
    while int(b)==5:
        h=b5(h)
        b=dsl()
    while int(b)==6:
        h=b6(h)
        b=dsl()
    if int(b)==7:
        lms=False
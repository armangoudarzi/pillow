from PIL import Image,ImageOps
def is_int(a):
    try:
        int(a)
        return(True)
    except ValueError:
        return(False)
def main_menu():
    _input_=input()
    _list_=_input_.split()
    return(_list_)
def insert_menu(_input_):
    img=Image.open(_input_[0])
    return img
def edit_menu(img,_input_):
    if len(_input_)>=3 and _input_[2]=="grayscale":
        img=img.convert("LA")
        img.show()
        if len(_input_)==4:
            img.save(_input_[3])
        return (img)
        
    if len(_input_)>=3 and _input_[2]=="black-and-white" :
        q=img.convert("L")
        img=q.point(lambda x:0 if x<128 else 255,"1")
        img.show()
        if len(_input_)==4:
            img.save(_input_[3])
        return (img)
    if len(_input_)>=3 and _input_[2]=="negative":
        img = ImageOps.invert(img)
        img.show()
        if len(_input_)==4:
            img.save(_input_[3])
        return (img)
    if len(_input_)>=3 and _input_[2]=="good-effect":
        img=img.convert("1")
        img.show()
        if len(_input_)==4:
            img.save(_input_[3])
        return(img)
def rotate_menu(img,_input_):
    if is_int(_input_[2])==True:
        img=img.rotate(int(_input_[2]))
        img.show()
        if len(_input_)==4:
            img.save(_input_[3])
        return(img)
    else:
        print("Error: please insert a vaild input ...")       
def resize_menu(img,_input_):
    _list_=_input_[2].split(",")
    if len(_list_)==2 and is_int(_list_[0])==True and is_int(_list_[1])==True:
        x=int(_list_[0])
        y=int(_list_[1])
        img=img.resize((x,y))
        img.show()
        if len(_input_)==4:
            img.save(_input_[3])
        return (img)
    else:
        print("Error: please insert a vaild input ...")        
def crop_menu(img,_input_):
    information=_input_[2].split(",")
    if len(information)==4 and is_int(information[0])==True and is_int(information[1])==True and is_int(information[2])==True and is_int(information[3])==True:
        img=img.crop((int(information[0]),int(information[1]),int(information[2]),int(information[3])))
        img.show()
        if len(_input_)==4:
            img.save(_input_[3])
        return(img)
    else:
        print("Error: please insert a vaild input ...")
def Horizontally_Flipped(img,_input_):
    img=img.transpose(Image.FLIP_LEFT_RIGHT)
    img.show()
    if len(_input_)==3:
        img.save(_input_[2])
    return img
def Vertically_Flipped(img,_input_):
    img=img.transpose(Image.FLIP_TOP_BOTTOM)
    img.show()
    if len(_input_)==3:
        img.save(_input_[2])
    return img
    
import functions
from PIL import Image,ImageOps
img=None
user_exit=True
_input_=functions.main_menu()
while user_exit:
    while _input_[0]!="exit":
        img=functions.insert_menu(_input_) 
        while 4>=len(_input_)>=3 and _input_[1]=="edit":
            img=functions.edit_menu(img,_input_)
            _input_=functions.main_menu()
            if _input_[0]=="exit":
                print("Thanks for using my code")
                user_exit=False
        while 4>=len(_input_)>=3 and _input_[1]=="rotate":
            img=functions.rotate_menu(img,_input_)
            _input_=functions.main_menu()
            if _input_[0]=="exit":
                print("Thanks for using my code")
                user_exit=False    
        while 4>=len(_input_)>=3 and _input_[1]=="resize":
            img=functions.resize_menu(img,_input_)
            _input_=functions.main_menu()
            if _input_[0]=="exit":
                print("Thanks for using my code")
                user_exit=False
        while 4>=len(_input_)>=3 and _input_[1]=="crop":
            img=functions.crop_menu(img,_input_)
            _input_=functions.main_menu()
            if _input_[0]=="exit":
                print("Thanks for using my code")
                user_exit=False
        while 3>=len(_input_)>=2 and _input_[1]=="Horizontally_Flipped":
            img=functions.Horizontally_Flipped(img,_input_)
            _input_=functions.main_menu()
            if _input_[0]=="exit":
                print("Thanks for using my code")
                user_exit=False
        while 3>=len(_input_)>=2 and _input_[1]=="Vertically_Flipped":
            img=functions.Vertically_Flipped(img,_input_)
            _input_=functions.main_menu()
            if _input_[0]=="exit":
                print("Thanks for using my code")
                user_exit=False

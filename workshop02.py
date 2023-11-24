import random

def guess_numder():
    
    secret_number = random.randint(1, 100)
    print('-------------------------------------')
    print(' ทายตัวเลขที่มีค่าอยู่ที่ 1 -100 กันเถอะ')
    while True:
        try:
            
            user_guess = int(input("ป้อนตัวเลขที่ต้องการ :"))
            
            if user_guess == secret_number :
                 print('-------------------------------------')
                 print('คูณท้ายถูก')
                 break
            elif user_guess < secret_number :
                print('-------------------------------------')
                print('คูณท้ายผิด ตัวเลขน้อยไป :')
            else:
                print('-------------------------------------')
                print('คูณท้ายผิด ตัวเลขมากไป')
        except ValueError:
            print('-------------------------------------')
            print('ฌปรดป้นตัวเลขที่ถูกต้อง')
            
if __name__ == "__main__":
    guess_numder()
    print('-------------------------------------')
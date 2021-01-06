import utilities as ut

# --------------- MAIN MENU ---------------
def main_menu():
    ut.figlet()
    print("1) PDF'leri birleştir")
    print("\n0) Çıkış\n")

    user_num = input("Lütfen seçiniz:")

    if user_num == "1":
        pass
    elif user_num == "0":
        ut.quit()
    else:
        pass
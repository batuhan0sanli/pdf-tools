import time
import utilities as ut
import modules.mergePDF as modPDF

# --------------- MAIN MENU ---------------
def main_menu():
    ut.figlet()
    print("1) PDF'leri birleştir")
    print("\n0) Çıkış\n")

    user_num = input("Lütfen seçiniz:")

    if user_num == "1":
        mergePdf_menu()
    elif user_num == "0":
        ut.quit()
    else:
        pass
    return None

# --------------- Merge PDF ---------------
def mergePdf_menu():
    ut.figlet()
    print("Dosyanızı sürükleyin ve ENTER'a basın.")
    fileNames = []
    fileNames.append(input(""))

    while True:
        ut.figlet()
        print("Dosyanız eklendi.")
        print("Bir başka dosya eklemek için sürükleyin ve ENTER'a basın.")
        print("Başka dosya eklemek istemiyorsanız ENTER'a basın.")
        user_sel = input("")
        if user_sel == "":
            break
        else:
            fileNames.append(user_sel)
    modPDF.mergePdf(fileNames,"cikti.pdf")
    print("İşlem Tamam. Dosyanız proje dizinine kaydedildi.\nAna ekrana dönülüyor.")
    time.sleep(3)
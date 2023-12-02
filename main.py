import tkinter
from PIL import Image, ImageTk
import cryptocode
from tkinter import messagebox
from tkinter import END


window = tkinter.Tk()
window.title("Secret Notes")
window.minsize(width=200, height=500)
window.config(padx=20, pady=20)

try:
   with open("sifre.txt", "r") as dosya:
      print("Sifre dosyası bulundu")
except FileNotFoundError:
   with open("sifre.txt","w") as dosya:
      print("Şifre dosyası oluşturuldu")

def encrypt_button():

   entryTitle = entry_title.get()
   es = entry_secret.get("1.0", 'end-1c')
   entryPass = entry_sifre.get()

   if entryTitle == "" or es == "" or entryPass == "":
      return messagebox.showinfo('HATA MESAJI', 'Lütfen verileri tam doldurun!')

   else:
      myEncryptedMessage = cryptocode.encrypt(str(es), str(entryPass))
      print(myEncryptedMessage)
      with open("sifre.txt", "a") as file_sifre:
      #file_sifre = open("sifre.txt", "a+")
         file_sifre.write(str(entryTitle))
         file_sifre.write("\n")
         file_sifre.write(str(myEncryptedMessage))
         file_sifre.write("\n")
         #file_sifre.close()
         print("Şifre Kaydedildi")

def decrypt_button():
   dec_secret = entry_secret.get("1.0", 'end-1c')
   dec_pass = entry_sifre.get()
   myDecryptedMessage = cryptocode.decrypt(str(dec_secret), str(dec_pass))
   print(myDecryptedMessage)

   entry_secret.delete("1.0", END)
   entry_secret.insert("1.0",myDecryptedMessage)

#************UI************************

#Logo
img = ImageTk.PhotoImage(Image.open("secret2.png"))
label_logo = tkinter.Label(image = img)
label_logo.pack()
#Label:Title
label_title = tkinter.Label(text="Şifrelenecek Konu Başlığı", font=('Arial', 10, "bold"))
label_title.pack()
#Entry:Title
entry_title = tkinter.Entry(width=30)
entry_title.pack()
#Label:Secret
label_secret = tkinter.Label(text="Şifrelenecek İçerik", font=('Arial', 10, "bold"))
label_secret.pack()
#Entry:Secret
entry_secret = tkinter.Text(width=50, height=10)
entry_secret.pack()
#Label:Sifre
label_sifre = tkinter.Label(text="Şifreyi Giriniz", font=('Arial', 10, "bold"))
label_sifre.pack()
#Entry:Sifre
entry_sifre = tkinter.Entry(width=30)
entry_sifre.pack()
#Şifreleme Butonu
encrypt_button = tkinter.Button(text="Save and Encrypt", command=encrypt_button,pady=15,padx=20)
encrypt_button.pack(pady=15)
#Şifre Çözme Butonu
decrypt_button = tkinter.Button(text="Decrypt Text", command=decrypt_button,pady=15,padx=20)
decrypt_button.pack()

window.mainloop()
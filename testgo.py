import itertools
from subprocess import check_output

passFound=False
for i in range(7):
    g = itertools.product('qwertyuioplkjhgfdsazxcvbnm', repeat=i+6)

    for password in g:
        try:
            check_output(r'"C:\Program Files\WinRAR\unrar.exe" x knowledge.rar -p'
                         + ''.join(password), shell=True)

            print("Password Found: "+''.join(password))
            passFound=True
            break
        except:
            print("Trying: "+''.join(password))
            continue
        if passFound:
            break

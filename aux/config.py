def pyqt5isinstaled():
    try:
        import PyQt5
        print("\033[1;32mPyQt5 já está instalado.")
        return True
    except:
        print("\033[1;31mPyqt5 não está instalado.\n\033[1;33mO use o comando a seguir para instala-lo")
        print("\033[1;31mpip3 install PyQt5")
        return False
pyqt5isinstaled()
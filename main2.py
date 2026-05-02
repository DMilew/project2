from logic2 import *


def main():
    '''
    Sets up windows and Guis.
    '''
    app = QApplication([])
    window = Logic()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

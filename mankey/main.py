from mankey.data import check_registration
from mankey.menu import index_menu, new_pwd, search_pwd_menu


def main():
    check_registration()

    while True:
        choice = index_menu()

        if choice == -1:
            break
        elif choice == 0:
            search_pwd_menu()
        elif choice == 1:
            new_pwd()


if __name__ == "__main__":
    main()

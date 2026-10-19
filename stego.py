# stego.py - main file, run this one
# steganography tool that hides messages in images

from hide import hide_message
from read import read_message


def main():
    print("=" * 45)
    print("  STEGANOGRAPHY TOOL")
    print("  hide secrets in images B)")
    print("=" * 45)
    print()
    print("1. Hide a message in an image")
    print("2. Read a hidden message from an image")
    print("3. Exit")
    print()

    choice = input("Pick an option (1/2/3): ").strip()

    if choice == "1":
        print("\n-- HIDE MODE --")
        # time to be sneaky

        img_path = input("Path to your image (use PNG): ").strip()
        msg = input("Type your secret message: ")
        # not stripping the message because spaces might be intentional

        if msg == "":
            print("You didnt type anything lol")
            return

        out_path = input("Save output as (e.g. secret.png): ").strip()
        if out_path == "":
            out_path = "secret_image.png"

        # force png because jpeg compression destroys the hidden data
        # learned that the hard way honestly
        if not out_path.lower().endswith('.png'):
            out_path = out_path + '.png'
            print(f"  Changed to PNG -> {out_path} (jpeg would ruin it)")

        try:
            hide_message(img_path, msg, out_path)
        except FileNotFoundError:
            print(f"Cant find '{img_path}', check the path?")
        except Exception as e:
            print(f"Something broke: {e}")

    elif choice == "2":
        print("\n-- READ MODE --")
        # detective time

        img_path = input("Path to image with hidden message: ").strip()

        try:
            result = read_message(img_path)
            if result is not None:
                print(f"\nThe secret message is:")
                print(f'  "{result}"')
        except FileNotFoundError:
            print(f"Cant find '{img_path}', check the path?")
        except Exception as e:
            print(f"Something broke: {e}")

    elif choice == "3":
        print("Bye! your secrets are safe")

    else:
        print("thats not 1, 2, or 3...")


if __name__ == "__main__":
    main()

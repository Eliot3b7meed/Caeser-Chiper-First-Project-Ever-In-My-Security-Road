what = str(input("what did you Need  >>  "))
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def Decode():
        Key = int(input("Key Number >>  "))
        String = str(input("String You Need To Decrypt >>  "))
        i = int(0)
        while i < len(String):
                M = alphabet.index(String[i])
                eq = ( M - Key ) % 26
                print(alphabet[eq], end="")
                i += 1
def Encode():
        Key = int(input("Key Number >>  "))
        String = str(input("String You Need To Encrypt >>  "))
        i = int(0)
        while i < len(String):
                M = alphabet.index(String[i])
                eq = ( Key + M) % 26
                print(alphabet[eq], end="")
                i += 1
if __name__ == "__main__":
        if "de" in what:
                Decode()
                print("\n")
        elif "en" in what:
                Encode()
                print("\n")
         else:
                print("This Input Not Valid Sorry For You :( ")
        

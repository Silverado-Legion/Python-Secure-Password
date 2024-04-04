

import secrets

Letter_List = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
Symbol_List = ("~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "|", "\\", ":", ";", "\"", "\'", "<", ">", ".", "?", "/")

# - Notice: Include_Symbols being true may result in generated passwords being hard to memorize
Include_Symbols = False
Include_Numbers = True

Module_Count = 3        # - How many modules to generate
Module_Length = 6       # - Length of each module
Module_Separator = "-"  # - Character that separates modules. Configuration switches between dashes and underscores.

# - Warning: This will immediately generate a password, and not ask for any configuration at all.
Bypass_Setup = False  # - Edit above variables for desired configuration when using this.

Upper_Letter_Pos = 0  # - Initialize variable that determines which module will have an upper letter.
Count = 0             # - Variable to keep track of the module currently being generated
Complete_String = ""


def Generate_Digit():
    S = ""
    if Include_Numbers and Include_Symbols:
        R = secrets.randbelow(4)
        if R == 0 or R == 1:
            S = secrets.choice(Letter_List)
        elif R == 2:
            S = str(secrets.randbelow(10))
        elif R == 3:
            S = secrets.choice(Symbol_List)
        return S

    elif Include_Numbers:
        R = secrets.randbelow(3)
        if R == 0 or R == 1:
            S = secrets.choice(Letter_List)
        elif R == 2:
            S = str(secrets.randbelow(10))
        return S

    elif Include_Symbols:
        R = secrets.randbelow(3)
        if R == 0 or R == 1:
            S = secrets.choice(Letter_List)
        elif R == 2:
            S = secrets.choice(Symbol_List)
        return S


def Generate_Module(length):
    global Count
    Module_String = ""
    ULP = secrets.randbelow(length)
    for x in range(length):
        S = Generate_Digit()
        if S.isalpha() and Count == Upper_Letter_Pos and x == ULP:
            S = S.capitalize()
        Module_String += S
    Count += 1
    return Module_String


print("Password Generator v1.0.0 by Silverado-Legion on GitHub")

if not Bypass_Setup:
    Setup = input("Do you wish to include symbols? (Leave blank for default) Y/n: ")
    Setup.lower()
    if Setup == "y":
        Include_Symbols = True
    elif Setup == "n":
        Include_Symbols = False

    Setup = input("Do you wish to include numbers? (Leave blank for default) Y/n: ")
    Setup.lower()
    if Setup == "y":
        Include_Numbers = True
    elif Setup == "n":
        Include_Symbols = False

    Setup = input("How many modules in the password? (Leave blank for default) int: ")
    if not Setup == "":
        Module_Count = int(Setup)

    Setup = input("How many characters per module? (Leave blank for default) int: ")
    if not Setup == "":
        Module_Length = int(Setup)

    Setup = input("Do you wish to use dashes or underscores to separate modules? (Leave blank for default) D/u:")
    Setup.lower()
    if Setup == "d":
        Module_Separator = "-"
    elif Setup == "u":
        Module_Separator = "_"

    print(f"Configuration complete\n\nSettings:\nInclude Numbers: {Include_Numbers}")
    print(f"Include Symbols: {Include_Symbols}\nModule Count: {Module_Count}\nModule Length: {Module_Length}")
    print(f"Separator character: {Module_Separator}\n")
print("Beginning password generation")

Complete_String += Generate_Module(Module_Length)
if Module_Count > 1:
    for y in range(Module_Count - 1):
        Complete_String += Module_Separator + Generate_Module(Module_Length)

print("Password generation complete\nGenerated password:\n" + Complete_String)

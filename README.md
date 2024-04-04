# Python-Secure-Password
Apple-style password generator using secrets library
### Info
Python 3.11, built-in secrets library was used.
The password generator generates a number of "modules", which are sets of characters of a set length, for example, 6 characters. These modules are then seperated by a dash, underscore, or whatever other seperating character you may choose.

# Usage (v1.0)
Most of the configuration happens when the script is run, through various prompts in the console. The settings in the actual script are the default settings for the pasword generator, and shouldn't really be cahnged unless "Bypass_Setup" is set to True.

### Script Settings
#### The following settings should not really ever be changed, but can if you want to or need to:
Letter_List: Contains the possible letters to be used by the script. By default, contains the following: 

"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"

Symbol_List: Contains the possible symbols to be used by the script. By default, contains the following: 

"~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "\[", "}", "]", "|", "\\\\", ":", ";", "\"", "\'", "<", ">", ".", "?", "/"
#### Notice: The entry containing the backslash (\) has two backslashes, as it needs to be an escape character to work. Treated as one backslash by the Python interpreter. [Also: the sourcecode for this markdown file has 4, so that 2 can be displayed]

#### The following settings are on the format of the generated password:
Include_Symbols: Whether or not symbols should be included in the generated password. Notice: May result in passwords that are hard to memorize, though potentially more secure. Default: False

Include_Numbers: Whether or not numbers should be included in the generated password. Default: True


Module_Count: How many "modules" (sections of the generated password of a defined length, with each seperated by the chosen seperator character). Default: 3

Module_Length: Number of characters in each module. Default: 6

Module_Seperator: Character that seperates each module. Configuration prompt lets you switch between underscore and dash. Default: "-"


Bypass_Setup: This bypasses the configuration prompts on the console, immediately generating a password. This is not recommended to be set to true, unless you need to generate passwords more frequently. If set to True, the settings set above will be done automatically, with no option to configure other than editing the script.
### Configuration in Console
If Bypass_Setup is set to False, then the script will send some configuration prompts in the console when running. The questions are as follows:

"Do you wish to include symbols? (Leave blank for default) Y/n:" 

"Do you wish to include numbers? (Leave blank for default) Y/n:" 

"How many modules in the password? (Leave blank for default) int:" 

"How many characters per module? (Leave blank for default) int:"

"Do you wish to use dashes or underscores to separate modules? (Leave blank for default) D/u:"

### Password Generation
After configuration, the script will remind you in the console of the selected settings, then begin password generation. Once complete (which takes only miliseconds), it will notify you of such and then show your generated password, and then the process will exit with exit code 0.
#### Known Issues:
The script is supposed to generate one uppercase letter, but may not if the selected position (which is selected before password generation) is a symbol or number, rather than a letter. Always check to see if the generated password has an uppercase letter. This issue will be addressed in the future, likely just requiring a simple reconfiguration of how it chooses the character to make uppercase.

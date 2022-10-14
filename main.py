"""
--Non Homographs--
pasword.txt
/home/user/Secret/Password.txt
../user/secret.txt
../../secret/password.txt
./secret/password.txt

--Homographs--
password.txt
/home/user/secret/password.txt
./password.txt
./user/secret/password.txt
../password.txt
../secret/password.txt
~/secret/password (~ represents the user folder in linux file systems)

All filepaths assume the current working directory is /home/user/secret/
"""


def manual_test(Full_File_Path):
    # Get both the file paths then run
    file_path1 = input('Specify the first filename: ')
    file_path2 = input('Specify the second filename: ')
    run_test(file_path1, file_path2, Full_File_Path)

def test_cases(Full_File_Path):
    # This needs to be worked on.....
    file_path1 = "password.txt"
    homographs = ["password.txt", "/home/user/secret/password.txt", "./password.txt", "./user/secret/password.txt", "../password.txt", "../secret/password.txt", "~/secret/password"]
    non_homographs = ["pasword.txt", "/home/user/Secret/Password.txt", "../user/secret.txt", "../../secret/password.txt", "./password.txt"]

    run_test(file_path1, homographs, Full_File_Path)


def run_test(file_path1, file_path2, Full_File_Path):
    file_path1 = canonicalization(file_path1, Full_File_Path)
    file_path2 = canonicalization(file_path2, Full_File_Path)
    
    # Compare the two final full file paths
    print("\nCanonicalized file paths")
    print(file_path1)
    print(file_path2)
    # Check if the full file paths are equal
    if file_path1 == file_path2:
        print(f'The paths are homographs')
        return True
    else:
        print(f'The paths are NOT homographs')
        return False

# canonicalization for ~ (tilde)
def tilde(file_path, File_Path):
    # Look for if ~ is in the file path
    if file_path.find("~") == 0:
        # Replace the ~ with the file path
        file_path = File_Path + file_path.split("~")[1][1:]
        return file_path
    else: # do nothing
        return file_path

# Canonicalization for ./
def dot(file_path, Full_File_Path):
    # Error if file name is less than 2 characters
    if len(file_path) > 2:
        # if the first two characters are "./"
        if file_path[0] + file_path[1] == './':
            # Remove ./ from the string 
            file_path = Full_File_Path + file_path[2:]
    return(file_path)

def canonicalization(file_path, Full_File_Path):
    # Full File path starts normally with / (/home/user/secret/password.txt)
    if file_path[0] == "/":
        # test for if two dots are in middle (/home/user/../user/secret/)

        return file_path

    # Work with the tilde ~
    file_path = tilde(file_path, Full_File_Path)

    # One dot at the start of the file path (./password.txt)
    file_path = dot(file_path, Full_File_Path)

    # Two dots .. in any part of file (../secret/password.txt)

    # One dot in any part of file (/home/user/secret/./password.txt)

    # Two // in file 
    
    # No / at start of file (password.txt)
    #file_path = Full_File_Path + file_path1
    return file_path




Full_File_Path = "/home/user/secret/"
userinput = input("Please enter a number\n1. Enter the test cases manually\n2. Run the provided test cases\nChoice: ")
if userinput == "1":
    manual_test(Full_File_Path)
else:
    test_cases(Full_File_Path)

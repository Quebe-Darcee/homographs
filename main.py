"""
-- Canon --

    /home/user/secret/password.txt

--Test Cases--
(2-3 test cases to verify)

    -- ./ --
        Non-Homographs
        ./secret/password.txt
        ./home/secret/password.txt

        HomoGraphs
        ./password.txt
        ./../secret/password.txt
        
    -- ../ --
        Non-Homographs
        ../user/secret.txt
        ../../secret/password.txt

        Homographs
        ../secret/password.txt
        ../../user/secret/password.txt

    -- ~/ --
        Non-Homographs
        ~/password.txt
        ~/../password.txt
        
        Homographs
        ~/secret/password
        ~/../user/secret/password.txt

    -- Caps Sensitivity --
        Non-Homographs
        home/user/Secret/Password.txt
        passWord.txt

        Homographs
        /~/Secret/../secret/password.txt
        /./Password/../password.txt

    -- Start Folder --
        Non-Homographs
        ./secret/password.txt
        ./user/secret/password.txt

        Homographs
        password.txt
        ./password.txt

    -- Unknown Folders --
        Non-Homographs
        ../../random/foldername/password.txt
        ~/folder/randomname/password.txt
        
        Homographs
        ~/random/../secret/password.txt
"""

from contextlib import nullcontext


def manual_test(Full_File_Path):
    # Get both the file paths then run
    file_path1 = input('Specify the first filename: ')
    file_path2 = input('Specify the second filename: ')
    run_test(file_path1, file_path2, Full_File_Path)

def test_cases(Full_File_Path):
    homographs = ["password.txt", "~/secret/password.txt", "/~/secret/password.txt","./password.txt", "../secret/password.txt", "./user/secret/password.txt", "./././user/secret/password.txt", "./../secret/password.txt", "../../user/secret/password.txt", "~/../user/secret/password.txt", "./Password/../password.txt"]
    non_homographs = ["/../../random/foldername/password.txt", "~/folder/randomname/password.txt", "~/Secret/../secret/password.txt", "./secret/password.txt", "home/user/Secret/Password.txt", "passWord.txt", "~/password.txt", "../user/secret.txt", "../../secret/password.txt", "./secret/password.txt", "./home/secret/password.txt", "~/../password.txt", "./user/secret/password.txt", "../../../home/user/secret/password.txt"]
    forbidden_file = "/home/user/secret/password.txt"

    print("\nTESTING HOMOGRAPHS")
    # Homographs
    count = 1
    for homograph in homographs:
        print(f"\n{count}. {homograph}")
        run_test(forbidden_file, homograph, Full_File_Path)
        count+=1

    print("\nTESTING NON-HOMOGRAPHS")
    # Non-Homographs
    count = 1
    for non_homograph in non_homographs:
        print(f"\n{count}. {non_homograph}")
        run_test(forbidden_file, non_homograph, Full_File_Path)
        count+=1

    



def run_test(file_path1, file_path2, Full_File_Path):
    file_path1 = canonicalization(file_path1, Full_File_Path)
    file_path2 = canonicalization(file_path2, Full_File_Path)
    
    # Compare the two final full file paths
    print("\nCanonicalized file paths:")
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
def tilde(file_path, Full_File_Path):
    # Look for if ~ is in the file path
    if file_path.rfind("~") == 0:
        # Replace the ~ with the file path
        file_path = Full_File_Path.split("secret")[0] + file_path.split("~")[1][1:]
        return file_path
    if file_path.rfind("~") > 0:
        # Remove all the previous string before ~
        file_path = file_path[file_path.rfind("~") - 1:]
        file_path = Full_File_Path.split("secret")[0] + file_path.split("~")[1][1:]
        return file_path
    # do nothing
    return file_path

# Canonicalization for ./
def dot(file_path, Full_File_Path):
    # Error if file name is less than 2 characters
    if len(file_path) > 2:
        # if the first two characters are "./"
        while file_path[0] + file_path[1] == './':
            # Remove ./ from the string 
            file_path = file_path[2:]
    return(file_path)

def two_dots(file_path, Full_File_Path):
    upCount = file_path.count('..')
    # ../../.. starts the path
    if file_path[:8] == "../../..":
        print("Error: Cannot go above home directory. Assumed starting directory is: /home/user/secret/")
    # ../../ starts the path
    elif file_path[:5] == "../..":
        # Split to /home
        modified_file_path = Full_File_Path.split("user")[0]
        file_path = modified_file_path + file_path[6:]
    # .. is start of file path
    elif file_path[:2] == "..":
        # Split the file path to /home/user
        modified_file_path = Full_File_Path.split("secret")[0]
        file_path = modified_file_path + file_path[3:]
    elif (upCount > 0):
        seqUpCounts = 0 #The number of folders we must go up for one row of ../../'s
        prevIsDot = false
        prevIsDouble = false
        numFolders = 0
        upCountStart = 0
        for x in file_path:
            if x == "." & prevIsDot == true: #if this and the previous index are dots
                seqUpCounts += 1
                prevIsDouble = true
            elif x == "." & prevIsDot == false: # if this one but not the last are dots
                prevIsDot = true
            elif x == "/": # slashes are used to count the folders weve passed through and mark where we start counting up
                prevIsDot = False
                if seqUpCounts == 1:
                    upCountStart = numFolders
                numFolders += 1
            else: # If not a slash or a dot, reset the
                prevIsDot = false
                prevIsDouble = false
                if seqUpCounts > 0:
                    modified_file_path = Full_File_Path.split("/")[upCountStart] # not sure how but we need to split in two at the start of the upCount

    return file_path


def canonicalization(file_path, Full_File_Path):
    # Full File path starts normally with / (/home/user/secret/password.txt)
    if file_path[0] == "/":
        # test for if two dots are in middle (/home/user/../user/secret/)

        file_path = tilde(file_path, Full_File_Path)

        return file_path

    # Work with the tilde ~
    file_path = tilde(file_path, Full_File_Path)

    # One dot at the start of the file path (./password.txt)
    file_path = dot(file_path, Full_File_Path)

    # Two dots .. in any part of file (../secret/password.txt)
    file_path = two_dots(file_path, Full_File_Path)
    """
        if file_path[]



        getOneFolderUp(fileName)
        delete the /.. from the string
        delete the previous working directiory from the string (eg: in the above case, the string would read /home/secret after this point)
        return
    """
    # One dot in any part of file (/home/user/secret/./password.txt)
    """
    If /. is the first character, replace it with home/user/secret
    else just delete it because it refers to the current directory
    """
    while file_path[:1] == "/.":
        file_path = file_path.split("/.")[1]


    # Two // in file 
    
    # No / at start of file (password.txt)
    if file_path[0] != "/":
        if file_path[:4] == "home":
            file_path = "/" + file_path
        elif file_path[:4] == "user":
            file_path = Full_File_Path.split("user")[0] + file_path
        elif file_path[:6] == "secret":
            file_path = Full_File_Path.split("secret")[0] + file_path
        else:
            file_path = Full_File_Path + file_path
    return file_path

def getOneFolderUp(folderName):
    """ if folderName = "home" return "/"
        If folderName = "user" return "home"
        if folderName = "secret" return "user"
        else throw error or ask for the previous folder and return
    """



Full_File_Path = "/home/user/secret/"
userinput = input("Please enter a number\n1. Enter the test cases manually\n2. Run the provided test cases\nChoice: ")
if userinput == "1":
    manual_test(Full_File_Path)
else:
    test_cases(Full_File_Path)

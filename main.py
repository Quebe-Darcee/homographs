
def manual_test(Full_File_Path):
    # Get both the file paths then run
    file_path1 = input('Specify the first filename: ')
    file_path2 = input('Specify the second filename: ')
    run_test(file_path1, file_path2, Full_File_Path)

def test_cases(Full_File_Path):
    homographs = ["password.txt", "~/secret/password.txt", "/~/secret/password.txt","./password.txt", "~/Secret/../secret/password.txt", "../secret/password.txt", "./../secret/password.txt", "../../user/secret/password.txt", "~/../user/secret/password.txt", "./Password/../password.txt", "../../../home/user/secret/password.txt"]
    non_homographs = ["../../random/foldername/password.txt", "~/folder/randomname/password.txt","./user/secret/password.txt", "./././user/secret/password.txt", "./secret/password.txt", "home/user/Secret/Password.txt", "passWord.txt", "~/password.txt", "../user/secret.txt", "../../secret/password.txt", "./secret/password.txt", "./home/secret/password.txt", "~/../password.txt", "./user/secret/password.txt"]
    
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
    home_directory = "/home/user"
    file_path1 = canonicalize(file_path1, Full_File_Path, home_directory)
    file_path2 = canonicalize(file_path2, Full_File_Path, home_directory)
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

def canonicalize(path, working_directory, home_directory):
    working_segments = working_directory.split('/')
    home_segments = home_directory.split('/')
    path_segments = path.split('/')

    # find starting directory
    canonicalized_segments = working_segments.copy()
    if path.startswith('/'):
        canonicalized_segments = []
    if path.startswith('~'):
        canonicalized_segments = home_segments.copy()
        path_segments.pop(0)


    # traverse given path and create canonical path
    for segment in path_segments:
        if segment == "..":
            canonicalized_segments.pop()
        elif segment == "~":
            canonicalized_segments = home_segments.copy()
        elif segment == ".":
            pass
        else:
            canonicalized_segments.append(segment)

    return '/'.join(canonicalized_segments)


Full_File_Path = "/home/user/secret"
userinput = input("Please enter a number\n1. Enter the test cases manually\n2. Run the provided test cases\nChoice: ")
if userinput == "1":
    manual_test(Full_File_Path)
else:
    test_cases(Full_File_Path)

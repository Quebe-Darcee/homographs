Path Homograph

--Constructs--

    ./ -Current folder
    
    ../ -Up one folder
    
    ~/ -Home folder
    
    Caps Sensitivity
    
    Different starting folder
    
    unknown filepaths

-- Canon --

    /home/user/secret/password.txt

--Test Cases--

    -- ./ --
        Non-Homographs
        ./secret/password.txt

        HomoGraphs
        ./password.txt
        
    -- ../ --
        Non-Homographs
        ../user/secret.txt
        ../../secret/password.txt

        Homographs
        ../secret/password.txt

    -- ~/ --
        Non-Homographs
        ~/password.txt
        
        Homographs
        ~/secret/password

    -- Caps Sensitivity --
        Non-Homographs
        /home/user/Secret/Password.txt
        passWord.txt

        Homographs
        ~/Secret/../secret/password.txt

    -- Start Folder --
        Non-Homographs
        ./secret/password.txt

        Homographs
        password.txt

    -- Unknown Folders --
        Non-Homographs
        ../../random/foldername/password.txt
        ~/folder/randomname/password.txt
        
        Homographs
        /~/random/../secret/password.txt


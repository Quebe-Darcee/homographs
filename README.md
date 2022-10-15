Path Homograph

--Constructs--

    ./ -Current folder
    
    ../ -Up one folder
    
    ~/ -Home folder
    
    Caps Sensitivity
    
    Different starting folder
    
    unknown filepaths

--Test Cases--

    -- ./ --
        Non-Homographs
        ./secret/password.txt

        HomoGraphs
        ./password.txt
        ./user/secret/password.txt
        
    -- ../ --
        Non-Homographs
        ../user/secret.txt
        ../../secret/password.txt

        Homographs
        ../password.txt
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
        
    -- Start Folder --
        Non-Homographs
        ./secret/password.txt

        Homographs
        password.txt
        /home/user/secret/password.txt

    -- Unknown Folders --
        Non-Homographs
        /../../random/foldername/password.txt
        /folder/randomname/password.txt
        
        Homographs



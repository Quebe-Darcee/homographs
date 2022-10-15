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
        /./secret/password.txt
        /./home/secret/password.txt

        HomoGraphs
        /./password.txt
        /./../secret/password.txt
        
    -- ../ --
        Non-Homographs
        /../user/secret.txt
        /../../secret/password.txt

        Homographs
        /../secret/password.txt
        /../../user/secret/password.txt

    -- ~/ --
        Non-Homographs
        /~/password.txt
        /~/../password.txt
        
        Homographs
        /~/secret/password
        /~/../user/secret/password.txt

    -- Caps Sensitivity --
        Non-Homographs
        /home/user/Secret/Password.txt
        passWord.txt

        Homographs
        /~/Secret/../secret/password.txt
        /./Password/../password.txt

    -- Start Folder --
        Non-Homographs
        /./secret/password.txt
        /./user/secret/password.txt

        Homographs
        password.txt
        /./password.txt

    -- Unknown Folders --
        Non-Homographs
        /../../random/foldername/password.txt
        /~/folder/randomname/password.txt
        
        Homographs
        /~/random/../secret/password.txt


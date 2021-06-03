# Steps to Fix Connection

1. Install UnrealCV plugin to the local game
2. Change port
    - Run "vget /unrealcv/status" to find location of config file
    - Update config file with port number
    - Update jupyter nb with port number
        ```
        import unrealcv

        ip = [#get with ipconfig in terminal]
        port = DESIRED_PORT
        client = client = unrealcv.Client((ip, port))
        ```


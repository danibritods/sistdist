# xmlrpc chat
Proof of concept of a chat application using the python library xmlrpc. Developed to our Distribuited Systems college subject.

# usage 
Run the server instance:
``` 
python chat_server.py 
```

Run the client instances:

``` 
python chat_client.py
```

## config
The only configuration currently available is IP and PORT in the config.py file


# file structure
    ├── README.md                  <- The top-level README for developers using this project (also know as this file!)
    ├── config.py                  <- Definition of IP and PORT
    ├── chat.py                    <- Chat module
    ├── xmlrpc_warapper.py         <- Module that wraps xmlrpc server and client
    ├── chat_server.py             <- Server running script
    ├── chat_client.py             <- Client running script

### Acknowledgments
* This README was adapted from [*A template to make good README.md*](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
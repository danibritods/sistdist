# TODO

## V0.1

### Code

- [ ] Minimum communication features
  - [ ] Client (N instances)
    - [ ] string checkMessage()
    - [ ] bool(?) sendMessage(remoteId, message)
    - [ ] Attributes
      - [ ] string id
      - [ ] dictionary chatList
  - [ ] Server (1 instance)
    - [ ] bool receiveMessage (senderId, receiverId, message)
    - [ ] string getMessage (id)
    - [ ] Attributes
      - [ ] dictionary list (?) pendingMessage

#### Self

- [ ] Server
  - [ ] Listen for messages from clients
  - [ ] Print client Id and message
- [ ] Cliente
- [ ] Try to exchange message between processes
- [ ] Try to exchange messages in a network
- [ ] JV: Add a command to show the available methods in the class

### Classroom - 31/08/2022

- [ ] Check if RPC and RMI in Python 3 are the same thing
- [ ] Check features and differences between:
  - [ ] xmlrpc
  - [ ] Pyro 2, 3, 4, 5
  - [ ] Dopy
  - [ ] PyCSP

- [ ] Show what was discovered

### Classroom - 30/09/2022

- [ ] Client
  - [ ] Set unique id for each client
  - [ ] Directed message
  - [ ] Optional: multicast message
  - [ ] Optional: broadcast message
- [ ] Server
  - [ ] Return json

## V0.N

- [ ] Set timestamp in each message
- [ ] Establish some system of online status
- [ ] Establish simple permanence system (such as pickle, txt... In some multiplataform folder. maybe /temp for now.)
- [ ] Decide how to approach library importation
- [ ] JV: Check if the created id is not already in use
  - [ ] JV: Or use something like '92c1290f512e20e1b13888fdd504a238d5'
- [ ] JV: Retry request message
- [ ] JV: Duplicate filtering (?)
- [ ] JV: Retransmission of results
- [ ] JV Self: Check if the exchanged data is an object

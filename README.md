pychat-server
=============

Simple twisted-based chat server supporting multiple users and rooms.


## Protocol documentation

Server awaits plain text lines with optional commands and responds with JSON-formatted replies.

At the present time the following commands are supported:


### LOGIN nickname

Parameters:

* nickname

Authorize with the server, supplying the `nickname` used. Duplicated nicknames in rooms are not allowed.


#### Server response:

Successful login:

    {"type": "commandResult", "result": "Username set to nickname"}

Error:

    {"type": "error", "error": "Invalid nickname"}


### JOIN room

Aliases:

* JOIN ROOM

Parameters:

* room

Join a `room` (subscribe for all messages sent within this room). If a room does not exist it would be created.


#### Server response:

Successful join:

    {"type": "commandResult", "result": "Joined room room"}

Error:

    {"type": "error", "error": "Login required"}
    {"type": "error", "error": "Invalid room name: !@#, please use alphanumericcharacters only"}
    {"type": "error", "error": "User with such nickname is already present in the requested room"}


### LEAVE

Aliases:

* LEAVE ROOM
* LEFT ROOM
* LEFT

Leave a room (unsubscribe from messages)


#### Server response:

Successful leave:

    {"type": "commandResult", "result": "OK"}

Error:

    {"type": "error", "error": "Join a room first"}


### HISTORY [from [to]]

Parameters:

* [optional] from
* [optional] to

Request history for a room from the server. Optional parameters allow you to fetch messages from the requested time interval only.


#### Server response:

Successful request:

    {"body": {"body": "User user has joined the room", "from": "user", "room": "room", "utctimestamp": "2015-05-24 15:17:19.209832", "to": "user", "type": "userJoined"}, "type": "history", "from": "user"}

Error:

    {"type": "error", "error": "Join a room first"}

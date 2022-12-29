# Django Chatrooms

This project develops an asynchronous chat room service with Django and the Channels Package.

Will develop a working chat room.

## Project Specs

- real live chat (with multiple users)
- user registration
- track conversation and users in chat
- record/save conversations
- delete/ edit messages
- _custom_ add social login

## Theory

Asynch vs. Synch: this can mean different things in different contexts.

Django webpages are mostly synchronous - the commands to complete a request are done in order and one depends on the other. If one times out, you'll recieve a timeout. using HTTP requests expects a reply before the application or browser does anything else.

Asynchronous webpages launch a request instead of sending a request. The request is forgotten about, and then you can carry on executing tasks. If a reponse is received, this information is then sent back. Working in asynchronous way allows a real-time workflow, because you can receive a message at any time once its sent, rather than making a request to receive the latest message.

This means a traditional HTTP server cannot handle sending a message to separate users once the message is added to the chat log. The chat log has to be accessed **again** by the second user to see any new messages. This is the reason some messaging apps require refreshes to get the latest message.

The solution is to use websockets instead. Websockets allow us to develop a chat with an asynchronous environment.

Any live or real-time data can be served in this asynchronous manner. This type of application is going to become more common.

## Websockets

This is a bi-directional protocol. This allows the client and server to talk to each other independently at the same time (called full-duplix communication). It's compatible with all modern browsers. There's are also secured websockets (WSS).

### How they work

- a user goes to a website with a websocket (HTTP request). Then upgrades to a websocket enabled connection.
  - This creates a record that the user now has a websocket connection available, or has websockets.
  - this opens a persistent connection.
  - the user can close this connection or the application server can close the connection itself.
- Then other users can now make the connection to the server, and add messages to the chat room hosted on the server.

This could be used for multiple data producers to be able to add to the same database independently, or other uses.

### Django Setup

All the users HTTP requests are handled by NGINX server and the Django Views, which uses WSGI. The Webksocket requests are handled by ASGI, and Daphine is the python package that handles this connection handling for us. This routes the websocket requests to a consumer.

You can think of the consumer as a Django view. Then we can sort out the logic to do with the data produced by this consumer view. The consumer view will get the message and send it to the users in the same chat room.

Note that its very similar to the usual Django request pattern, but slightly different.

### Channels in Django

Every client will have a reply channel from their connections.

This keeps track of users in a connected list.

Channels use groups. And you can create user groups that are assigned to a chatroom. Then, when a user goes to a chat room, the user will be added to the chat room's reply channel.

This is how Django keeps track of who's added to the group, and messages will be sent to the whole group. This will send messages individually, but the logic of sending the messages relies on referring the individual users as a group.

Users are assigned to a group when they join a chat room.

## Process

- install django channels
- create django templates / views
- channel routing - exactly the same as the URLs in Django.
- consumer view: uses the channel routing to send the proper messages to the right users.
- template configuration to handle Web sockets.

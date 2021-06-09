# ipc-connector
 Full Duplex inter process Communication software with TCP socket
 
# How to use?
this software have two section 1."token generator" and 2."main ipc connector".<br/>#first you need to select which ip to listen.#then you need to select listening port.<br/>#after that you need to set timeout for socket to kill thread when peers dosent send anything to ipc software.<br/>#then you need to set buffer size.the buffer size should equal in both peers and should bigger than data length you need to send.<br/># when ipc connector start to listening you need to have token for start connection from client.token_generator.py uses merkle tree with sha256 hash algorithm for generating token.after that both clients have token for starting communicate.



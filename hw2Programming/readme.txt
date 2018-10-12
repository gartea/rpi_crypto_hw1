Set up:
3 files kdc, alice and bob.
To show the Needham–Schroeder first get the kdc running, then bob.py running and 
then alice.py running. It will do the Needham–Schroeder protocol giving alice 
and bob keys from the KDC using Diffie-Hellman. Then it will transmit the
symmetric key between Bob and Alice for them to use. At the end
Bob and Alice both have the symmetric key and can communicate securely.
Assumptions:
KDC and Bob are server to communicate with. Alice is just a person that sends
messages to servers and gets replies back.
Algebraic constructions:
My cryptographic algorithm is a simple shift cipher by a random amount. Could
be fairly easily replaced by something secure
# MessageEncoder
This program allows you to send encoded messages in the form of composite numbers. If you have been sent a message, use the MessageDecoder program.

Say that a certain message is encoded as the number '1000'. This number is multiplied by a prime only known by the sender, let's say 3, and sent to the recipient. The recipient then multiplies the number, in this case 3000, by a prime known only to them, let's say 5. This is sent back to the original sender, who divides the number by the prime only they know, in this case yielding 5000. Finally, this number is sent to the original recipient, who divides by the prime only they know, yielding 1000. This can then be decoded using the MessageDecoder program.

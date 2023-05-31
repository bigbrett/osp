# Test ussl with key/cert passed in

try:
    import uio as io
    import wolfssl as ssl
except ImportError:
    print("SKIP")
    raise SystemExit

key = b"0\x82\x019\x02\x01\x00\x02A\x00\xf9\xe0}\xbd\xd7\x9cI\x18\x06\xc3\xcb\xb5\xec@r\xfbD\x18\x80\xaaWoZ{\xcc\xa3\xeb!\"\x0fY\x9e]-\xee\xe4\t!BY\x9f{7\xf3\xf2\x8f}}\r|.\xa8<\ta\xb2\xd7W\xb3\xc9\x19A\xc39\x02\x03\x01\x00\x01\x02@\x07:\x9fh\xa6\x9c6\xe1#\x10\xf7\x0b\xc4Q\xf9\x01\x9b\xee\xb9\x8a4\r\\\xa8\xc8:\xd5\xca\x97\x99\xaa\x16\x04)\xa8\xf9\x13\xdeq\x0ev`\xa7\x83\xc5\x8b`\xdb\xef \x9d\x93\xe8g\x84\x96\xfaV\\\xf4R\xda\xd0\xa1\x02!\x00\xfeR\xbf\n\x91Su\x87L\x98{\xeb%\xed\xfb\x06u)@\xfe\x1b\xde\xa0\xc6@\xab\xc5\xedg\x8e\x10[\x02!\x00\xfb\x86=\x85\xa4'\xde\x85\xb5L\xe0)\x99\xfaL\x8c3A\x02\xa8<\xdew\xad\x00\xe3\x1d\x05\xd8\xb4N\xfb\x02 \x08\xb0M\x04\x90hx\x88q\xcew\xd5U\xcbf\x9b\x16\xdf\x9c\xef\xd1\x85\xee\x9a7Ug\x02\xb0Z\x03'\x02 9\xa0D\xe2$|\xf9\xefz]5\x92rs\xb5+\xfd\xe6,\x1c\xadmn\xcf\xd5?3|\x0em)\x17\x02 5Z\xcc/\xa5?\n\x04%\x9b{N\x9dX\xddI\xbe\xd2\xb0\xa0\x03BQ\x02\x82\xc2\xe0u)\xbd\xb8\xaf"

# Invalid key
try:
    ssl.wrap_socket(io.BytesIO(), key=b"!")
except ValueError as er:
    print(repr(er))

# Valid key, no cert
try:
    ssl.wrap_socket(io.BytesIO(), key=key)
except TypeError as er:
    print(repr(er))

# Valid key, invalid cert
try:
    ssl.wrap_socket(io.BytesIO(), key=key, cert=b"!")
except ValueError as er:
    print(repr(er))

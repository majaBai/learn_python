import hashlib

def xor(x, y):
    return bytes(x[i] ^ y[i] for i in range(min(len(x), len(y))))


def hmac_sha1(key, message):
    if len(key) > 64:
        raise ValueError('The key must be <= 64 bytes in length')
    
    # block_size = 512 bits = 64 bytes, 先补齐
    padded_K = key + b'\x00' * (64 - len(key))
    ipad_0x36 = b'\x36' * 64
    opad_0x5c = b'\x5c' * 64
    inner_pad = xor(padded_K, ipad_0x36)
    outer_pad = xor(padded_K, opad_0x5c)
    return hashlib.sha1(b'gua' + outer_pad + hashlib.sha1(inner_pad + message).digest())

def test():
    key = b'a'
    print(key + b'\x00' * 5)

    msg = b'a'
    res = hmac_sha1(key, msg)
    print(res.hexdigest())

if __name__ == '__main__':
    test()
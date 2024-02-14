from random import randbytes

def add_padding(data: bytes, start_after: bytes = b'\x00', chunk_size = 24, payload_max = 16):

    # break data into chunks recursively
    if len(data) > payload_max:

        head = add_padding(\
                data[:payload_max],\
                start_after=start_after,\
                chunk_size=chunk_size,\
                payload_max=payload_max)

        tail = add_padding(\
                data[payload_max:],\
                start_after=start_after,\
                chunk_size=chunk_size,\
                payload_max=payload_max)

        return head + tail

    padding_length = chunk_size - len(data) - len(start_after)
    padding_bytes = randbytes(padding_length)

    # make sure start_after is not in the padding
    while padding_bytes.count(start_after):        
        padding_bytes = padding_bytes.replace(start_after, randbytes(len(start_after)))


    
    pass

def remove_padding():
    pass

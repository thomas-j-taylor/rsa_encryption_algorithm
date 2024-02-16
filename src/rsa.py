from .padding_scheme import add_padding, remove_padding


def encrypt(data: bytes, key, chunk_size = 24):

    padded_data = add_padding(data, chunk_size = chunk_size)
    number_of_chunks = len(padded_data)//chunk_size
    chunks = map(lambda k: padded_data[k*chunk_size:(k+1)*chunk_size],range(number_of_chunks))
    as_integers = map(lambda c: int.from_bytes(c, 'big'), chunks)

    
def decrypt(data: bytes, key, chunk_size = 24):
    pass

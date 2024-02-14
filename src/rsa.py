from .padding_scheme import add_padding, remove_padding

def encrypt(data: bytes, key, chunk_size = 24):

    padded_data = add_padding(data, chunk_size = chunk_size)
    
def decrypt(data: bytes, key, chunk_size = 24):
    pass

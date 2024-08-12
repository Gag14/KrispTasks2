import io
def get_payments_storage():

# Sample implementation to make the code run in coderpad.
# Do not rely on this exact implementation.
    return open('/dev/null', 'wb')

# This is a library function, you can't modify it.
def stream_payments_to_storage(storage):

# Sample implementation to make the code run in coderpad.
# Do not rely on this exact implementation.
    for i in range(10):
        storage.write(bytes([1, 2, 3, 4, 5]))

def process_payments():

    stream_payments_to_storage(get_payments_storage())
# Here print the check sum of all of the bytes written by
# `stream_payments_to_storage()`
process_payments()
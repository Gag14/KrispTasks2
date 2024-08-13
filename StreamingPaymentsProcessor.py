import io

# This is a library function, you can't modify it.
def get_payments_storage():
    """
    @returns an instance of
    https://docs.python.org/3/library/io.html#io.BufferedWriter
    """
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
    # Create an in-memory stream to capture the data
    buffer = io.BytesIO()
    
    # Stream payments to the in-memory buffer
    stream_payments_to_storage(buffer)
    
    # Get the written data from the buffer
    written_data = buffer.getvalue()
    
    # Calculate the checksum as the sum of all bytes
    checksum = sum(written_data)
    
    # Print the checksum
    print(checksum)

process_payments()
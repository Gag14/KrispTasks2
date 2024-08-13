import io

# This is a library function, you can't modify it.
def stream_payments(callback_fn):
    """
    Reads payments from a payment processor and calls `callback_fn(amount)`
    for each payment.
    Returns when there is no more payments.
    """
    # Sample implementation to make the code run in coderpad.
    # Do not rely on this exact implementation.
    for i in range(10):
        callback_fn(i)

# This is a library function, you can't modify it.
def store_payments(amount_iterator):
    """
    Iterates over the payment amounts from amount_iterator
    and stores them to a remote system.
    """
    # Sample implementation to make the code run in coderpad.
    # Do not rely on this exact implementation.
    for i in amount_iterator:
        print(i)

def process_payments_2():
    """
    This function acts as glue code that enables `store_payments()` to consume
    payments produced by `stream_payments()`.
    """

    # Define a generator that will receive values from the callback and yield them
    def payment_generator():
        # This list will store payments temporarily
        payments = []

        # Define the callback function that will be used in stream_payments
        def callback(amount):
            payments.append(amount)

        # Call stream_payments with the callback function
        stream_payments(callback)

        # Yield each payment from the list to the iterator
        for payment in payments:
            yield payment
    
    # Pass the generator to store_payments
    store_payments(payment_generator())

# Example usage
process_payments_2()

def get_value(data, key, default, lookup=None, mapper=None):
    """
    Finds the value from data associated with key, or default if the
    key isn't present.
    If a lookup enum is provided, this value is then transformed to its
    enum value.
    If a mapper function is provided, this value is then transformed
    by applying mapper to it.
    """
    # Check if the key is in data to avoid KeyError
    if key not in data:
        return default  # Early return if key is not present

    return_value = data[key]
    
    # Check for both None and empty string
    if return_value is None or return_value == "":
        return_value = default

    # Apply the lookup transformation if provided
    if lookup:
        # Should check if return_value is in lookup to avoid KeyError
        if return_value in lookup:
            return_value = lookup[return_value]
        else:
            # Return a warning or default if not found in lookup
            return default
    
    # Apply the mapper function if provided
    if mapper:
        # Consider wrapping in a try-except to handle unexpected mapper errors
        return_value = mapper(return_value)
    
    return return_value

def ftp_file_prefix(namespace):
    """
    Given a namespace string with dot-separated tokens, returns the
    string with the final token replaced by 'ftp'.
    Example: a.b.c => a.b.ftp
    """
    # Check if namespace has at least one dot-separated token
    tokens = namespace.split(".")
    if len(tokens) > 1:
        return ".".join(tokens[:-1]) + '.ftp'
    else:
        return namespace  # Return the original namespace if no dot is found

def string_to_bool(string):
    """
    Returns True if the given string is 'true' case-insensitive,
    False if it is 'false' case-insensitive.
    Raises ValueError for any other input.
    """
    # Handle possible edge cases with more comprehensive comparison
    if string.strip().lower() == 'true':  # Strip whitespace just in case
        return True
    if string.strip().lower() == 'false':
        return False
    # Consider providing a more descriptive error message
    raise ValueError(f"String '{string}' is neither 'true' nor 'false'")

def config_from_dict(dict):
    """
    Given a dict representing a row from a namespaces CSV file,
    returns a DAG configuration as a pair whose first element is the
    DAG name and whose second element is a dict describing the DAG's properties
    """
    namespace = dict['Namespace']
    return (
        dict['Airflow DAG'],
        {
            "earliest_available_delta_days": 0,
            "lif_encoding": 'json',
            "earliest_available_time":
                get_value(dict, 'Available Start Time', '07:00'),
            "latest_available_time":
                get_value(dict, 'Available End Time', '08:00'),
            "require_schema_match":
                get_value(dict, 'Requires Schema Match', 'True',
                          mapper=string_to_bool),
            "schedule_interval":
                get_value(dict, 'Schedule', '1 7 * * * '),
            "delta_days":
                get_value(dict, 'Delta Days', 'DAY_BEFORE',
                          lookup=DeltaDays),
            "ftp_file_wildcard":
                get_value(dict, 'File Naming Pattern', None),
            "ftp_file_prefix":
                get_value(dict, 'FTP File Prefix',
                          ftp_file_prefix(namespace)),
            "namespace": namespace
        }
    )

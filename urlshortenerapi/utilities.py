import hashlib

# TODO: Use a library that could hash this cleaner and ensure unique values

def generate_id_from_url(url):
    id = int(hashlib.sha256(url.encode('utf-8')).hexdigest(), 16) % 10 ** 8
    return id


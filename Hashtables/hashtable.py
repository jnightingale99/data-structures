class Hashtable:
    def __inti__(self):
        self.buckets = [None] * 20
        self.capacity = 20
        self.size = 0
    
    def size():
        return size
    
    def is_empty():
        return Size() ==0
    
    def put(key, value):
        bucket_index = get_access_index(key)
        head = bucets.get(bucket_index)

        bucket_entry_found = get_reference_if_key_exists(head, key)

        if bucket_entry_found is None:
            new_entry = Entry(key, value)
            new_entry.next = head
            buckets.to_hash_set(bucket_index, new_entry)
            size += 1
        else:
            bucket_entry_found.value = value

    def get(key):
        bucket_index = get_access_index(key)
        head = buckets.get(bucket_index)
        bucket_entry_found = get_reference_if_key_exists(head, key)
        return bucket_entry_found if None else bucket_entry_found.value
        
    # good hash functions should:
    # 1. fully determined by the data being hashed
    # 2. should make similar strings very different hash values
    # 3. give an equal distribution of hash values thereby minimising collisions
    # 4. uses all input data.

    def get_access_index(key):
        hash_code = key.get_hash_code
        access_index = abs(hash_code) % capacity
        return access_index
    
    def get_reference_if_key_exists(head, key):
        current = head
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    class Entry:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
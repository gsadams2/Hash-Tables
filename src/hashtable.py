# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

        


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity



    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        key_hash_index = self._hash_mod(key)

        if self.storage[key_hash_index] is None:
            self.storage[key_hash_index] = LinkedPair(key, value)    
    
        else:
            pair = self.storage[key_hash_index]
            #if key is the same then update the value 
            if pair.key == key:
                pair.value = value
                return
            
            #while there is a next
            while pair.next is not None:
                if pair.next.key == key:
                    pair.next.value = value
                    return 
                else:
                    #repoint the pointer 
                    pair = pair.next
            #do something here outside of while loop..... if there isn't a match with the key then insert new pair as a next 
            pair.next = LinkedPair(key, value)




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        key_hash_index = self._hash_mod(key)

        if self.storage[key_hash_index] is None:
            print("The key is not found")
        else:
            self.storage[key_hash_index] = None 
            # not accounting for collision


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        key_hash_index = self._hash_mod(key)

        pair = self.storage[key_hash_index]

        if pair is None:
            return None
        else:
            while pair:
                if pair.key == key:
                    return pair.value
                else:
                    ##if there isn't a match, go to the next one 
                    pair = pair.next
            #if there is never a match, return None    
            return None
      

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

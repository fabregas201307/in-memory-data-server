import redis
import json

class RedisDataStoreClient:
    def __init__(self, host='localhost', port=16379, password=None):
        self.client = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

    def start_transaction(self):
        """Start a Redis transaction."""
        self.transaction = self.client.pipeline()
        print({"status": "Ok", "mesg": "Transaction started"})

    def commit_transaction(self):
        """Commit all commands in the transaction."""
        try:
            self.transaction.execute()
            print({"status": "Ok", "mesg": "Transaction committed"})
        except Exception as e:
            print({"status": "Error", "mesg": str(e)})

    def rollback_transaction(self):
        """Discard all commands in the transaction."""
        self.transaction.reset()
        print({"status": "Ok", "mesg": "Transaction rolled back"})

    def put(self, key, value):
        """Put a key-value pair."""
        if hasattr(self, 'transaction'):
            self.transaction.set(key, value)
        else:
            self.client.set(key, value)
        print({"status": "Ok", "mesg": f"Key '{key}' set to '{value}'"})

    def get(self, key):
        """Get a value by key."""
        try:
            value = self.client.get(key)
            if value is not None:
                print({"status": "Ok", "result": value})
            else:
                print({"status": "Error", "mesg": "Key not found"})
        except Exception as e:
            print({"status": "Error", "mesg": str(e)})

    def delete(self, key):
        """Delete a key-value pair."""
        if hasattr(self, 'transaction'):
            self.transaction.delete(key)
        else:
            self.client.delete(key)
        print({"status": "Ok", "mesg": f"Key '{key}' deleted"})

# Test the RedisDataStoreClient with an example transaction
if __name__ == "__main__":
    store = RedisDataStoreClient()

    # Test commands as per requirements
    # Start a transaction
    store.start_transaction()

    # PUT commands within the transaction
    store.put("favorite_color", "blue")
    store.put("name", "Alice")

    # GET command within the transaction (will not retrieve uncommitted data)
    store.get("favorite_color")

    # Commit the transaction
    store.commit_transaction()

    # GET command after commit (should retrieve committed data)
    store.get("favorite_color")

    # Start a new transaction to test ROLLBACK
    store.start_transaction()
    store.put("name", "Bob")  # Temporary update

    # GET should still return the committed value since this transaction is not yet committed
    store.get("name")

    # Rollback the transaction, discarding changes
    store.rollback_transaction()

    # GET command after rollback (should still retrieve the original committed data)
    store.get("name")

    # Clean up by deleting keys
    store.delete("favorite_color")
    store.delete("name")

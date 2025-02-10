import time
import hashlib
import json

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        """
        Initializes a block in the blockchain.
        :param index: Block number or index.
        :param transactions: A list (or dummy data) of transactions.
        :param timestamp: Time of block creation.
        :param previous_hash: Hash of the previous block.
        :param nonce: Number used for proof-of-work.
        """
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the block's hash using SHA-256.
        Only includes essential data (and nonce) in the hash computation.
        """
        # Create a string with block properties (except self.hash itself)
        block_string = (
            str(self.index) +
            self.previous_hash +
            str(self.timestamp) +
            json.dumps(self.transactions, sort_keys=True) +
            str(self.nonce)
        )
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Simple proof-of-work: increment nonce until the hash has the required number of leading zeros.
        :param difficulty: The number of leading zeros required.
        """
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block #{self.index} mined: {self.hash}")


class Blockchain:
    def __init__(self):
        """
        Initializes the blockchain with a genesis block and a preset difficulty for mining.
        """
        self.chain = [self.create_genesis_block()]
        # Difficulty sets how many leading zeros the block hash must have.
        self.difficulty = 3

    def create_genesis_block(self):
        """
        Generates the genesis (first) block of the blockchain.
        """
        return Block(0, "Genesis Block", time.time(), "0")

    def get_latest_block(self):
        """
        Returns the most recent block in the chain.
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Adds a new block to the chain after setting its previous hash and performing mining.
        :param new_block: Block to be added.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the blockchain integrity.
        Checks that each block's hash is correct and that the chain of hashes is intact.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Recalculate the hash and compare
            if current_block.hash != current_block.calculate_hash():
                print(f"Block #{current_block.index} has invalid hash.")
                return False

            # Check if the block's previous hash matches the hash of the previous block
            if current_block.previous_hash != previous_block.hash:
                print(f"Block #{current_block.index} has incorrect previous hash.")
                return False

        return True


def main():
    # Create a new blockchain
    my_blockchain = Blockchain()

    # Add block 1 with dummy transaction data
    print("Mining block 1...")
    block1 = Block(
        index=1,
        transactions=[{"sender": "Alice", "receiver": "Bob", "amount": 50}],
        timestamp=time.time(),
        previous_hash=my_blockchain.get_latest_block().hash
    )
    my_blockchain.add_block(block1)

    # Add block 2 with dummy transaction data
    print("Mining block 2...")
    block2 = Block(
        index=2,
        transactions=[{"sender": "Bob", "receiver": "Charlie", "amount": 25}],
        timestamp=time.time(),
        previous_hash=my_blockchain.get_latest_block().hash
    )
    my_blockchain.add_block(block2)

    # Display the blockchain
    print("\n--- Full Blockchain ---")
    for block in my_blockchain.chain:
        print(f"Block #{block.index}")
        print(f"Timestamp: {time.ctime(block.timestamp)}")
        print(f"Transactions: {block.transactions}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Nonce: {block.nonce}")
        print(f"Hash: {block.hash}")
        print("-" * 50)

    # Validate chain integrity
    print("\nBlockchain valid?", my_blockchain.is_chain_valid())

    # Demonstrate tampering:
    print("\n*** Tampering with block data ***")
    # Change transaction data of block 1 (tampering)
    my_blockchain.chain[1].transactions = [{"sender": "Alice", "receiver": "Bob", "amount": 5000}]
    # Recalculate the hash for the tampered block (in real scenario, recalculation wouldn’t occur automatically)
    my_blockchain.chain[1].hash = my_blockchain.chain[1].calculate_hash()

    # Validate the chain after tampering (this should fail)
    print("Blockchain valid after tampering?", my_blockchain.is_chain_valid())


if __name__ == "__main__":
    main()

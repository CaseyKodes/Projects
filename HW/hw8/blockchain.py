from hashmap import hashmap

class Transaction:
    """initialize object, parameters must be declared"""

    def __init__(self, from_user, to_user, amount): 
        # settign atributes ot parameters
        self.from_user = from_user 
        self.to_user = to_user 
        self.amount = amount 

    def __repr__(self):  

        #returns transaction from above parameters
        return f'Transaction("{self.from_user}", "{self.to_user}", {self.amount})'

class Block:
    def __init__(self, transactions=None, previous_blockhash=None): 
        """initialize object, default is None"""

        self.transactions = transactions 
        self.previous_blockhash = previous_blockhash 

        if self.transactions is None: #object checking
            self.transactions = list() #creates empty list

        if self.previous_blockhash is None: #object checking
            self.previous_blockhash = 0000 #sets to 0

    def add_transaction(self, transaction):
        """add transcation, if this is first transaction, create empty set"""

        self.transactions.append(transaction) 

    def __hash__(self):
        hashes = "" # empty

        for transaction in self.transactions: #for loop to hash

            hash_1 = str(hash((transaction.from_user, transaction.to_user, transaction.amount))) #hashes transaction
            hashes += hash_1

        compress_hash = hash(hashes) #hashes again at end
        return compress_hash 

    def __eq__(self, other):
        return hash(self) == hash(other) #returns true when two blocks are the same meaning they will hash to the same value

    def __repr__(self):
        return f"Block({self.transactions}, {self.previous_blockhash})" #return string of block object

class Ledger:

    def __init__(self):
        """ledgers are empty hashmaps, which are just dictionaries"""

        self._hashmap = hashmap() 

    def has_funds(self, user, amount):
        """returns true or false if user has enough"""

        if user not in self._hashmap: 
            return False 

        balance = self._hashmap.get(user) 

        return balance >= amount # returns if the user has the funds

    def deposit(self, user, amount):
        """adds amount to users balance"""

        if amount <= 0: 
            raise RuntimeError("cannot deposit nothing or negative balance") 

        if user not in self._hashmap: 
            self._hashmap.add(user) 

        balance = self._hashmap.get(user) #user recieves balance
        new_balance = balance + amount #new balance is created by adding old blance to amount
        self._hashmap.map[user] = new_balance #gives amount to user

    def transfer(self, user, amount):
        # more like a withdrawl functions

        if user not in self._hashmap:
            raise KeyError("user is not in ledger") 

        if not self.has_funds(user, amount): 
            raise RuntimeError("user does not have sufficient funds for this transfer") 

        balance = self._hashmap.get(user) #balance goes to user
        new_balance = balance - amount #creates new balance by subtracting amount from old balance
        self._hashmap.map[user] = new_balance #sets balance to user

    def __repr__(self):
        return f"Ledger: {self._hashmap.map}" 

class Blockchain:
    """Contains the chain of blocks."""

    #########################
    # Do not use these three values in any code that you write.
    _ROOT_BC_USER = "ROOT"  # Name of root user account.
    _BLOCK_REWARD = 1000  # Amoung of HuskyCoin given as a reward for mining a block
    _TOTAL_AVAILABLE_TOKENS = (
        999999  # Total balance of HuskyCoin that the ROOT user receives in block0
    )
    #########################

    def __init__(self):

        self._blockchain = list()  # Use the Python List for the chain of blocks

        self._bc_ledger = Ledger()  # The ledger of HuskyCoin balances

        # Create the initial block0 of the blockchain, also called the "genesis block"
        self._create_genesis_block()

    # This method is complete. No additional code needed.
    def _create_genesis_block(self):
        """Creates the initial block in the chain.
        This is NOT how a blockchain usually works, but it is a simple way to give the
        Root user HuskyCoin that can be subsequently given to other users"""
        trans0 = Transaction(self._ROOT_BC_USER, self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)
        block0 = Block([trans0])
        self._blockchain.append(block0)
        self._bc_ledger.deposit(self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)

    # This method is complete. No additional code needed.
    def distribute_mining_reward(self, user):
        """
        You need to give HuskyCoin to some of your users before you can transfer HuskyCoing
        between users. Use this method to give your users an initial balance of HuskyCoin.
        (In the Bitcoin network, users compete to solve a meaningless mathmatical puzzle.
        Solving the puzzle takes a tremendious amount of copmputing power and consuming a lot
        of energy. The first node to solve the puzzle is given a certain amount of Bitcoin.)
        In this assigment, you do not need to understand "mining." Just use this method to
        provide initial balances to one or more users."""
        trans = Transaction(self._ROOT_BC_USER, user, self._BLOCK_REWARD)
        block = Block([trans])
        self.add_block(block)

    # TODO - add the rest of the code for the class here
    def add_block(self, transactions=None):
        """add block to blockchain"""

        if transactions != None: #when transaction does not equal None

            for transaction in transactions:

                user = transaction.from_user # sets new user
                amount = transaction.amount # sets new amount

                if not self._bc_ledger.has_funds(user, amount):
                    return False

        new_block = Block(transactions) #creating new block

        self._blockchain.append(new_block) #add new block
        prev_blockidx = self._blockchain.index(new_block) - 1 #puts previous block hash as new
        prev_block = self._blockchain[prev_blockidx] #prev block equals new
        prev_blockhash = hash(prev_block) #hash prev block

        new_block.previous_blockhash = prev_blockhash #creates new block

        for transaction in transactions: #update ledger

            from_user = transaction.from_user #updating user
            to_user = transaction.to_user #update user
            amount = transaction.amount #update amount

            self._bc_ledger.transfer(from_user, amount) #transfer user and amount
            self._bc_ledger.deposit(to_user, amount) #deposit user and amount

        return True

    def validate_chain(self):
        "return a list of blocks who's hash has been improperly changed"

        # compares hash of blocks to the prev hash of its next block
        changed = [] #empty list

        for block_idx in range(len(self._blockchain)):

            if block_idx == len(self._blockchain) - 1:
                continue

            next_block_prev_hash = self._blockchain[block_idx + 1].previous_blockhash
            blockidxhash = hash(self._blockchain[block_idx])
            
            if next_block_prev_hash != blockidxhash:
                changed.append(self._blockchain[block_idx])
        return changed

    def __repr__(self):
        """returns string representation of block chain"""

        s = "Blockchain: "
        for block in self._blockchain:
            s += repr(block) + ", "
        s = s[:-2]
        return s

    def print_chain(self):
        """prints repr of self"""

        print(self)

    def print_ledger(self):
        """prints repr of ledger"""

        print(self._bc_ledger)

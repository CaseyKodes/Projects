from hashmap import hashmap
from blockchain import Blockchain, Block, Transaction, Ledger
import unittest

class test_transaction(unittest.TestCase):
    def test_transaction_init(self):
        # test init for transaction class

        t = Transaction("user1", "user2",900)
        self.assertEqual(t.from_user, "user1")
        self.assertEqual(t.to_user, "user2")
        self.assertEqual(t.amount, 900)

class test_block(unittest.TestCase):
    def test_block_init(self):
        # tests init for block class

        newblock = Block()
        list1 = []
        prevhash = 0000
        self.assertEqual(newblock.transactions, list1)
        self.assertEqual(newblock.previous_blockhash, prevhash)

    def test_add_transaction(self):
        # test add trasaction for block class

        newblock = Block()
        t = Transaction("user1", "user2", 40)
        newblock.add_transaction(t)

        list2 = []
        list2.append(t)
        self.assertEqual(newblock.transactions, list2)

    def test_hash(self):
        # tests hash for block class

        # These two blocks have the same exact transactions, so are equal
        newblock = Block()
        t = Transaction("hey", "now", 420)
        newblock.add_transaction(t)
        newblockhash = hash(newblock)

        newblockcopy = Block()
        tcopy = Transaction("hey", "now", 420)
        newblockcopy.add_transaction(tcopy)
        newblockcopyhash = hash(newblockcopy)
        self.assertEqual(newblockhash, newblockcopyhash)

        difblock = Block()
        dift = Transaction("hey", "now", 40)  # changed transaction amount, results in diff hash
        difblock.add_transaction(dift)
        difblockhash = hash(difblock)
        self.assertNotEqual(newblockcopyhash, difblockhash)

        difblock = Block()
        dift = Transaction("hey", "hey", 420)  # changed transaction second user, results in diff hash
        difblock.add_transaction(dift)
        difblockhash = hash(difblock)
        self.assertNotEqual(newblockcopyhash, difblockhash)

        difblock = Block()
        dift = Transaction("now", "now", 40)  # changed transaction first user, results in diff hash
        difblock.add_transaction(dift)
        difblockhash = hash(difblock)
        self.assertNotEqual(newblockcopyhash, difblockhash)

class test_ledger(unittest.TestCase):
    def test_ledger_init(self):
        # tests init for ledger class

        l = Ledger()
        dic = {}
        self.assertEqual(l._hashmap.map, dic)

    def test_ledger_has_funds(self):
        # tests has funds for ledger class

        # user not in ledger, returns false
        l = Ledger()
        self.assertFalse(l.has_funds("user1", 1))

        # returns true if user has more than that many funds
        newl = Ledger()
        newl._hashmap.add("user2", 51)
        self.assertTrue(newl.has_funds("user2", 50))

        # returns true when the user has exactly that many funds
        samel = Ledger()
        samel._hashmap.add("user3", 700)
        self.assertTrue(samel.has_funds("user3", 700))

        # returns false if user does not have that many funds
        invalidl = Ledger()
        invalidl._hashmap.add("user4", 4999)
        self.assertFalse(invalidl.has_funds("user4", 5000))

    def test_ledger_deposit(self):
        # tests deposit for ledger class

        # user should have 69 funds if we deposit 69
        l = Ledger()
        l._hashmap.add("user1")
        l.deposit("user1", 69)
        self.assertTrue(l.has_funds("user1", 69))

        # cannot deposit 0 (or negative)
        falsel = Ledger()
        falsel._hashmap.add("user2")
        self.assertRaises(RuntimeError, falsel.deposit, "user2", 0)
        self.assertRaises(RuntimeError, falsel.deposit, "user2", -5)


        # if user doesnt exist, they will be added and their balance adjusted
        newl = Ledger()
        newl.deposit("user3", 4)
        self.assertEqual(newl._hashmap.get("user3"), 4)

    def test_ledger_transfer(self):
        # test transfer for ledger class

        # cannot transfer if user does not exist
        l = Ledger()
        self.assertRaises(KeyError, l.transfer, "user1", 10)

        # cannot transfer if user does not have sufficient funds
        invalidl = Ledger()
        invalidl._hashmap.add("user2", 10)
        self.assertRaises(RuntimeError, invalidl.transfer, "user2", 11)

        # transfer should subtract from balance
        subtractl = Ledger()
        subtractl._hashmap.add("user3", 20)
        subtractl.transfer("user3", 7)
        self.assertEqual(subtractl._hashmap.get("user3"), 13)

    def test_ledger_repr(self):
        # test repr ofr ledger class

        l = Ledger()
        l._hashmap.add("user", 10)
        self.assertEqual(repr(l), f"Ledger: {l._hashmap.map}")

class test_blockchain(unittest.TestCase):
    def test_blockchain_init(self):
        # test init for blockchain class

        bc = Blockchain()
        b = bc._blockchain[0]  # genesis block
        self.assertEqual(len(bc._blockchain), 1)  # len is 1 for genesis block
        self.assertIsInstance(b, Block)  # item in blockchain is a block
        self.assertTrue(bc._bc_ledger.has_funds("ROOT", 999999))  # root has 999999 funds in new ledger
        self.assertEqual(b.previous_blockhash, 0000)  # previous hash of genesis block is 0000

    def test_blockchain_add_block(self):
        # tests ass block for blockchain class

        # previous block hash is store in new block and returns true
        bc = Blockchain()
        t1 = Transaction("user1", "user2", 50)
        bc._bc_ledger.deposit("user1", 50)
        bc._bc_ledger.deposit("user2", 10)
        b1hash = hash(bc._blockchain[0])  # hash of genesis block

        self.assertTrue(bc.add_block([t1]))  # block 1 after genesis block and that it returns true
        b2prevhash = bc._blockchain[1].previous_blockhash  # block 1s previous block hash
        self.assertEqual(b2prevhash, b1hash)

        # return false if transaction of block is invalid
        falsebc = Blockchain()
        falsebc._bc_ledger.deposit("user3", 25)
        falsebc._bc_ledger.deposit("user4", 10)
        t2 = Transaction("user3", "user4", 50)
        self.assertFalse(falsebc.add_block([t2]))

        # ledger should be updated
        bc2 = Blockchain()
        bc2._bc_ledger.deposit("user5", 70)
        bc2._bc_ledger.deposit("user6", 10)

        user5before = bc2._bc_ledger._hashmap.get("user5")
        self.assertEqual(user5before, 70)
        user6before = bc2._bc_ledger._hashmap.get("user6")
        self.assertEqual(user6before, 10)

        t3 = Transaction("user5", "user6", 50)
        bc2.add_block([t3])

        user5before = bc2._bc_ledger._hashmap.get("user5")
        self.assertEqual(user5before, 20)
        user6before = bc2._bc_ledger._hashmap.get("user6")
        self.assertEqual(user6before, 60)

    def test_blockchain_validate_chain(self):
        # tests validate chain for blockchain class

        # changing from_user
        bc1 = Blockchain()
        t1 = Transaction("user1", "user2", 50)
        bc1._bc_ledger.deposit("user1", 100)
        bc1._bc_ledger.deposit("user2", 100)
        bc1.add_block([t1])  # make blockchain with two blocks

        bc1._blockchain[0].transactions[0].from_user = "victimuser"

        self.assertEqual(bc1.validate_chain(), [bc1._blockchain[0]])  # block 0 is listed as a invalid block

        # changing to_user
        bc2 = Blockchain()
        t2 = Transaction("user3", "user4", 50)
        bc2._bc_ledger.deposit("user3", 100)
        bc2._bc_ledger.deposit("user4", 100)
        bc2.add_block([t2])  # make blockchain with two blocks

        bc2._blockchain[0].transactions[0].to_user = "malicioususer"

        self.assertEqual(bc2.validate_chain(), [bc2._blockchain[0]])  # block 0 is listed as a invalid block

        # changing amount
        bc3 = Blockchain()
        t3 = Transaction("user5", "user6", 50)
        bc3._bc_ledger.deposit("user5", 100)
        bc3._bc_ledger.deposit("user6", 100)
        bc3.add_block([t3])  # make blockchain with two blocks

        bc3._blockchain[0].transactions[0].amount = 999

        self.assertEqual(bc3.validate_chain(), [bc3._blockchain[0]])  # block 0 is listed as a invalid block

    def test_blockchain_repr(self):
        # tests repr for blockchain class

        bc = Blockchain()
        t = Transaction("user1", "user2", 50)
        bc._bc_ledger.deposit("user1", 100)
        bc._bc_ledger.deposit("user2", 100)
        bc.add_block([t])  # make blockchain with two blocks
        expected_str = f"Blockchain: {bc._blockchain[0]}, {bc._blockchain[1]}"
        self.assertEqual(repr(bc), expected_str)

unittest.main()
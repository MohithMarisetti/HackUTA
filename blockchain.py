# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 01:05:58 2019

@author: Thekku
"""

import time
import hashlib 

class Block(object):    
   def __init__(self, index="", proof="", previous_hash="", transactions=""):
       self.index = index
       self.proof = proof
       self.previous_hash = previous_hash
       self.transactions = transactions
       self.timestamp = time.time()    
   @property
   def get_block_hash(self):
       block_string = "{}{}{}{}{}".format(self.index, self.proof, self.previous_hash, self.transactions, self.timestamp)
       return hashlib.sha256(block_string.encode()).hexdigest()
   def get_transaction_details(self,hash):
       if(hash==self.get_block_hash):
           return self.transactions
   def getBlockObj(self,hash):
       return self
   
class BlockChain(object):    
   def __init__(self):
       self.chain = []
       self.current_node_transactions = []
       self.create_genesis_block()  
       
   def create_new_transaction(self, username, amount, id):
       self.current_node_transactions.append({
       'username': username,
       'amount': amount,
       'id': id
       })        
       return self.get_last_block.index + 1 # Returning new block's index where this transaction will be stored    
   
   def create_new_block(self, proof, previous_hash):
       block = Block(
       index=len(self.chain),
       proof=proof,
       previous_hash=previous_hash,
       transactions=self.current_node_transactions)
       self.current_node_transactions = [] # Reset the transaction list        
       self.chain.append(block)
       return block
       
   def create_genesis_block(self):
       self.create_new_block(proof=0, previous_hash=0)   
   
   @staticmethod
   def create_proof_of_work(previous_proof):
       proof = previous_proof + 1
       while (proof + previous_proof) % 7 != 0:
           proof += 1        
       return proof  
       
   @property
   def get_last_block(self):
       return self.chain[-1]
   @property
   def get_last_blockchain(self):
       return self.chain[:-1]
       
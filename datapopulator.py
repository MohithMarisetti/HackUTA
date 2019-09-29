# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 01:31:36 2019

@author: Thekku
"""
from blockchain import BlockChain 
from blockchain import Block
import time
import hashlib 

class datapopulator:
    
    def __init__(self):
        self.flag=0
        self.blockchain = BlockChain()
    
    def populateData(self):
        
        last_block = self.blockchain.get_last_block
        last_proof = last_block.proof
        proof = self.blockchain.create_proof_of_work(last_proof)
        self.blockchain.create_new_transaction( username = "Chris Evans",amount=600000, id=6)
        last_hash = last_block.get_block_hash
        block = self.blockchain.create_new_block(proof, last_hash)
        
        last_block = self.blockchain.get_last_block
        last_proof = last_block.proof
        proof = self.blockchain.create_proof_of_work(last_proof)
        self.blockchain.create_new_transaction( username = "Gal Gadot",amount=400000, id=7)
        last_hash = last_block.get_block_hash
        block = self.blockchain.create_new_block(proof, last_hash)
        
        last_block = self.blockchain.get_last_block
        last_proof = last_block.proof
        proof = self.blockchain.create_proof_of_work(last_proof)
        self.blockchain.create_new_transaction( username = "Barack Obama",amount=300000, id=8)
        last_hash = last_block.get_block_hash
        block = self.blockchain.create_new_block(proof, last_hash)
        
        last_block = self.blockchain.get_last_block
        last_proof = last_block.proof
        proof = self.blockchain.create_proof_of_work(last_proof)
        self.blockchain.create_new_transaction( username = "Prescott",amount=700000, id=9)
        last_hash = last_block.get_block_hash
        block = self.blockchain.create_new_block(proof, last_hash)
        last_block = self.blockchain.get_last_block
        last_proof = last_block.proof
        proof = self.blockchain.create_proof_of_work(last_proof)
        self.blockchain.create_new_transaction( username = "Scarllet J",amount=5000000, id=10)
        last_hash = last_block.get_block_hash
        block = self.blockchain.create_new_block(proof, last_hash)
        
        last_block = self.blockchain.get_last_block
        last_proof = last_block.proof
        proof = self.blockchain.create_proof_of_work(last_proof)
        self.blockchain.create_new_transaction( username = "Serena Williams",amount=4000000, id=11)
        last_hash = last_block.get_block_hash
        block = self.blockchain.create_new_block(proof, last_hash)
        
        last_block = self.blockchain.get_last_block
        last_proof = last_block.proof
        proof = self.blockchain.create_proof_of_work(last_proof)
        self.blockchain.create_new_transaction( username = "Tom Cruise",amount=300000, id=12)
        last_hash = last_block.get_block_hash
        block = self.blockchain.create_new_block(proof, last_hash)
        
        last_block = self.blockchain.get_last_block
        last_proof = last_block.proof
        proof = self.blockchain.create_proof_of_work(last_proof)
        self.blockchain.create_new_transaction( username = "Harshit",amount=5000, id=13)
        last_hash = last_block.get_block_hash
        block = self.blockchain.create_new_block(proof, last_hash)
        
        last_block = self.blockchain.get_last_block
        last_proof = last_block.proof
        proof = self.blockchain.create_proof_of_work(last_proof)
        self.blockchain.create_new_transaction( username = "Eapen",amount=4000, id=14)
        last_hash = last_block.get_block_hash
        block = self.blockchain.create_new_block(proof, last_hash)
        
        last_block = self.blockchain.get_last_block
        last_proof = last_block.proof
        proof = self.blockchain.create_proof_of_work(last_proof)
        self.blockchain.create_new_transaction( username = "Navaneeth",amount=3000, id=15)
        last_hash = last_block.get_block_hash
        block = self.blockchain.create_new_block(proof, last_hash)
        
        last_block = self.blockchain.get_last_block
        last_proof = last_block.proof
        proof = self.blockchain.create_proof_of_work(last_proof)
        self.blockchain.create_new_transaction( username = "Mohith",amount=7000, id=16)
        last_hash = last_block.get_block_hash
        block = self.blockchain.create_new_block(proof, last_hash)
        
        
        
        for block in self.blockchain.chain:
            currentBlockhash = block.get_block_hash;
            previousBlockhash = block.previous_hash;
            block_string = "{}{}{}{}{}".format(block.index, block.proof, block.previous_hash, block.transactions, block.timestamp)
            if ( currentBlockhash != hashlib.sha256(block_string.encode()).hexdigest()):
                print("Current Hashes not equal")
                self.flag=-1
            if ( previousBlockhash != block.previous_hash):
                print("Previous Hashes not equal")   
                self.flag=-1
                 
    def findIDDetails(self,id):
        self.populateData()
        resname=""
        resamount=0
        if(self.flag!=-1):
            print("Valid Blockchain")
            #lasthash=blockchain.get_last_block.previous_hash
            #b = BlockChain()
            ct=self.blockchain.get_last_blockchain
            print(ct)
            for bl in ct:
                if(bl.previous_hash!=0):
                    if(bl.transactions[0]['id']==id):
                        resname=bl.transactions[0]['username']
                        resamount=bl.transactions[0]['amount']
            print(resname) 
            print("insinde det")
            return resname,resamount
        return "not found"


        
from brownie import Lottery,accounts , network , config
from web3 import Web3

def test_lottery_entrance():
    account = accounts[0]
    feed=config['networks']["mainnet_fork"]['eth_usd_price_feed']
    lottery = Lottery.deploy(feed,{"from":account}) 
   
    assert lottery.getEntranceFee() < Web3.toWei(.018,"ether")
    



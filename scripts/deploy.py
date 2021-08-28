import os 
from dotenv import load_dotenv
from brownie import Wei, accounts, GuessNumber

load_dotenv()

def main():
    deploy_account = accounts.add(os.environ['PRIVATE_KEY_1'])
    deployment_details = {
        'from': accounts[0],
        'value': Wei('10 ether'),
    }
    guess_number = GuessNumber.deploy(9,deployment_details)
    print('Current accounts balances:\n')
    for contractAccount in accounts:
        print('{}'.format(contractAccount.balance()) )
    return guess_number

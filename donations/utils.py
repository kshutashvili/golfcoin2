from web3 import Web3, HTTPProvider
from django.conf import settings
from config.models import DonationAddresses


def get_web3():

    return Web3(HTTPProvider(settings.WEB3_PROVIDER))


def get_crowdsale_address():
    return DonationAddresses.get_solo().eth_address


def get_token_contract(web3):
    return web3.eth.contract(abi=settings.TOKEN_ABI,
                             address=settings.TOKEN_ADDRESS)


def get_token_balance(user):

    balance = 0
    web3 = get_web3()
    token_contract = get_token_contract(web3)

    for address in user.addresses.all():
        try:
            balance += web3.fromWei(
                token_contract.call().balanceOf(address.e20_wallet),
                'ether'
            )
        except:
            pass

    return balance

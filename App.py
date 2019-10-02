from web3 import Web3,HTTPProvider
import json

# truffleで生成したjsonを読み込んでaddressとabiを取得する
f = open("UnitFactory.json", 'r')
json_data = json.load(f)
abi = json_data["abi"]
address = json_data["networks"]["5777"]["address"]
print("address: " + address)

# コントラクトへ接続してインスタンス生成
web3 = Web3(HTTPProvider("http://127.0.0.1:7545"))
UnitFactory = web3.eth.contract(address=address, abi=abi)

unit_num = UnitFactory.functions.getUnitNum().call()
print("unit_num: " + str(unit_num))

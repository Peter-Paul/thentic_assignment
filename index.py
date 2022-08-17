import requests, json

proceed = 1

while proceed!="exit":
    print("Welcome to Thentic's easy to use API. Select task you want to perform from list provided!")
    try:
        api_method = input(
            '[1] Show NFT contracts\n[2] Show NFTs\n[3] Create NFT contract\n[4] Mint NFT\n[5] Transfer NFT\n[6] Show invoices\n[7] Create invoice\n[8] Cancel invoice\n[9] Show wallets\n[10] Create new wallet\n[11] Exit\n\n[Select API method (1-10) ]:'
        )
        if api_method == '11':
            proceed = 'exit'
        else:
            try:
                api_key
            except:
                api_key = input(
                    '[API key (skip for new key):\n')
                if not api_key:
                    api_key = requests.get('https://thentic.tech/api/key').text
                    print('[Your API key: ' + api_key)
            try:
                chain_id
            except:
                chain_id = input(
                    '[EVM chain id (skip for 97 - Binance testnet):\n'
                )
                if not chain_id:
                    chain_id = '97'

            if api_method == '1':
                print('Getting NFT contracts..')

                url = 'https://thentic.tech/api/contracts'
                headers = {'Content-Type': 'application/json'}
                data = {'key': api_key, 'chain_id': chain_id}

                r = requests.get(url, json=data, headers=headers)
                try:
                    if len(json.loads(r.text)['contracts']) == 0:
                        print('No contracts created yet')

                    for i in json.loads(r.text)['contracts']:
                        try:
                            print( i['name'] + ' (' + i['short_name'] +
                                '):\n  status: ' +
                                i['status'] + '\n  [request id: ' +
                                i['request_id'] +
                                '\n  [contract: ' + i['contract'])
                        except:
                            print( i['name'] + ' (' + i['short_name'] +
                                '):\n  status: ' +
                                i['status'] + '\n  [request id: ' +
                                i['request_id'] +
                                '\n  transaction url: ' +
                                i['transaction_url'] +
                                '\n  transaction pixel: ' +
                                i['transaction_pixel'])

                except:
                    pass

                if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                    print(r.text)
                    api_key = input(
                        '[API key (skip for new key)]:\n'
                    )
                    if not api_key:
                        api_key = requests.get('https://thentic.tech/api/key').text
                        print('[Your API key: ' + api_key)
                elif r.text == 'Chain not found':
                    print(r.text)
                    chain_id = input(
                        '[EVM chain id (skip for 97 - Binance testnet)]:\n'
                    )
                    if not chain_id:
                        chain_id = '97'
                else:
                    proceed = input('Press any key to continue or type (exit) to end proccess\n')
            elif api_method == '2':
                print('Getting NFTs..')

                url = 'https://thentic.tech/api/nfts'
                headers = {'Content-Type': 'application/json'}
                data = {'key': api_key, 'chain_id': chain_id}

                r = requests.get(url, json=data, headers=headers)
                try:
                    if len(json.loads(r.text)['nfts']) == 0:
                        print('No NFTs created yet')

                    for i in json.loads(r.text)['nfts']:

                        print( i['name'] + ' (' + i['short_name'] +
                            '):\n  status: ' +
                            i['status'] + '\n  [request id: ' +
                            i['request_id'] + '\n  [contract: ' +
                            i['contract'] + '\n  [id: ' + i['id'] +
                            '\n  [data: ' + i['data'] +
                            '\n  transaction url: ' +
                            i['transaction_url'] +
                            '\n  transaction pixel: ' +
                            i['transaction_pixel'])

                except:
                    pass

                if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                    print(r.text)
                    api_key = input(
                        '[API key (skip for new key)]:\n'
                    )
                    if not api_key:
                        api_key = requests.get('https://thentic.tech/api/key').text
                        print('[Your API key: ' + api_key)
                elif r.text == 'Chain not found':
                    print(r.text)
                    chain_id = input(
                        '[EVM chain id (skip for 97 - Binance testnet)]:\n'
                    )
                    if not chain_id:
                        chain_id = '97'
                else:
                    proceed = input('Press any key to continue or type (exit) to end proccess\n')

            elif api_method == '3':

                name = input('[NFT Name]:\n')
                short_name = input('[NFT Symbol]:\n')

                print('Creating NFT contract..')

                url = 'https://thentic.tech/api/nfts/contract'
                headers = {'Content-Type': 'application/json'}
                data = {
                    'key': api_key,
                    'chain_id': chain_id,
                    'name': name,
                    'short_name': short_name
                }

                r = requests.post(url, json=data, headers=headers)

                print(
                     name + ' (' + short_name + ')' +
                    '\n  status: pending\n  [request id: '
                    + json.loads(r.text)['request_id'] +
                    '\n  transaction url: ' +
                    json.loads(r.text)['transaction_url'])

                if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                    print(r.text)
                    api_key = input(
                        '[API key (skip for new key)]:\n'
                    )
                    if not api_key:
                        api_key = requests.get('https://thentic.tech/api/key').text
                        print('[Your API key: ' + api_key)
                elif r.text == 'Chain not found':
                    print(r.text)
                    chain_id = input(
                        '[EVM chain id (skip for 97 - Binance testnet)]:\n'
                    )
                    if not chain_id:
                        chain_id = '97'
                else:
                    proceed = input('Press any key to continue or type (exit) to end proccess\n')
            elif api_method == '4':
                nft_contract = input(
                    '[NFT Contract address (0x..)]:\n')
                nft_id = input('[NFT On-chain ID]:\n')
                nft_data = input('[Encrypted data]:\n')
                nft_to = input('[Owner address (0x..)]:\n')

                print('Minting NFT..')

                url = 'https://thentic.tech/api/nfts/mint'
                headers = {'Content-Type': 'application/json'}
                data = {
                    'key': api_key,
                    'chain_id': chain_id,
                    'contract': nft_contract,
                    'nft_id': nft_id,
                    'nft_data': nft_data,
                    'to': nft_to
                }

                r = requests.post(url, json=data, headers=headers)

                print(
                    '  status: pending\n  [request id: '
                    + json.loads(r.text)['request_id'] +
                    '\n  transaction url: ' +
                    json.loads(r.text)['transaction_url'])

                if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                    print(r.text)
                    api_key = input(
                        '[API key (skip for new key)]:\n'
                    )
                    if not api_key:
                        api_key = requests.get('https://thentic.tech/api/key').text
                        print('[Your API key: ' + api_key)
                elif r.text == 'Chain not found':
                    print(r.text)
                    chain_id = input(
                        '[EVM chain id (skip for 97 - Binance testnet)]:\n'
                    )
                    if not chain_id:
                        chain_id = '97'
                else:
                    proceed = input('Press any key to continue or type (exit) to end proccess\n')
            
            elif api_method == '5':
                nft_contract = input(
                    '[NFT Contract address (0x..):\n')
                nft_id = input('[NFT On-chain ID:\n')
                nft_from = input('[Transfer from address (0x..):\n')
                nft_to = input('[Transfer to address (0x..):\n')

                print('Transferring NFT..')

                url = 'https://thentic.tech/api/nfts/transfer'
                headers = {'Content-Type': 'application/json'}
                data = {
                    'key': api_key,
                    'chain_id': chain_id,
                    'contract': nft_contract,
                    'nft_id': nft_id,
                    'from': nft_from,
                    'to': nft_to
                }

                r = requests.post(url, json=data, headers=headers)

                print(
                    '  status: pending\n  [request id: '
                    + json.loads(r.text)['request_id'] +
                    '\n  transaction url: ' +
                    json.loads(r.text)['transaction_url'])
                if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                    print(r.text)
                    api_key = input(
                        '[API key (skip for new key)]:\n'
                    )
                    if not api_key:
                        api_key = requests.get('https://thentic.tech/api/key').text
                        print('[Your API key: ' + api_key)
                elif r.text == 'Chain not found':
                    print(r.text)
                    chain_id = input(
                        '[EVM chain id (skip for 97 - Binance testnet)]:\n'
                    )
                    if not chain_id:
                        chain_id = '97'
                else:
                    proceed = input('Press any key to continue or type (exit) to end proccess\n')

            elif api_method == '6':
                print('Getting invoices..')

                url = 'https://thentic.tech/api/invoices/all'
                headers = {'Content-Type': 'application/json'}
                data = {'key': api_key, 'chain_id': chain_id}

                r = requests.get(url, json=data, headers=headers)
                try:
                    if len(json.loads(r.text)['invoices']) == 0:
                        print('No invoices created yet')

                    for i in json.loads(r.text)['invoices']:
                        print( i['amount'] + ' ' + i['currency'] +
                            ':\n  status: ' + i['status'] +
                            '\n  [request id: ' + i['request_id'] +
                            '\n  transaction url: ' +
                            i['transaction_url'])

                except:
                    pass

                if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                    print(r.text)
                    api_key = input(
                        '[API key (skip for new key)]:\n'
                    )
                    if not api_key:
                        api_key = requests.get('https://thentic.tech/api/key').text
                        print('[Your API key: ' + api_key)
                elif r.text == 'Chain not found':
                    print(r.text)
                    chain_id = input(
                        '[EVM chain id (skip for 97 - Binance testnet)]:\n'
                    )
                    if not chain_id:
                        chain_id = '97'
                else:
                    proceed = input('Press any key to continue or type (exit) to end proccess\n')

            elif api_method == '7':
                invoice_amount = input('[Invoice Amount]:\n')
                invoice_to = input('[Receiver address (0x..)]:\n')

                print('Generating Invoice..')

                url = 'https://thentic.tech/api/invoices/new'
                headers = {'Content-Type': 'application/json'}
                data = {
                    'key': api_key,
                    'chain_id': chain_id,
                    'amount': invoice_amount,
                    'to': invoice_to
                }

                r = requests.post(url, json=data, headers=headers)

                print(
                    '  status: pending\n  [request id: '
                    + json.loads(r.text)['request_id'] +
                    '\n  transaction url: ' +
                    json.loads(r.text)['transaction_url'])
                if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                    print(r.text)
                    api_key = input(
                        '[API key (skip for new key)]:\n'
                    )
                    if not api_key:
                        api_key = requests.get('https://thentic.tech/api/key').text
                        print('[Your API key: ' + api_key)
                elif r.text == 'Chain not found':
                    print(r.text)
                    chain_id = input(
                        '[EVM chain id (skip for 97 - Binance testnet)]:\n'
                    )
                    if not chain_id:
                        chain_id = '97'
                else:
                    proceed = input('Press any key to continue or type (exit) to end proccess\n')

            elif api_method == '8':
                request_id = input('[Invoice Request ID:\n')

                print('Cancelling Invoice..')

                url = 'https://thentic.tech/api/invoices/cancel'
                headers = {'Content-Type': 'application/json'}
                data = {
                    'key': api_key,
                    'chain_id': chain_id,
                    'request_id': request_id
                }

                r = requests.delete(url, json=data, headers=headers)

                print(r.text)
                if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                    #print(r.text)
                    api_key = input(
                        '[API key (skip for new key)]:\n'
                    )
                    if not api_key:
                        api_key = requests.get('https://thentic.tech/api/key').text
                        print('[Your API key: ' + api_key)
                elif r.text == 'Chain not found':
                    print(r.text)
                    chain_id = input(
                        '[EVM chain id (skip for 97 - Binance testnet)]:\n'
                    )
                    if not chain_id:
                        chain_id = '97'
                else:
                    proceed = input('Press any key to continue or type (exit) to end proccess\n')
            elif api_method == '9':
                print('Getting wallets..')

                url = 'https://thentic.tech/api/wallets/all'
                headers = {'Content-Type': 'application/json'}
                data = {'key': api_key, 'chain_id': chain_id}

                r = requests.get(url, json=data, headers=headers)

                try:
                    if len(json.loads(r.text)['wallets']) == 0:
                        print('No wallets created yet')

                    for i in json.loads(r.text)['wallets']:
                        print('[' + i + '')
                except:
                    pass

                if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                    print(r.text)
                    api_key = input(
                        '[API key (skip for new key)]:\n'
                    )
                    if not api_key:
                        api_key = requests.get('https://thentic.tech/api/key').text
                        print('[Your API key: ' + api_key)
                elif r.text == 'Chain not found':
                    print(r.text)
                    chain_id = input(
                        '[EVM chain id (skip for 97 - Binance testnet)]:\n'
                    )
                    if not chain_id:
                        chain_id = '97'
                else:
                    proceed = input('Press any key to continue or type (exit) to end proccess\n')
            elif api_method == '10':
                print('Creating new wallet..')

                url = 'https://thentic.tech/api/wallets/new'
                headers = {'Content-Type': 'application/json'}
                data = {'key': api_key}

                r = requests.post(url, json=data, headers=headers)

                try:
                    print('[  wallet: ' +
                        json.loads(r.text)['wallet'] +
                        '\n  [private key: ' +
                        json.loads(r.text)['private_key'] +
                        '\n[91mDO NOT SHARE PRIVATE KEY WITH ANYONE')
                except:
                    pass

                if r.text == 'API key not authorized. Get key: https://thentic.tech/api/key':
                    print(r.text)
                    api_key = input(
                        '[API key (skip for new key)]:\n'
                    )
                    if not api_key:
                        api_key = requests.get('https://thentic.tech/api/key').text
                        print('[Your API key: ' + api_key)
                elif r.text == 'Chain not found':
                    print(r.text)
                    chain_id = input(
                        '[EVM chain id (skip for 97 - Binance testnet)]:\n'
                    )
                    if not chain_id:
                        chain_id = '97'
                else:
                    proceed = input('Press any key to continue or type (exit) to end proccess\n')
            
            else:
                print('' + 'Please try again' + '')
    except:
        # print('' + 'Please try again' + '')
        print('' + 'Please try again' + '')
# Installation

```
pip install git+https://github.com/asluchevskiy/slavik_crypto_api.git
```

# Usage

```python
from slavik_crypto_api import SlavikAPIClient

base_url = 'http://api_base_url/api/'
api_key = 'your_api_key'
password = 'your_api_password'

api = SlavikAPIClient(base_url=base_url, api_key=api_key, password=password)
user = api.get_userinfo()
action = api.create_action(soft='zksync', action='swap')

print(f'username: {user["user"]}, points: {user["points"]}')
print(action)
```

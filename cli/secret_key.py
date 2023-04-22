from django.core.management.utils import get_random_secret_key
import json
key = get_random_secret_key()
json.dump(obj=key,fp=open('data.json','w'))

'''
Created on Jan 1, 2014

@author: ylou
'''
import pickle
import json
import tempfile

var = ['hello', [1.0, 2], ['one', 'two'], 'world']

# Native serialization
with tempfile.NamedTemporaryFile() as temp:
    serialized_var = pickle.dumps(var)
    temp.write(serialized_var)

    # deserialize to produce original content
    temp.seek(0)
    deserialized_var = pickle.load(temp)

    print deserialized_var

# JSON based serialization
encoded_var = json.dumps(var)

decoded_var = json.loads(encoded_var)

print encoded_var
print decoded_var

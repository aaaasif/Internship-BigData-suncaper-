import ast #Q5 Custom Object Serialization:

# Serialize function
def serialize(obj):
    return f"Object({obj})"

# Deserialize function
def deserialize(s):
    return ast.literal_eval(s.replace("Object(", "").replace(")", ""))

# Test the functions
original_obj = 66
serialized_obj = serialize(original_obj)
print("Serialized:", serialized_obj)

deserialized_obj = deserialize(serialized_obj)
print("Deserialized:", deserialized_obj)

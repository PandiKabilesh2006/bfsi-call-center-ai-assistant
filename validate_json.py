import json

file_path="data/alpaca_dataset.json"

try:
    with open(file_path,"r",encoding="utf-8") as f:
        data=json.load(f)
    print("JSON is valid.")
    print(f"Total samples:{len(data)}")
except json.JSONDecodeError as e:
    print("JSON Error:")
    print(e)

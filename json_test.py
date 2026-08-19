import json


json_text = """
{
  "goal": "掌握 Tool Calling",
  "days": 3
}
"""

data = json.loads(json_text)

print(type(json_text))
print(type(data))

print(data["goal"])
print(data["days"])

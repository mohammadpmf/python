import requests
import json
from tkinter import messagebox
response = requests.get("https://one-api.ir/joke/?token=258252:647f0bae10f6c")
messagebox.showinfo("جک", f"{json.loads(response.content)['result']}")

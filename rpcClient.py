import xmlrpc.client

# Connect to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Call the remote method
response = proxy.say_hello("Davin")
print("Server responded:", response)

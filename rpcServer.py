from xmlrpc.server import SimpleXMLRPCServer

# Define the function to expose
def say_hello(name):
    return f"Hello, {name}!"

# Create server
server = SimpleXMLRPCServer(("localhost", 8000))
print("RPC Server is running on port 8000...")

# Register the function
server.register_function(say_hello, "say_hello")

# Run the server
server.serve_forever()

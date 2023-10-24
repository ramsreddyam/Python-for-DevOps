server_name = "my_server"
is_http_enabled = True
port = 80
max_connections = 1000


print(f"Server Name: {server_name}")
print(f"HTTP enabled: {is_http_enabled}")
print(f"port number: {port}")
print(f"Maximum Connections: {max_connections}")

# Updated configurations

port = 443
is_http_enabled = False

print(f"Updated Port: {port}")
print(f"HTTP status: {is_http_enabled}")


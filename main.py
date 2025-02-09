import device_manager
import net_wol
import status_light

# Connect to network
ip = net_wol.connect()

# Successfully connected to network
status_light.send_blinks(1)

# Open a socket on port 80 for http requests and establish wol socket
connection = net_wol.listen(ip)
wol_socket = net_wol.establish_wol_socket()

# Successfully opened the port
status_light.send_blinks(2)

# Accept client requests
net_wol.serve(connection, device_manager.get_target_ip(), wol_socket)
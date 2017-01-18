 #!/bin/bash 
python3.4 server.py -i 0.0.0.0 -p 5121 &
python3.4 client.py -i 0.0.0.0 -p 5121 

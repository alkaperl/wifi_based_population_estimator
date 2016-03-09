# wifi_based_population_estimator
This is a piece of glueware that sticks up different components from hardware detection to real-time web display.

USAGE:

echo "input" | python parser.py

or, better yet if airodump-ng available 

airodum-ng <necessary args> | python parser.py

This script will print out all parsed source and dest MAC address. I'm currently working to send those information to a mysql database and then display it in real time (via php or ios app).

Testing webpage: http://ec2-52-36-84-12.us-west-2.compute.amazonaws.com/~lyan/deviceCount.php

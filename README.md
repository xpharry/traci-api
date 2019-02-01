# sumo-motion-planning
SUMO is a high level simulator for the traffic and autonomous vehicles.

# Using TraCI with python (under ./traci-python)

After starting the sumo simulator, simply run the python script:

```
python runner.py
```

# Using TraCI/C++TraCIAPI (under ./sumo-1.1.0/src/traci_client)

Files ./sumo-1.1.0 except for "./sumo-1.1.0/src/traci_client" are copied from sumo source directory with version 1.1.0.

## Useage:

**Under ./sumo-1.1.0, compile:**
```
mkdir build
cmake ..
make -j 8
```

**Run exetables generated in ../bin**

Start sumo simulator in one terminal and parse the port number:

```
sumo-gui -c example.sumocfg --remote-port 1337
```

```
./example
```

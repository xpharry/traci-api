# traci-api
SUMO is a high level simulator for the traffic and autonomous vehicles. Traci API provides an interface to interact with the simulator.

# Using TraCI with python (under ./traci-python)

After starting the sumo simulator, simply run the python script:

```
python runner.py
```

# Using TraCI/C++TraCIAPI (under ./traci-cpp)

Under ./traci-cpp there is a concised Traci C++ API called "traci_api" for sumo, we put our developed commanding
programs in the ./tests folder.

## Useage:

**Under ./traci-cpp, compile:**

```bash
mkdir build
cmake ..
make -j 8
```

The executables will be generated in ./traci-cpp/bin.

**Run executables**

1. Start sumo simulator in one terminal with the port number.

In scenarios folder, pick a scenario and parse the port number (here we hard-coded it as 1337),

```bash
sumo-gui -c example.sumocfg --remote-port 1337
```

2. Open another terminal, and under ./traci-cpp/bin run.

```bash
./example
```

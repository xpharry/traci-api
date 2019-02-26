#include <iostream>
#include <traci_api/TraCIAPI.h>
    
class Client : public TraCIAPI {
public:
    Client() {};
    ~Client() {};
};

int main(int argc, char* argv[]) {
    Client client;
    client.connect("localhost", 1337);
    std::cout << "time in ms: " << client.simulation.getCurrentTime() << "\n";
    std::cout << "run 5 steps ...\n";
    client.simulationStep(5 * 100);
    std::cout << "time in ms: " << client.simulation.getCurrentTime() << "\n";
    client.close();
}   

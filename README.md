# The Biscuit Machine Simulator

The Biscuit Machine Simulator is a project that tries to simulate the communication 
 between the different components that may be part in a real world biscuit 
conveyor belt machine as well as to show how such components can be controlled 
to work as one following certain set of rules. 

The communication between the components showed in this project 
is definatelly not the most optimized solution but it purpose is to try and replicate the different
components (devices) as if they were attached to an Arduino board and had input and output pins
for receiving and sending data. The project uses Redis key-value store 
which simulates the different pins of our controller board and allows us 
to run our devices as separate processes.

## Installation and usage

The project runs in 3 docker containers:
* One simulating the machine components and their basic functionalities based on their input.
* One running Redis.
* One running our machine controller and API providing us with interface for controlling the machine with ON, OFF and PAUSE commands.  

The 3 containers are orchestrated by docker compose and are started with:

```bash
docker-compose up
```

The containers run on their own docker bridge network for isolation in the environment.

If code changes are made to the project we would need to rebuild the docker images with the following command:

```bash
docker-compose build --no-cache
```

## Future ideas for features and improvements

* `Improvement:` Unit tests needs to be written.
* `Improvement:` We can pass the project code inside the containers as volumes instead of making a COPY. This will lower the number of time we need to rebuild the project when we make changes.
* `Improvement:` Some classes can be made Singletons.
* `Improvement:` Instead of simulating the pins and communication with Redis key value store we can use the Pub/Sub feature for more dynamic messaging.
* `Future feature:` We can introduce /state endpoint to show current state of the machine and it's components.
* `Future feature:` Flask-SocketIO can be added to the project to enable more real time communication with our controller. Changes to our machine state can be emitted/broadcasted to all connected clients.
* `Future feature:` Single Page Application can be created. It will communicate with our controller and provide good user interface for controlling the biscuit machine.


## Contributors
 Nikolay Tsonev

## License
[MIT](https://opensource.org/licenses/MIT)
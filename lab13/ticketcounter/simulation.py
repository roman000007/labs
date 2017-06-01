# Implementation of the main simulation class.
from arrays import Array
from linkedqueue import LinkedQueue as Queue
from ticketcounter.simpeople import TicketAgent, Passenger
from random import random


class TicketCounterSimulation :
# Create a simulation object.
    def __init__( self, numAgents, numMinutes, betweenTime, serviceTime ):
    # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes

        # Simulation components.
        self._passengerQ = Queue()
        self._theAgents = Array( numAgents )
        for i in range( numAgents ) :
            self._theAgents[i] = TicketAgent(i+1)

        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

# Run the simulation using the parameters supplied earlier.
    def run( self ):
        for curTime in range(self._numMinutes + 1) :
            self._handleArrive( curTime )
            self._handleBeginService( curTime )
            self._handleEndService( curTime )
        self.printResults()

# Print the simulation results.
    def printResults( self ):
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float( self._totalWaitTime ) / numServed
        print( "" )
        print( "Number of passengers served = ", numServed )
        print( "Number of passengers remaining in line = %d" %
        len(self._passengerQ) )
        print( "The average wait time was %4.2f minutes." % avgWait )


# The remaining methods that have yet to be implemented.
    def _handleArrive(self, curTime ): # Handles simulation rule #1.
        if random() < self._arriveProb:
            self._numPassengers += 1
            passenger = Passenger(self._numPassengers, curTime)
            self._passengerQ.add(passenger)
            print("Time", str(curTime + 1) + ":", "Passenger", passenger.idNum(), "arrived")


    def _handleBeginService(self, curTime ): # Handles simulation rule #2.
        for agent in self._theAgents:
            if agent.isFree():
                if not self._passengerQ.isEmpty():
                    passenger = self._passengerQ.pop()
                    agent.startService(passenger, curTime + self._serviceTime)
                    print("Time", str(curTime + 1) + ": Agent", agent.idNum(), "started serving Passenger", passenger.idNum())

    def _handleEndService(self,  curTime ): # Handles simulation rule #3.
        for agent in self._theAgents:
            if agent.isFinished(curTime):
                passenger = agent.stopService()
                print("Time", str(curTime + 1) + ": Agent", agent.idNum(), "stoped serving Passenger", passenger.idNum())
        self._totalWaitTime += len(self._passengerQ)

p = TicketCounterSimulation(2, 25, 4, 6)
p.run()

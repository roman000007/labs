# Implementation of the main simulation class.
from arrays import Array
from linkedqueue import LinkedQueue as Queue
from ticketcounter.simpeople import TicketAgent, Passenger


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
            self._handleArrival( curTime )
            self._handleBeginService( curTime )
            self._handleEndService( curTime )

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

    def _handleBeginService(self, curTime ): # Handles simulation rule #2.

    def _handleEndService(self,  curTime ): # Handles simulation rule #3.


p = TicketCounterSimulation(3, 3, 5, 6)
p.run()

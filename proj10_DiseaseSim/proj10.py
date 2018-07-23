# proj10: Simulating the Spread of Disease and Virus Population Dynamics
# Name:
# Date:

# import numpy
# import pylab
import random


class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """


class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """

    def __init__(self, maxBirthProb, clearProb):

        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def doesClear(self):

        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.clearProb and otherwise returns
        False.
        """

        number = random.random()
        if number <= self.clearProb:
            return True
        else:
            return False

    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         

        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        self.popDensity = popDensity
        num = random.random()
        probability = self.maxBirthProb * (1 - popDensity)
        if num < probability:
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException


class SimplePatient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, maxPop):
        """

        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """

        # TODO
        self.viruses = viruses
        self.maxPop = maxPop

    def getTotalPop(self):
        """
        Gets the current total virus population. 
        returns: The total virus population (an integer)
        """

        # TODO
        return len(self.viruses)

    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus survives and updates the list
        of virus particles accordingly.   
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """

        # TODO
        for virus in self.viruses:
            if virus.doesClear():
                self.viruses.remove(virus)
            popDensity = float((int(self.getTotalPop()))/float(int(self.maxPop)))
            try:
                self.viruses.append(virus.reproduce(popDensity))
            except NoChildException:
                continue
        return len(self.viruses)


#
# PROBLEM 2
#
def simulationWithoutDrug():

    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """

    # TODO
    viruses = []
    viruses2 = []
    viruses3 = []
    for x in range(0, 100):
        viruses.append(SimpleVirus(0.1, 0.05))
    patient = SimplePatient(viruses, 1000)
    for y in range(0, 300):
        viruses2.append(len(patient.viruses))
        patient.update()
        viruses3.append(y)
    print viruses2
    print viruses3

simulationWithoutDrug()



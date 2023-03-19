from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
from typing import List
from enum import Enum
import numpy as np

@dataclass
class Context:
    num_immediate_agents: int # how close the nearby agents are
    position: np.ndarray # where the agent is
    positions: List[np.ndarray] # where the nearby agents are
    num_cycles: int # number of iterations psased

class StrategyType(Enum):
    POSITION = 0
    REPRODUCTION = 1
    OTHER = 2

class AgentStrategy(ABC):
    type = StrategyType.OTHER 

    @abstractmethod
    def evolve(self, context: Context):
        pass

    @abstractproperty
    def state(self):
        pass

class PositionNearby(AgentStrategy):
    type = StrategyType.POSITION
    
    def __init__(self, position:np.ndarray, lr=0.1):
        """A strategy to move towards/away from population centers, weighted by distance

        Arguments:
        position (np.ndarray): seed position
        lr (float): moving towards or away from population centers, value multiplied to agent direction 
        """
        assert len(position) == 3, "we are in 3 space!"

        self.__position = position
        self.__lr = lr

    @property
    def state(self):
        return self.__position

    def evolve(self, context):

        # calculate regional inluences of each
        for i in context.positions:
            # subtracting i means that it will be a vector
            # pointing TOWARDS i
            # now we divide by absolute value of i to ensure that
            # closer points are more valued
            self.__position += (self.__position - i)*(lr/(np.linalg.norm(i-self.__position)))

class Agent:

    def __init__(self, initial_position:np.ndarray,
                       initial_metadata=None):
        self.__position_strategy = None
        self.__reproduction_strategy = None
        self.__other_strategy = None

        self.position = initial_position
        self.other = initial_metadata

    def register(strategy:AgentStrategy, type:StrategyType):

        if type == StrategyType.POSITION:
            self.__position_strategy = strategy
        elif type == StrategyType.REPRODUCTION:
            self.__reproduction_strategy = strategy
        elif type == StrategyType.OTHER:
            self.__other_strategy = strategy

    # def __call__(self):
        



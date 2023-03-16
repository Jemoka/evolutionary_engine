from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
from typing import List
from enum import Enum

@dataclass
class Position:
    x: float
    y: float
    z: float

@dataclass
class Context:
    resources: float # float value for amount of resources available
    resource_desirability: float # num "not hungry" 0 ---> "hungry" 1
    num_immediate_agents: int # how close the nearby agents are
    position: Position # where the agent is
    immediate_position: List[Position] # where the nearby agents are
    num_cycles: int # number of 

class StrategyType(Enum):
    POSITION = 0
    CONSUMPTION = 1
    REPRODUCTION = 2
    COSMETIC = 3
    OTHER = 4

class AgentStrategy(ABC):
    type = StrategyType.OTHER 

    @abstractmethod
    def evolve(self, context: Context):
        pass

    @abstractproperty
    def state(self):
        pass

class PositionStrategy(AgentStrategy):
    type = StrategyType.POSITION
    
    def __init__(self, position:Position):
        self.__position = position

    @property
    def state(self):
        return self.__position

# class Agent:
#     """
#     An agent that moves in the environment
#     """

#     def __init__(self):


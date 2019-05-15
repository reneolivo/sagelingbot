#!/usr/bin/env python3

from ffai.web.api import *
import numpy as np
import time
import ffai.core.model as Model
import ffai.core.table as Table
from ffai.ai.registry import register_bot, make_bot
import ffai.core.game as game
from ffai.util.bothelper import ActionSequence
import ffai.util.bothelper as helper

class SagelingBot(ProcBot):

    mean_actions_available = []
    steps = []

    def __init__(self, name):
        super().__init__(name)
        self.my_team = None
        self.actions_available = []
        self.current_move = None

    def new_game(self, game, team):
        self.my_team = team
        self.actions_available = []
        self.actions_taken = 0

    def coin_toss_flip(self, game: game.Game) -> Model.Action:
        return Model.Action(Table.ActionType.HEADS)

    def coin_toss_kick_receive(self, game: game.Game) -> Model.Action:
        if (game.state.weather != Table.WeatherType.NICE):
            return Model.Action(Table.ActionType.KICK)
        else:
            return Model.Action(Table.ActionType.RECEIVE)

    def setup(self, game: game.Game) -> Model.Action:
        if (self.current_move and self.current_move.is_empty() == False):
            return self.current_move.popleft()
        else:
            formation = game.config.offensive_formations[0] \
              if game.state.receiving_this_drive == self.my_team else \
              game.config.defensive_formations[0]
            actions = formation.actions(game, self.my_team)
            actions.append(Model.Action(Table.ActionType.END_SETUP))
            self.current_move = ActionSequence(actions)

    def place_ball(self, game: game.Game):
        center_opposite = Model.Square(helper.reverse_x_for_left(game, self.my_team, 7), 8)
        return Model.Action(Table.ActionType.PLACE_BALL, pos=center_opposite)

    def high_kick(self, game):
        return Model.Action(Table.ActionType.END_TURN)

    def touchback(self, game):
        return Model.Action(Table.ActionType.END_TURN)

    def turn(self, game):
        return Model.Action(Table.ActionType.END_TURN)

    def quick_snap(self, game):
        return Model.Action(Table.ActionType.END_TURN)

    def blitz(self, game):
        return Model.Action(Table.ActionType.END_TURN)

    def player_action(self, game):
        return Model.Action(Table.ActionType.END_TURN)

    def block(self, game):
        return Model.Action(Table.ActionType.END_TURN)

    def push(self, game):
        return Model.Action(Table.ActionType.END_TURN)

    def follow_up(self, game):
        return Model.Action(Table.ActionType.END_TURN)

    def apothecary(self, game):
        return Model.Action(Table.ActionType.END_TURN)

    def pass_action(self, game):
        return Model.Action(Table.ActionType.END_TURN)

    def catch(self, game):
        return Model.Action(Table.ActionType.END_TURN)

    def interception(self, game):
        return Model.Action(Table.ActionType.END_TURN)

    def gfi(self, game):
        return Model.Action(Table.ActionType.END_TURN)

    def dodge(self, game):
        return Model.Action(Table.ActionType.END_TURN)

    def pickup(self, game):
        return Model.Action(Table.ActionType.END_TURN)

    def end_game(self, game):
        print("Num steps:", len(self.actions_available))
        print("Avg. branching factor:", np.mean(self.actions_available))
        winner = game.get_winner()
        print("Casualties: ", game.num_casualties())
        if winner is None:
            print("It's a draw")
        elif winner == self:
            print("I ({}) won".format(self.name))
        else:
            print("I ({}) lost".format(self.name))
        print("I took", self.actions_taken, "actions")

register_bot('SagelingBot', SagelingBot)

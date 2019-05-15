#!/usr/bin/env python3

import ffai.web.server as server
import ffai.web.api as api
from ffai.ai.registry import make_bot
from ffai.core.model import Agent

# Import this to register bots
import sagelingbot

api.new_game(home_team_id="orc-1",
             away_team_id="human-1",
             home_agent=make_bot("SagelingBot"),
             away_agent=make_bot("SagelingBot"))

# Run server
server.start_server(debug=True, use_reloader=False)

import sagelingbot as sagelingbot
import ffai.core.game as game
import ffai.core.load as load
import ffai.core.model as Model
import ffai.core.table as Table

from behave import given, when, then, step

def setupGameAndBots(context):
    myTeam = Model.Team('my_team', name='My Team', race='Humans', coach='AI Coach')
    theirTeam = Model.Team('their_team', name='Their Team', race='Humans', coach='AI Coach')
    config = load.get_config("ff-11.json")
    context.myBot = sagelingbot.SagelingBot('HomeAgentBot')
    theirBot = sagelingbot.SagelingBot('AwayAgentBot')
    context.game = game.Game('test_game', home_team=myTeam, away_team=theirTeam, home_agent=context.myBot, away_agent=theirBot, config=config)

@given('the coin toss phase')
def step_impl(context):
    setupGameAndBots(context)

@when('the coin is toss')
def step_impl(context):
    context.actionTaken = context.myBot.coin_toss_flip(context.game)

@when('the weather is "{weatherType}"')
def step_impl(context, weatherType):
    weatherTypes = {
        "Swealtering Heat": Table.WeatherType.SWELTERING_HEAT,
        "Very Sunny": Table.WeatherType.VERY_SUNNY,
        "Nice": Table.WeatherType.NICE,
        "Pouring Rain": Table.WeatherType.POURING_RAIN,
        "Blizzard": Table.WeatherType.BLIZZARD,
    }

    context.game.state.weather = weatherTypes[weatherType]

@when('the bot wins the coin toss')
def step_impl(context):
    context.actionTaken = context.myBot.coin_toss_kick_receive(context.game)

@then('the bot chooses "{coinFace}"')
def step_impl(context, coinFace):
    coinFaces = {
        "Heads": Table.ActionType.HEADS,
        "Tails": Table.ActionType.TAILS,
    }
    assert context.actionTaken.action_type == coinFaces[coinFace]

@then('the bot chooses to "{kickOrReceive}"')
def step_impl(context, kickOrReceive):
    kickOrReceiveActions = {
        "Kick": Table.ActionType.KICK,
        "Receive": Table.ActionType.RECEIVE,
    }

    assert context.actionTaken.action_type == kickOrReceiveActions[kickOrReceive]

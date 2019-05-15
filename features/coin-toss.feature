Feature: Coin Toss

  Scenario: Selecting the coin face before the toss
    Given the coin toss phase
    When the coin is toss
    Then the bot chooses "Heads"

  Scenario: Choosing to receive
    Given the coin toss phase
    When the weather is "Nice"
    And the bot wins the coin toss
    Then the bot chooses to "Receive"

  Scenario Outline: Choosing to kick
    Given the coin toss phase
    When the weather is "<Bad Weather>"
    And the bot wins the coin toss
    Then the bot chooses to "Kick"

    Examples:
      | Bad Weather      |
      | Swealtering Heat |
      | Very Sunny       |
      | Pouring Rain     |
      | Blizzard         |

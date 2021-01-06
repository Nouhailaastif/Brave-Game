from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'BRAVE'
    players_per_group = 3
    num_rounds = 1
    errors_EX2 = 0


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # First we start by defining the variables for our three players

    # For executant 1
    EX1_Answer_1_1 = models.StringField()
    EX1_Answer_1_2 = models.StringField()
    EX1_Answer_1_3 = models.StringField()
    EX1_Answer_1_4 = models.StringField()
    EX1_Answer_1_5 = models.StringField()

    EX1_Answer_2_1 = models.StringField()
    EX1_Answer_2_2 = models.StringField()
    EX1_Answer_2_3 = models.StringField()
    EX1_Answer_2_4 = models.StringField()
    EX1_Answer_2_5 = models.StringField()

    EX1_Answer_3_1 = models.StringField()
    EX1_Answer_3_2 = models.StringField()
    EX1_Answer_3_3 = models.StringField()
    EX1_Answer_3_4 = models.StringField()
    EX1_Answer_3_5 = models.StringField()

    EX1_Answer_4_1 = models.StringField()
    EX1_Answer_4_2 = models.StringField()
    EX1_Answer_4_3 = models.StringField()
    EX1_Answer_4_4 = models.StringField()
    EX1_Answer_4_5 = models.StringField()

    EX1_Answer_5_1 = models.StringField()
    EX1_Answer_5_2 = models.StringField()
    EX1_Answer_5_3 = models.StringField()
    EX1_Answer_5_4 = models.StringField()
    EX1_Answer_5_5 = models.StringField()

    # for executant 2

    EX2_Answer_1_1 = models.StringField()
    EX2_Answer_1_2 = models.StringField()
    EX2_Answer_1_3 = models.StringField()
    EX2_Answer_1_4 = models.StringField()
    EX2_Answer_1_5 = models.StringField()

    EX2_Answer_2_1 = models.StringField()
    EX2_Answer_2_2 = models.StringField()
    EX2_Answer_2_3 = models.StringField()
    EX2_Answer_2_4 = models.StringField()
    EX2_Answer_2_5 = models.StringField()

    EX2_Answer_3_1 = models.StringField()
    EX2_Answer_3_2 = models.StringField()
    EX2_Answer_3_3 = models.StringField()
    EX2_Answer_3_4 = models.StringField()
    EX2_Answer_3_5 = models.StringField()

    EX2_Answer_4_1 = models.StringField()
    EX2_Answer_4_2 = models.StringField()
    EX2_Answer_4_3 = models.StringField()
    EX2_Answer_4_4 = models.StringField()
    EX2_Answer_4_5 = models.StringField()

    EX2_Answer_5_1 = models.StringField()
    EX2_Answer_5_2 = models.StringField()
    EX2_Answer_5_3 = models.StringField()
    EX2_Answer_5_4 = models.StringField()
    EX2_Answer_5_5 = models.StringField()

    # FOR THE MANAGER

    Answer_1_1 = models.StringField()
    Answer_1_2 = models.StringField()
    Answer_1_3 = models.StringField()
    Answer_1_4 = models.StringField()
    Answer_1_5 = models.StringField()

    Answer_2_1 = models.StringField()
    Answer_2_2 = models.StringField()
    Answer_2_3 = models.StringField()
    Answer_2_4 = models.StringField()
    Answer_2_5 = models.StringField()

    Answer_3_1 = models.StringField()
    Answer_3_2 = models.StringField()
    Answer_3_3 = models.StringField()
    Answer_3_4 = models.StringField()
    Answer_3_5 = models.StringField()

    Answer_4_1 = models.StringField()
    Answer_4_2 = models.StringField()
    Answer_4_3 = models.StringField()
    Answer_4_4 = models.StringField()
    Answer_4_5 = models.StringField()

    Answer_5_1 = models.StringField()
    Answer_5_2 = models.StringField()
    Answer_5_3 = models.StringField()
    Answer_5_4 = models.StringField()
    Answer_5_5 = models.StringField()

# We are going to create a function that will attribute random numbers for our three players
    factor = random.randint(1, 3)

    def num_attribution(self):
        players = self.get_players()
        for p in players:
            return factor

# The players have to make a choice if they want to be responsible or not

    role_decision = models.BooleanField(label='As stated in the instructions, do prefer to take the control?',
                                        choices=[
                                            [1, 'Yes, I want to be the manager!'],
                                            [0, 'No, I\'m good.']
                                        ],
                                        widget=widgets.RadioSelect
                                        )

# This function will decide who will be the manager and who will be the executants depending  on their previous choices

    def role_attribution(self):
        if role_decision.count(1) == 1:
            if self.role_decision == 1:
                return 'manager'
            elif self.role_decision == 0:
                return 'executant1' or 'executant2'

        elif role_decision.count(1) == 2:
            if self.role_decidion == 1 and self.factor.max():
                return 'manager'
            elif self.role_decidion == 1 and self.factor.min():
                return 'manager'
            elif self.role_decision == 0:
                return 'executant1'
            else:
                return 'executant2'
        elif role_decision.count(1) == 3:
            if self.factor.max():
                return 'manager'
            elif self.factor.min():
                return 'executant1'
            else:
                return 'executant2'
        elif role_decision.count(1) == 0:
            if self.factor.max():
                return 'manager'
            elif self.factor.min():
                return 'executant1'
            else:
                return 'executant2'

# now we are going to try to

    EX1_Answers = ['EX1_Answer_1_1', 'EX1_Answer_1_2', 'EX1_Answer_1_3', 'EX1_Answer_1_4', 'EX1_Answer_1_5',
                   'EX1_Answer_2_1', 'EX1_Answer_2_2', 'EX1_Answer_2_3', 'EX1_Answer_2_4', 'EX1_Answer_2_5',
                   'EX1_Answer_3_1', 'EX1_Answer_3_2', 'EX1_Answer_3_3', 'EX1_Answer_3_4', 'EX1_Answer_3_5',
                   'EX1_Answer_4_1', 'EX1_Answer_4_2', 'EX1_Answer_4_3', 'EX1_Answer_4_4', 'EX1_Answer_4_5',
                   'EX1_Answer_5_1', 'EX1_Answer_5_2', 'EX1_Answer_5_3', 'EX1_Answer_5_4', 'EX1_Answer_55_5']
    EX2_Answers = ['EX2_Answer_1_1', 'EX2Answer_1_2', 'EX2_Answer_1_3', 'EX2_Answer_1_4', 'EX2_Answer_1_5',
                   'EX2_Answer_2_1', 'EX2_Answer_2_2', 'EX2_Answer_2_3', 'EX2_Answer_2_4', 'EX2_Answer_2_5',
                   'EX2_Answer_3_1', 'EX2_Answer_3_2', 'EX2_Answer_3_3', 'EX2_Answer_3_4', 'EX2_Answer_3_5',
                   'EX2_Answer_4_1', 'EX2_Answer_4_2', 'EX2_Answer_4_3', 'EX2_Answer_4_4', 'EX2_Answer_4_5',
                   'EX_Answer_5_1', 'EX2_Answer_5_2', 'EX2_Answer_5_3', 'EX2_Answer_5_4', 'EX2_Answer_55_5']
    MG_Answers = ['Answer_1_1', 'Answer_1_2', 'Answer_1_3', 'Answer_1_4', 'Answer_1_5',
                  'Answer_2_1', 'Answer_2_2', 'Answer_2_3', 'Answer_2_4', 'Answer_2_5',
                  'Answer_3_1', 'Answer_3_2', 'Answer_3_3', 'Answer_3_4', 'Answer_3_5',
                  'Answer_4_1', 'Answer_4_2', 'Answer_4_3', 'Answer_4_4', 'Answer_4_5',
                  'Answer_5_1', 'Answer_5_2', 'Answer_5_3', 'Answer_5_4', 'Answer_55_5']

# This functions will help us compare between the verifications the manager does
    # and the answers provided by the executants
    errors_EX1 = 0
    for g in EX1_Answers:
        for k in MG_Answers:
            if EX1_Answers[g] == MG_Answers[k]:
                errors_EX1 += 0
        else:
            errors_EX1 += 1

    errors_EX2 = 0
    for j in EX2_Answers:
        for i in MG_Answers:
            if EX2_Answers[j] == MG_Answers[i]:
                errors_EX2 += 0
        else:
            errors_EX2 += 1
# We're going to take the maximum number of errors made by the executants to have
    # it a the deducted amount of the payoffs as indicated in teh instructions

    errors = max(errors_EX2, errors_EX1)

    payment_MG = models.CurrencyFields(initial=20) + models.CurrencyField(errors)
    payment_EX1 = models.CurrencyFields(initial=20) - models.CurrencyField(errors_EX1)
    payment_EX2 = models.CurrencyFields(initial=20) - models.CurrencyField(errors_EX2)

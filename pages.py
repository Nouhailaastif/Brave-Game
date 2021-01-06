from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Instructions(Page):
    pass


class Responsible_or_not(Page):
    form_model = "player"
    form_fields = ['role_decision']


class Role_attribution(Page):
    pass


class Task1A(Page):
    form_model = 'group'
    form_fields = ['EX1_Answer_1_1', 'EX1_Answer_1_2', 'EX1_Answer_1_3', 'EX1_Answer_1_4', 'EX1_Answer_1_5']

    def is_displayed(self):
        return self.player.role_attribution() == 'executant1'


class Task1B(Page):
    form_model = 'group'
    form_fields = ['EX2_Answer_1_1', 'EX2_Answer_1_2', 'EX2_Answer_1_3', 'EX2_Answer_1_4', 'EX2_Answer_1_5']

    def is_displayed(self):
        return self.player.role_attribution() == 'executant2'


class Task2A(Page):
    form_model = 'group'
    form_fields = ['EX1_Answer_2_1', 'EX1_Answer_2_2', 'EX1_Answer_2_3', 'EX1_Answer_2_4', 'EX1_Answer_2_5']

    def is_displayed(self):
        return self.player.role_attribution() == 'executant1'


class Task2B(Page):
    form_model = 'group'
    form_fields = ['EX2_Answer_2_1', 'EX2_Answer_2_2', 'EX2_Answer_2_3', 'EX2_Answer_2_4', 'EX2_Answer_2_5']

    def is_displayed(self):
        return self.player.role_attribution() == 'executant2'


class Task3A(Page):
    form_model = 'player'
    form_fields = ['EX1_Answer_3_1', 'EX1_Answer_3_2', 'EX1_Answer_3_3', 'EX1_Answer_3_4', 'EX1_Answer_3_5']

    def is_displayed(self):
        return self.player.role_attribution() == 'executant1'

class Task3B(Page):
    form_model = 'player'
    form_fields = ['EX2_Answer_3_1', 'EX2_Answer_3_2', 'EX2_Answer_3_3', 'EX2_Answer_3_4', 'EX2_Answer_3_5']

    def is_displayed(self):
        return self.player.role_attribution() == 'executant2'


class Task4A(Page):
    form_model = 'player'
    form_fields = ['EX1_Answer_4_1', 'EX1_Answer_4_2', 'EX1_Answer_4_3', 'EX1_Answer_4_4', 'EX1_Answer_4_5']

    def is_displayed(self):
        return self.player.role_attribution() == 'executant1'


class Task4B(Page):
    form_model = 'player'
    form_fields = ['EX2_Answer_4_1', 'EX2_Answer_4_2', 'EX2_Answer_4_3', 'EX2_Answer_4_4', 'EX2_Answer_4_5']

    def is_displayed(self):
        return self.player.role_attribution() == 'executant2'


class Task5A(Page):
    form_model = 'player'
    form_fields = ['EX1_Answer_5_1', 'EX1_Answer_5_2', 'EX1_Answer_5_3', 'EX1_Answer_5_4', 'EX1_Answer_5_5']

    def is_displayed(self):
        return self.player.role_attribution() == 'executant1'


class Task5B(Page):
    form_model = 'player'
    form_fields = ['EX2_Answer_5_1', 'EX2_Answer_5_2', 'EX2_Answer_5_3', 'EX2_Answer_5_4', 'EX2_Answer_5_5']

    def is_displayed(self):
        return self.player.role_attribution() == 'executant2'


class WaitPage(WaitPage):
    pass


class Verification(Page):
    form_model = 'player'
    form_fields = ['Answer_1_1', 'Answer_1_2', 'Answer_1_3', 'Answer_1_4', 'Answer_1_5',
                   'Answer_2_1', 'Answer_2_2', 'Answer_2_3', 'Answer_2_4', 'Answer_2_5',
                   'Answer_3_1', 'Answer_3_2', 'Answer_3_3', 'Answer_3_4', 'Answer_3_5',
                   'Answer_4_1', 'Answer_4_2', 'Answer_4_3', 'Answer_4_4', 'Answer_4_5',
                   'Answer_5_1', 'Answer_5_2', 'Answer_5_3', 'Answer_5_4', 'Answer_5_5']

    def is_displayed(self):
        return self.player.role_attribution() == 'manager'


class Payment(Page):
    pass


page_sequence = [Introduction,
                 Instructions,
                 Responsible_or_not,
                 Role_attribution,
                 Task1A,
                 Task1B,
                 Task2A,
                 Task2B,
                 Task3A,
                 Task3B,
                 Task4A,
                 Task4B,
                 Task5A,
                 Task5B,
                 Verification,
                 Payment
                 ]

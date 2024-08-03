
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'cognitive_load_experiment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    recall_numbers1 = models.IntegerField(label='Recall Numbers')
    recall_numbers2 = models.IntegerField(label='Recall Numbers')
    recall_numbers3 = models.IntegerField(label='Recall Numbers')
    sequence1 = models.StringField()
    sequence2 = models.StringField()
    sequence3 = models.StringField()
    answer = models.StringField()
    text_answer1 = models.BooleanField(choices=[[True, 'True'], [False, 'False']], label=' ')
    text_answer2 = models.BooleanField(choices=[[True, 'True'], [False, 'False']], label=' ')
    text_answer3 = models.BooleanField(choices=[[True, 'True'], [False, 'False']], label=' ')
    math1 = models.IntegerField(label=' ')
    math2 = models.IntegerField(label=' ')
    math3 = models.IntegerField(label=' ')
    math4 = models.IntegerField(label=' ')
    math5 = models.IntegerField(label=' ')
    confidence_own = models.IntegerField(label='How confident were you in doing the tasks on your own?')
    confidence_ai = models.IntegerField(label='How confident were you in relying on the AI solutions?')
class IntroductionPage(Page):
    form_model = 'player'
class SequencePage1(Page):
    form_model = 'player'
    form_fields = ['sequence1']
class TaskTextAndAiUsePage11(Page):
    form_model = 'player'
class TaskTextAndAiUsePage111(Page):
    form_model = 'player'
    form_fields = ['text_answer1', 'text_answer2', 'text_answer3']
class SolutionTextTask(Page):
    form_model = 'player'
class RecallSequencePage1(Page):
    form_model = 'player'
    form_fields = ['recall_numbers1']
class ResultPage1(Page):
    form_model = 'player'
class NewRound(Page):
    form_model = 'player'
class SequencePage2(Page):
    form_model = 'player'
    form_fields = ['sequence2']
class TaskEcoAndAiUsePage(Page):
    form_model = 'player'
    form_fields = ['answer']
class SolutionEcoTask(Page):
    form_model = 'player'
class RecallSequencePage2(Page):
    form_model = 'player'
    form_fields = ['recall_numbers2']
class ResultPage2(Page):
    form_model = 'player'
class NewRoundA(Page):
    form_model = 'player'
class SequencePage3(Page):
    form_model = 'player'
    form_fields = ['sequence3']
class TaskMathAndAiUsePage(Page):
    form_model = 'player'
    form_fields = ['math1', 'math2', 'math3', 'math4', 'math5']
class SolutionMathTask(Page):
    form_model = 'player'
class RecallSequencePage3(Page):
    form_model = 'player'
    form_fields = ['recall_numbers3']
class ResultPage3(Page):
    form_model = 'player'
class OverallResults(Page):
    form_model = 'player'
class OutroPage(Page):
    form_model = 'player'
    form_fields = ['confidence_own', 'confidence_ai']
page_sequence = [IntroductionPage, SequencePage1, TaskTextAndAiUsePage11, TaskTextAndAiUsePage111, SolutionTextTask, RecallSequencePage1, ResultPage1, NewRound, SequencePage2, TaskEcoAndAiUsePage, SolutionEcoTask, RecallSequencePage2, ResultPage2, NewRoundA, SequencePage3, TaskMathAndAiUsePage, SolutionMathTask, RecallSequencePage3, ResultPage3, OverallResults, OutroPage]
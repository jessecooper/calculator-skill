from mycroft import MycroftSkill, intent_file_handler
from lingua_franca.parse import extract_numbers


class Calculator(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('calculator.intent')
    def handle_calculator(self, message):
        self.log.info("maessage: %s", message.data.get('utterance'))
        self.log.info("equation: %s", message.data.get('equation'))
        self.speak_dialog('not_implemented')

    @intent_file_handler('sum.intent')
    def handle_calculator(self, message):
        numbers = extract_numbers(message.data.get('numbers'))
        self.log.info("maessage: %s", numbers)
        answer = sum(numbers)
        self.speak_dialog('calculator', {'answer': answer})


def create_skill():
    return Calculator()


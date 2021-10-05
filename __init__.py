from mycroft import MycroftSkill, intent_file_handler
from lingua_franca.parse import extract_numbers


class Calculator(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('calculator.intent')
    def handle_calculator(self, message):
        self.log.info("maessage: %s", message.data.get('utterance'))
        self.log.info("number1: %s", message.data.get('number1'))
        self.log.info("number2: %s", message.data.get('number2'))
        self.speak_dialog('not_implemented')

    @intent_file_handler('sum.intent')
    def handle_sum(self, message):
        numbers = extract_numbers(message.data.get('numbers'))
        self.log.info("maessage: %s", numbers)
        answer = sum(numbers)
        self.speak_dialog('calculator', {'answer': answer})


def create_skill():
    return Calculator()


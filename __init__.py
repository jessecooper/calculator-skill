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
        # TODO issue with decimal points
        self.log.info("lang: %s", self.lang)
        self.log.info("raw numbers var: %s", message.data.get('numbers'))
        numbers = extract_numbers(message.data.get('numbers'))
        self.log.info("numbers: %s", numbers)
        answer = sum(numbers)
        # answer as an int if it is not a float
        self.speak_dialog('calculator', {'answer': int(answer) if answer.is_integer() else answer})

    @intent_file_handler('difference.intent')
    def handle_difference(self, message):
        self.log.info("raw numbers var: %s", message.data.get('numbers'))
        numbers = extract_numbers(message.data.get('numbers'))
        self.log.info("numbers: %s", numbers)
        if len(numbers) > 2:
            self.speak_dialog('not_implemented')
        else:
            if message.data.get('numbers').find('from') != -1:
                answer = numbers[1]-numbers[0]
            else:
                answer = numbers[0]-numbers[1]
            # answer as an int if it is not a float
            self.speak_dialog('calculator', {'answer': int(answer) if answer.is_integer() else answer})

    @intent_file_handler('percentage.intent')
    def handle_percentage(self, message):
        self.log.info("raw numbers var: %s", message.data.get('numbers'))
        numbers = extract_numbers(message.data.get('numbers'))
        self.log.info("numbers: %s", numbers)
        if len(numbers) > 2:
            self.speak_dialog('not_implemented')
        else:
            if numbers[0] != 0:
                answer = (numbers[1]-numbers[0])/numbers[0]*100
            else:
                self.speak_dialog('divide_by_zero')
            self.speak_dialog('calculator', {'answer': f"{int(answer) if answer.is_integer() else answer} percent"})


def create_skill():
    return Calculator()


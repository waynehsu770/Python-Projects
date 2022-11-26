

from abc import ABC, abstractmethod

class SignupForm(ABC):
    def question(self, answer):
        print("Do you wish to signup? Please answer 'yes' or 'no': ",answer)

    @abstractmethod
    def response(self, answer):
        pass

class SubmitForm(SignupForm):
    def response(self, answer):
        print("You've answered {}! Thank you for signing up!".format(answer))

obj = SubmitForm()
obj.question("yes")
obj.response("yes")

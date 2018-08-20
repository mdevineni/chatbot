from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

import warnings
import ruamel
warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/assignment_rest_nlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-414578144033-415276250005-415001861763-514929468c15cf69f1e48b089a0b9abf', #app verification token
							'xoxb-414578144033-415001862019-e1MOyUxnKiOjMj40au9PS7EN', # bot verification token
							'OhEdoAfEv8yWW5qa5YR3DcOB', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
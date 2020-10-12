from mycroft import MycroftSkill, intent_file_handler


class DroneSim(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sim.drone.intent')
    def handle_sim_drone(self, message):
        self.speak_dialog('sim.drone')


def create_skill():
    return DroneSim()


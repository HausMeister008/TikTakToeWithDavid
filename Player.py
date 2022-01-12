from math import sqrt, floor
class Player():
    def __init__(self, p_name:str, chosen_icons:list=[]):
        self.name = self.get_input('Wie heißt du?\n>')
        self.bet_value = 0
        self.budget = 0
        self.icon = self.choose_icon(chosen_icons)
    
    def talkToMe(self, output):
        print(output)
    
    def get_input(self, prompt="> "):
        return input(prompt)
    
    def choose_icon(self,chosen_icons:list=[]):
        icon_pref = self.get_input('Choose your icon and you shall stick with it for ever: ') 
        return icon_pref if icon_pref not in chosen_icons else self.choose_icon(chosen_icons)
        
    
    def set_budget(self):
        self.budget = self.get_input('Choose your budget and you shall stick with it for ever: ')
        try:
           self.budget = int(self.budget)
        except ValueError:
            self.budget = self.set_budget()
        return self.budget

    def bet(self):
        self.bet_value = self.get_input('place bet: ')
        try:
           self. bet_value = int(self.bet_value)
        except ValueError:
            self.bet_value = self.bet()
        if(self.bet_value > self.budget):
            self.talkToMe('you cannot set a bet higher than your budget')
            self.bet_value = self.bet()
        
        self.budget -= self.bet_value
        return self.bet_value

    def won(self)->int:
        self.budget += self.bet_value * 2 
        return self.budget

    def draw(self, message:str='', positions:dict={}):
        pos = input(f'{message+": " if message else ""}{self.name}, in which spaces to you want to write your {self.icon}?\n> ')
        f_size = floor(sqrt(len(positions)))
        self.talkToMe(f_size)
        try:
            pos = tuple([int(s.strip()) for s in pos.split(',')])
            
            if not (0<pos[0]<=f_size and 0<pos[1]<=f_size):
                pos = self.draw(message='Outside the field: ', positions=positions)
                
            elif(positions[pos[0] + (pos[1]-1)*f_size].strip()):
                pos = self.draw(message='Position already taken: ', positions=positions)
            
        except ValueError:
            pos = self.draw(message='invalid input (should look like: "x,y"): ', positions=positions)
        return pos


class TTSSTTPlayer(Player):
    def __init__(self, p_name:str, chosen_icons:list=[]):
        super().__init__(p_name, chosen_icons)

    def talkToMe(self, output):
            # engine = p.init("sapi5")  # engine wird eine Instanz von pyttsx3
            # voices = engine.getProperty("voices")  # Systemstimmen werden geholt
            # self.language = 'de'
            # v = 2
            # engine.setProperty(
            #     "voice", 'Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_deDE_StefanM'
            # )  # Stimme wird ausgewählt (0->deutsche frau, 1->englische Frau)
            # engine.setProperty("rate", 175)  # Sprechgeschwindigkeit
            # engine.say(str(output))  # Was gesagt werden soll
            # engine.runAndWait()  # tatsächliches Sprechen des Audios
            tts = gTTS(output, lang="de", )
            tts.save('./output.mp3')
            playsound.playsound('./output.mp3')

    def get_input(self, prompt):
        r = sr.Recognizer()
        with sr.Microphone() as source:                                                                 
            self.talkToMe(prompt)
            r.pause_threshold = 2
            r.adjust_for_ambient_noise(
                source, duration=0.5
            )
            audio = r.listen(source)
        try: 
            transcript = r.recognize_google(audio, language="de-DE")
            print(f"You said: {transcript}")
        except sr.UnknownValueError:
            print("Could not understand audio")
            self.get_input(prompt)
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            self.get_input(prompt)
# board = [[' |', ' |', ' '], [' |', ' |', ' '], [' |', ' |', ' ']]
# positions = {1:' ', 2:'X', 3:' '}
if __name__ == '__main__':
    s1 = Player('Alice')
    print(s1.set_budget())
    print(s1.bet())
    print(s1.draw())
    print(s1.won())
    
#  1 2 3
# 1[][][]
# 2[][][]
# 3[][][]

# [] [x] []
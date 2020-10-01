from kivy.app import App
import speech_recognition as sr

GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
     # YOUR CREDENTIALS HERE
   }"""

class DailyDaddyApp(App):
    # An app to listen for microphone input and check for a given word or phrase
    
    # holds occurrences of target phrase to display
    daddy_count = 0
    
    # microphone control 
    currently_listening = False
    initial_state = True
    stop_listening = None
    
    def start_listening(self):
        # Starts to stops listening when button is pressed 
        
        # change on to off, off to on
        self.currently_listening = not self.currently_listening
        
        # microphone is on
        if self.currently_listening:
    
            print("I'm listening!")
            self.root.ids.start_stop.text = ("Stop Listening")
            
            # have pressed the button at least once
            # and can call to stop_listening()
            self.inital_state = False
            
            r = sr.Recognizer()
            m = sr.Microphone()
            
            with m as source: 
                
                # calibrate mic
                r.adjust_for_ambient_noise(source)  
            
                
            self.stop_listening = r.listen_in_background(m, self.callback)
        
        # microphone is off
        else:
    
            print("not currently listening")
            self.root.ids.start_stop.text = ("Start Listening")
            
            # avoid calling stop_listening before it has
            # been created/initalized due to a button press
            if self.stop_listening == None:
            
                print('hmm')
            
            self.stop_listening()      
            
    def daddy_counter(self, text):
        # check microphone input for target text
        # update and returns integer equal to total number of occurrences 
        
        list_text = text.split(' ')
        
        for each in list_text:
        
            # target word phrase is recognized 
            # set target word/phrase (phrase requires additional preparation)
            if each.lower() == 'daddy':
            
                self.daddy_count += 1
        
        print(self.daddy_count, end = " ")
        print("Daddies found.")
                
        return(self.daddy_count)
        
    def on_stop(self):
        
        if self.currently_listening:
        
            self.stop_listening()
       
        print("goodbye")
        
    def callback(self, recognizer, audio): 
        # check microphone input and display transcription 
        
        try:
            
            text = recognizer.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
            print("You said " + text)  # received audio data, now need to recognize it
            
            # holds current occurrences of target 
            dc = self.daddy_counter(text)
            
            # displays current occurrences if more than none
            if  dc > 0:
            
                self.root.ids.count.text = "Daddy Count: " + str(dc)
        
        except sr.UnknownValueError:
        
            pass
        
        except sr.RequestError as e:
       
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            
if __name__ == "__main__":
    
    DailyDaddyApp().run()

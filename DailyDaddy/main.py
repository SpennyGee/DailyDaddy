from kivy.app import App
import speech_recognition as sr

GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
     "type": "service_account",
     "project_id": "triple-shadow-276319",
     "private_key_id": "1bfc89372e1fad527290eb947439cb35d468f261",
     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDh8qve2I4Yxp2m\n8+1UOsbcIUczoix0GWm9ewM1VYKSPvSYGVhb55CNpHduPpdqUbGzZEaDEX2BxiIb\nxbhF8YzVdGr4ac471KIXDQD15N5F7Cy9YC1fR7oosvDLgW7OUiNQRgrLL3xD90K3\nPwBJwKI4/ZsPHwTcrUWktC8wHAMlvvOI+u/84YZZUkuVU1AvCuuo5VeoA6x6BDFX\nWPzapHwMIEtpATMlt/7l1kuiX2yFH1rHjfXpqh/igGBBR12gncF9Yv3UsvGFQcan\nKlLQ9jkQ4QDh39+Zdk/EHd7FfRBjSwBEX2+ra+ti/eipobwKnGJuBEeK8o/dgbZV\nv8teeY5TAgMBAAECggEAEJjnW1WUACm2BfM86tpTpj+2WVdSpaECQ/FuN5o7uHg+\nz/dr2eBr0J1h5B7D6s+42nRSVUMEWAz3KQwZyhJN/2LV9fNFVRH8nO3b6E2/roPR\nRR30Z0XZD/x8NK67nK53uptSiqdgnPHj6QFyb3h8Uh+XwGe0Am1vkR0Ad5IiZw2S\n9UrLvdYwwDZizaGdJfvAsN9zXtB53TWG1c62uvijziSJTnASetLFJUlcBZAKZivG\nlz1BH1q1ol1BicuxhaKDjrux0wny5LVwH0fz7ArKE6uppFwrb42qTt16HlHsY0Iz\nVaCMaM6WeaWglf7MYUNhz7hAl9RVp+qSd40layjQAQKBgQD2G2/FB/R0sHqdR9Wi\npbY2aIHRuNDP3GvSSY8S37cgFy6Yi/EYOv5eGCsJLLqJgvYJHB/wuRLCDiulknRf\n0szJ8TOn5qWv9HLZf9ffiSqetpd9UBgvLGjDA1ygR/ou+5Qerjq/t7OYLgKvo9/t\nwVQUs1HK7/yJa753XZEkeTDQAQKBgQDrB8lMVDe/DHkkSS7DnERnv/QCKc7bp2Vv\nlxLRXCcKq9LIwgdfXeIB1ocsVNSayFv00PcQqN70RNadPcXzkjldXmAXOL2QK0Uu\nFlE+NxuUkFbwxHkhfW5yJvI14Y0YbFNRaqEerggTYcW1d2W8erJXFUKBc2KZAitC\n5eN7e0YeUwKBgQDbOx2Zmrh8qijPqon4VT23wejC9autPmEd9kDpQzhR8dSkNyUR\nvJuTHlxX0+xnSq3494DMY1D+ZLkkyQ25voKG8cJeMuwtjcgxT9zxV7MLpwPTsWGZ\nxCmeboQ4k2WeLKWJnxLebboiOfpSk9yKYsmPlx2pdZa0o7ILiuIcZ4jAAQKBgQDf\n9MZzLlkEeq1Az195VAG23ylzmkUb95Hn2Iw85VPqjjpHxOPjkwFWgQbDTn5ck4lU\nan7S6CezmZjrsr5az75L4y8rUY0IwMKmHOwDnd1xHm1J9d369Jv2uHfasfeSCz8F\neNbY9jqJxYPw3DocdMpVwtNhqQKODIwOriKrOpdhMwKBgQCwf8yWVdrS3DfngZIU\nTY+ABdwHeyOghzTCS83bcmvFOjHhsq+mUASeefjIaj9qXQo5MXTyzrY/dFMFZKuV\n76ojCdl4lGJGepU4khhhuW7V1Mt0UvDi4q+gRMXGgWvy/UGuevYj84bYU939ig7A\nTGFpAzMj1z93Vzkfb/7poorrYw==\n-----END PRIVATE KEY-----\n",
     "client_email": "starting-account-qspw946dixx1@triple-shadow-276319.iam.gserviceaccount.com",
     "client_id": "100175108747364243003",
     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
     "token_uri": "https://oauth2.googleapis.com/token",
     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/starting-account-qspw946dixx1%40triple-shadow-276319.iam.gserviceaccount.com"
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
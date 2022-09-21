def open_google_and_search(text):
    search_for = text.split("kiếm", 1)[1]
    speak('Okay!')
    driver = webdriver.Chrome(path)
    driver.get("http://www.google.com")
    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)
def shutdown():  
    h = int(speak("Nhập giờ: "))
    m = int(speak("Nhập phút: "))
    s = int(speak("Nhập giây: "))
    while True:
        t = speak("Mời bạn chọn chế độ (ShutDown = s, Restart = r ): ")
        if t == "s" or t == "r":
            break  
        
    h = h*60*60
    m = m*60 
    s = s+m+h  
    print("Bắt đầu hẹn giờ")
    os.system(f"ShutDown -{t} -t {s}") # Lệnh thực hiện dòng lệnh
    print("Gõ lệnh ShutDown -a để hủy hẹn giờ")
    speak("Nhớ tắt hết ứng dụng trước khi tắt máy nhoa, ihihi ^^")
    time.sleep(2)

def Q_and_A():
    while True:
        with speech_recognition.Microphone() as mic:
            audio = robot_ear.listen(mic)
            speak("Mời bạn hỏi: ")
        try: 
            you = robot_ear.recognize_google(audio)
        except:
            you = ""
        print("You: " + you)
        
        if you == "":
            robot_brain = "Bot không nghe rõ. Bạn nói lại được không ?"
        elif "hello" in you:
            robot_brain = "hello Teddy"
        elif "today" in you:
            today = date.today()
            robot_brain = today.strftime("%B %d, %Y")
        elif "time" in you:
            now = datetime.now()
            robot_brain = now.strftime("%H hours %M minutes %S seconds")
        elif "oK. thanks" in you:
            robot_brain = "Không có gì đâu"
        elif "president" in you:
            robot_brain = "Donald Trump"
        elif "bye" in you:
            robot_brain = "Bye.Hẹn gặp lại bạn sau"
            speak("Bot: " + robot_brain) 
        else: 
            robot_brain = "Tôi vẫn khỏe, còn bạn ?"
            time.sleep(4)
            

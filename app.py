import tkinter as tk 
from tkinter import messagebox
import joblib
from nltk.tokenize import TweetTokenizer


#load the pretrained image 
model=joblib.load('Bangla_sentiment_Analysis_model.pkl')

#Function to analyze Sentiment 
def analyze_sentiment():
    #Get input text from the user 
    text=entry.get()
    
    #perfome sentimnet analysis using the model 
    sentiment=model.predict([text])[0]
    
    #Display the result
    if sentiment==1:
        result_label.config(text="Positive Sentiment")
    else:
        result_label.config(text="Negative Sentiment")
        
        
#create the main application windows
root=tk.Tk()
root.title("Bangla Sentiment Analysis") 


#Create GUI components 
label=tk.Label(root, text="Enter your Bangla Sentence:")
label.pack()

entry=tk.Entry(root,width=50)
entry.pack()

analyze_button=tk.Button(root,text='Analyze',command=analyze_sentiment)
analyze_button.pack()

result_label=tk.Label(root,text="")
result_label.pack()


#Run the Application

root.mainloop()
        
        
            
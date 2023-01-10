#Importing important packages
import spacy
import nltk
from nltk import tokenize

stories = pd.read_csv('Books _DataSheet - Sheet1.csv',sep=',',error_bad_lines=False)
stories.head()

nltk.download('punkt')
import requests
import re
from bs4 import BeautifulSoup
sentences=[]
author_gender=[]
genre=[]

for index,story in stories.iterrows():
  page = requests.get(story['HTML Link to the book'])
  soup = BeautifulSoup(page.content, 'html.parser')
  trial = soup.find_all('p')
  paragraphs=[]
  for p in trial:
    paragraphs.append(str(p))
  paragraphs_clean=[]

  for p in paragraphs:
    removed_htmltag_sent = BeautifulSoup(p, "html.parser").getText()
    paragraphs_clean.append(re.sub('[^a-zA-Z. ]','', str(removed_htmltag_sent)))
  for p in paragraphs_clean:
    temp = nltk.tokenize.sent_tokenize(p)
    for s in temp:
      sentences.append(s)
      author_gender.append(story['Author Gender'])
      genre.append(story['Genre'])

print(len(sentences))

data = pd.DataFrame({'Sentences':sentences,'Author':author_gender,'Genre':genre})
# display(data)

sentences[:10]

nlp = spacy.load("en_core_web_sm")

def find_event_with_gender_pronoun1(doc):
    sentence_events = []
    for token in doc:
        if token.pos_ == "VERB":     
          v1 = [str(child).lower() for child in token.children if str(child.pos_) == "PROPN" or str(child.pos_) == "PRON"]
          for v in v1:
            sentence_events.append([token.lemma_, v,])
    return sentence_events
events = []
for i in range(len(sentences)):
    doc = nlp(sentences[i])
    sentence_events = find_event_with_gender_pronoun1(doc)
    if len(sentence_events):
      sentence_events = list(map(lambda x: x + [author_gender[i], genre[i]], sentence_events))
      events += sentence_events

# for element in events:
#   for e in element:
  #   file1.write(str(e) + " ")
  # file1.write("\n")

print(events[:50])

female_list=['lady','female','girl','wife','Señora','gal','sister','sheila','broad','maiden','damsel','gentlewoman','daughter', 'hers', 'grandma', 'grandmother', 'aunt', 'sis', 'niece', 'mother', 'she', 'her', 'granny', 'granddaughter', 'girlfriend', 'woman', 'mom','miss','mrs.','ms']
male_list=['man','gentleman','boy','youth','guy','fellow','gent','bloke','chap','hombre','dude', 'godfather', 'grandson', 'stepbrother', 'sir', 'he', 'uncle', 'male', 'soninlaw', 'boyfriend', 'brother', 'grandpa', 'him', 'nephew', 'son', 'papa', 'exboyfriend', 'granddad', 'husband', 'stepson', 'dad', 'fatherinlaw', 'daddy', 'stepdad', 'father', 'grandfather', 'bro', 'his','Mr.']

events = []
for e in events:
  e = re.sub('[^a-zA-Z._]','', str(e))
  events.append(e.split('_'))
print(events[:10])
import pandas as pd
verb=[]
subject=[]
gender=[]
author_gender = []
story_genre = []
for x in events:
  if str(x[1]) in female_list:
    verb.append(x[0])
    subject.append(x[1])
    gender.append('F')
    author_gender.append(x[2])
    story_genre.append(x[3])
  if str(x[1]) in male_list:
    verb.append(x[0])
    subject.append(x[1])
    gender.append('M')
    author_gender.append(x[2])
    story_genre.append(x[3])
df = pd.DataFrame({'Event':verb,'Subject':subject,'Gender':gender, 'Author Gender':author_gender,'Story Genre':story_genre})
print(df.head(20))

df1= df.loc[df['Event'] == 'fight']
print(len(df1))
df2 = df1.loc[df1['Gender'] == 'F']
print(len(df2))


df.to_csv('events_with_details.csv', index=False)


import pandas as pd

class MedicalKnowledgeBase:
    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)
        self.df['question'] = self.df['question'].str.lower()

    def search(self, user_query):
        query = user_query.lower()
        for idx, row in self.df.iterrows():
            if query in row['question']:
                return row['answer']
        return "I'm not sure about that. Please consult a medical professional."

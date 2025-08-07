from app.nlp_pipeline import NLPPipeline
from app.med_knowledge_base import MedicalKnowledgeBase

class ChatBot:
    def __init__(self, faq_path):
        self.knowledge_base = MedicalKnowledgeBase(faq_path)
        self.pipeline = NLPPipeline()

    def get_response(self, user_input):
        input_keywords = self.pipeline.preprocess(user_input)

        best_match = None
        best_score = 0

        # Check each question in the knowledge base
        for question in self.knowledge_base.df['question']:
            question_keywords = self.pipeline.preprocess(question)
            score = len(set(input_keywords) & set(question_keywords))

            if score > best_score:
                best_score = score
                best_match = question

        if best_match:
            return self.knowledge_base.df.loc[
                self.knowledge_base.df['question'] == best_match, 'answer'
            ].values[0]
        else:
            return "I'm not sure about that. Please consult a medical professional."

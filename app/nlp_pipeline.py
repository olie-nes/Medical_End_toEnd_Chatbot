import re

class NLPPipeline:
    def __init__(self):
        self.stop_words = {
            'what', 'is', 'am', 'are', 'the', 'of', 'a', 'an', 'to', 'in',
            'why', 'do', 'you', 'i', 'this', 'that', 'how', 'have', 'having'
        }

    def preprocess(self, text):
        text = text.lower()
        # Tokenize using regex: split by non-alphanumeric
        tokens = re.findall(r'\b\w+\b', text)
        keywords = [word for word in tokens if word not in self.stop_words]
        return keywords


# Test it
if __name__ == "__main__":
    pipeline = NLPPipeline()
    query = input("Enter medical query: ")
    print("Extracted keywords:", pipeline.preprocess(query))

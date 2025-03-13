import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .knowledgeBase import conversations

class ChatbotTFIDF:
    def __init__(self):
        self.conversations = conversations
        self.vectorizer = TfidfVectorizer()
        self.vectorizer.fit(self.conversations.keys())

    def respond(self, question):
        question_vec = self.vectorizer.transform([question])
        responses_vec = self.vectorizer.transform(self.conversations.keys())
        similarities = cosine_similarity(question_vec, responses_vec)
        best_response = list(self.conversations.values())[similarities.argmax()]
        return best_response

    def start_chat(self, duration_min=20):
        print("Chatbot Consejero de Estudios activado. Puedes preguntarme sobre técnicas de estudio, organización y más.")
        start_time = time.time()
        time_limit = start_time + (duration_min * 60)  

        while time.time() < time_limit:
            user_input = input("\nTú: ")
            if user_input.lower() in ["salir", "adiós", "terminar"]:
                print("Bot: ¡Hasta luego! Espero haberte ayudado.")
                break
            response = self.respond(user_input)
            print(f"Bot: {response}")

        print("\n Tiempo de conversación terminado. ¡Éxito en tus estudios! ")

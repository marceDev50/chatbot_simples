import tkinter as tk
from tkinter import scrolledtext
import random

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "oi": ["Olá!", "Oi! Como vai?", "Oi!"],
            "tudo bem?": ["Estou bem, obrigado! E você?", "Tudo ótimo!", "Estou bem, e você?"],
            "qual o seu nome?": ["Eu sou um chatbot!", "Pode me chamar de Chatbot.", "Sou um chatbot, prazer!"],
            "o que você faz?": ["Eu converso com você!", "Estou aqui para bater um papo.", "Eu sou programado para conversar com você!"],
            "adeus": ["Até mais!", "Tchau!", "Foi bom conversar com você!"]
        }
        self.default_responses = [
            "Interessante! Conte-me mais.",
            "Humm, não sei muito sobre isso.",
            "Desculpe, não entendi. Pode repetir?",
            "Fale mais sobre isso."
        ]
        
    def get_response(self, user_input):
        user_input = user_input.lower()
        if user_input in self.responses:
            return random.choice(self.responses[user_input])
        else:
            return random.choice(self.default_responses)

def send_message():
    user_message = user_input.get()
    if user_message.strip() != "":
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "Você: " + user_message + "\n")
        user_input.delete(0, tk.END)
        
        if user_message.lower() == "adeus":
            chat_window.insert(tk.END, "Chatbot: Até mais!\n")
            chat_window.config(state=tk.DISABLED)
            return
        
        response = chatbot.get_response(user_message)
        chat_window.insert(tk.END, "Chatbot: " + response + "\n")
        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)

# Criação da janela principal
root = tk.Tk()
root.title("Chatbot Simples")

# Criação do widget de texto para exibir a conversa
chat_window = scrolledtext.ScrolledText(root, state=tk.DISABLED, width=50, height=20, wrap=tk.WORD)
chat_window.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
chat_window.config(state=tk.NORMAL)
chat_window.insert(tk.END, "Chatbot: Olá! Como posso ajudar você hoje? (Digite 'adeus' para encerrar a conversa)\n")
chat_window.config(state=tk.DISABLED)

# Criação da entrada de texto para o usuário digitar suas mensagens
user_input = tk.Entry(root, width=40)
user_input.grid(row=1, column=0, padx=10, pady=10)

# Criação do botão de enviar
send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Instância do chatbot
chatbot = SimpleChatbot()

# Inicialização da janela principal
root.mainloop()
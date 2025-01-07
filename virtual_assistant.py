from gtts import gTTS
import os
import tempfile
from datetime import datetime
import playsound
import pyjokes
import wikipedia
import webbrowser
import winshell
from pygame import mixer
import warnings
import time
import speech_recognition as sr

# Suppress Wikipedia parser warnings
warnings.filterwarnings("ignore", category=UserWarning)

class VirtualAssistant:
    def __init__(self, use_voice_input=False):
        self.music_dir = os.path.join(os.path.expanduser("~"), "Music")
        self.user_name = None
        self.temp_dir = tempfile.gettempdir()
        self.use_voice_input = use_voice_input
        if use_voice_input:
            self.recognizer = sr.Recognizer()

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.1)

    def print_separator(self):
        """Print a visual separator"""
        print("\n" + "="*50)

    def listen(self):
        """Capture audio from microphone and convert to text"""
        with sr.Microphone() as source:
            print("\nOuvindo...")
            self.recognizer.pause_threshold = 1
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            try:
                audio = self.recognizer.listen(source, timeout=5)
                text = self.recognizer.recognize_google(audio, language='pt-BR')
                print(f"Você disse: {text}")
                return text.lower()
            except sr.WaitTimeoutError:
                print("Nenhum áudio detectado")
                return ""
            except sr.UnknownValueError:
                print("Não entendi o que você disse")
                return ""
            except sr.RequestError:
                print("Erro ao acessar o serviço de reconhecimento de voz")
                return ""

    def get_audio(self):
        """Get input from user (voice or text)"""
        self.print_separator()
        if self.use_voice_input:
            return self.listen()
        else:
            print("\nDigite seu comando (ou 'sair' para encerrar):")
            text = input("> ").lower()
            print(f"Você digitou: {text}")
            return text

    def speak(self, text, also_print=True):
        """Display text and speak it"""
        if also_print:
            print(f"\nAssistente: {text}")
        # Text to speech
        tts = gTTS(text=text, lang='pt-BR')
        temp_file = os.path.join(self.temp_dir, 'voice.mp3')
        try:
            tts.save(temp_file)
            playsound.playsound(temp_file)
        except Exception as e:
            print(f"Erro ao reproduzir áudio: {str(e)}")
        finally:
            try:
                os.remove(temp_file)
            except:
                pass

    def play_music(self, song):
        """Play a music file"""
        try:
            mixer.init()
            mixer.music.load(song)
            mixer.music.play()
        except Exception as e:
            self.speak(f"Erro ao tocar música: {str(e)}")

    def stop_music(self):
        """Stop playing music"""
        try:
            mixer.music.stop()
        except:
            pass

    def search_wikipedia(self, query):
        """Search Wikipedia and return results"""
        try:
            # Try to search in Portuguese first
            wikipedia.set_lang('pt')
            try:
                result = wikipedia.summary(query, sentences=3)
            except wikipedia.exceptions.DisambiguationError as e:
                # If there are multiple matches, use the first one
                result = wikipedia.summary(e.options[0], sentences=3)
            except wikipedia.exceptions.PageError:
                # If not found in Portuguese, try English
                wikipedia.set_lang('en')
                try:
                    result = wikipedia.summary(query, sentences=3)
                    # Inform that the result is in English
                    self.speak("Encontrei informações apenas em inglês:", also_print=True)
                except:
                    raise Exception("Não encontrado em português nem em inglês")
                
            self.speak("De acordo com a Wikipedia:", also_print=True)
            print(result)  # Print the result
            self.speak(result, also_print=False)  # Speak the result without printing again
            
        except Exception as e:
            error_msg = str(e) if str(e) != "" else "Desculpe, não consegui encontrar informações sobre isso."
            self.speak(error_msg)
            # Suggest a web search
            self.speak("Você gostaria que eu pesquisasse isso no Google?")
            response = self.get_audio()
            if 'sim' in response:
                url = f"https://www.google.com/search?q={query}"
                webbrowser.get().open(url)
                self.speak("Abrindo pesquisa no Google.")

    def extract_query(self, text, phrases):
        """Extract query from text based on search phrases"""
        for phrase in phrases:
            if phrase in text:
                return text.split(phrase, 1)[1].strip()
        return None

    def set_name(self, text):
        """Set or update user name"""
        if 'meu nome é' in text or 'me chamo' in text:
            name = text.split('é')[-1].strip() if 'é' in text else text.split('chamo')[-1].strip()
            if name and name != '[seu nome]':  # Prevent literal placeholder
                old_name = self.user_name
                self.user_name = name
                if old_name:
                    self.speak(f"Ok, vou te chamar de {name} agora!")
                else:
                    self.speak(f"Prazer em conhecê-lo, {name}!")
                return True
        return False

    def test_voice_features(self):
        """Test voice input and output features"""
        print("\n=== Teste de Conversão de Texto para Voz ===")
        test_text = "Testando a conversão de texto para voz. Se você está ouvindo esta mensagem, o sistema está funcionando corretamente."
        print("Reproduzindo texto de teste...")
        self.speak(test_text)

        if self.use_voice_input:
            print("\n=== Teste de Conversão de Voz para Texto ===")
            print("Por favor, fale algo para testar o reconhecimento de voz...")
            text = self.listen()
            if text:
                print(f"\nTexto reconhecido: {text}")
                print("Teste de voz para texto concluído com sucesso!")
            else:
                print("Não foi possível realizar o teste de voz para texto.")

    def show_help(self):
        """Show available commands"""
        self.speak("Aqui está o que eu posso fazer:")
        print("\nComandos disponíveis:")
        print("1. Pesquisar informações:")
        print("   - 'pesquise sobre [tema]'")
        print("   - 'quem foi [pessoa]'")
        print("   - 'o que é [conceito]'")
        print("\n2. YouTube:")
        print("   - 'youtube' (para iniciar uma busca)")
        print("\n3. Entretenimento:")
        print("   - 'conte uma piada'")
        print("   - 'tocar música'")
        print("   - 'parar música'")
        print("\n4. Utilitários:")
        print("   - 'que horas são'")
        print("   - 'esvaziar lixeira'")
        print("\n5. Personalização:")
        print("   - 'meu nome é [seu nome]'")
        print("   - 'corrigir nome'")
        print("\n6. Outros:")
        print("   - 'ajuda' (mostra este menu)")
        print("   - 'testar voz' (testa as funcionalidades de voz)")
        print("   - 'sair' ou 'tchau' (encerra o assistente)")

    def respond(self, text):
        """Respond to commands"""
        # Handle name setting
        if self.set_name(text):
            return

        # Handle name correction
        if 'corrigir nome' in text or 'mudar nome' in text:
            self.speak("Como você gostaria de ser chamado?")
            new_name = self.get_audio()
            if new_name and new_name != '[seu nome]':
                self.user_name = new_name
                self.speak(f"Ok, vou te chamar de {new_name} agora!")
            return

        # Handle help command
        if 'ajuda' in text or 'help' in text:
            self.show_help()
            return

        # Handle greetings
        if any(word in text for word in ['oi', 'olá', 'ola', 'bom dia', 'boa tarde', 'boa noite']):
            greeting = "Olá" if not self.user_name else f"Olá, {self.user_name}"
            self.speak(f"{greeting}! Como posso ajudar?")
            return

        # Handle YouTube search
        if 'youtube' in text:
            self.speak("O que você quer pesquisar?")
            keyword = self.get_audio()
            if keyword != '':
                url = f"https://www.youtube.com/results?search_query={keyword}"
                webbrowser.get().open(url)
                self.speak(f"Aqui está o que encontrei para {keyword} no YouTube")

        # Handle Wikipedia search with various phrases
        elif any(phrase in text for phrase in [
            'pesquisa', 'pesquisar', 'procure', 'procurar',
            'quem é', 'quem foi', 'o que é', 'me fale sobre',
            'pesquise sobre', 'procure sobre', 'busque sobre',
            'buscar', 'busque', 'procure por', 'pesquise por'
        ]):
            search_phrases = [
                'pesquise sobre', 'procure sobre', 'busque sobre',
                'pesquise por', 'procure por', 'busque por',
                'quem é', 'quem foi', 'o que é',
                'me fale sobre', 'pesquisar', 'procurar',
                'buscar', 'pesquisa', 'procure', 'busque'
            ]
            
            query = self.extract_query(text, search_phrases)
            if query:
                self.search_wikipedia(query)
            else:
                self.speak("O que você quer pesquisar?")
                query = self.get_audio()
                if query:
                    self.search_wikipedia(query)

        # Handle jokes
        elif 'piada' in text:
            try:
                joke = pyjokes.get_joke(language='pt')
                self.speak(joke)
            except:
                self.speak("Desculpe, não consegui gerar uma piada no momento.")

        # Handle recycle bin
        elif 'lixeira' in text:
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                self.speak("Lixeira esvaziada")
            except:
                self.speak("Não foi possível esvaziar a lixeira")

        # Handle time
        elif 'horas' in text or 'hora' in text:
            strTime = datetime.today().strftime("%H:%M")
            self.speak(f"Agora são {strTime}")

        # Handle music
        elif 'tocar música' in text or 'música' in text:
            self.speak("Tocando música...")
            try:
                songs = os.listdir(self.music_dir)
                if songs:
                    self.play_music(os.path.join(self.music_dir, songs[0]))
                else:
                    self.speak("Nenhuma música encontrada no diretório")
            except Exception as e:
                self.speak(f"Erro ao acessar músicas: {str(e)}")

        elif 'parar música' in text:
            self.speak("Parando a música.")
            self.stop_music()

        # Handle exit
        elif 'sair' in text or 'tchau' in text:
            farewell = "Até logo" if not self.user_name else f"Até logo, {self.user_name}"
            self.speak(f"{farewell}!")
            exit()

        # Handle unknown commands
        else:
            self.show_help()

def main():
    # Perguntar ao usuário se deseja usar entrada por voz
    print("\n=== Assistente Virtual ===")
    print("\nComo você deseja interagir com o assistente?")
    print("1. Usando texto (digitando)")
    print("2. Usando voz (microfone)")
    
    while True:
        choice = input("\nEscolha uma opção (1 ou 2): ").strip()
        if choice in ['1', '2']:
            break
        print("Opção inválida. Por favor, escolha 1 ou 2.")

    use_voice = (choice == '2')
    
    assistant = VirtualAssistant(use_voice_input=use_voice)
    assistant.clear_screen()
    print("\n=== Assistente Virtual ===")
    print("\nDigite 'ajuda' para ver todos os comandos disponíveis")
    print("Digite 'testar voz' para testar as funcionalidades de voz")
    
    assistant.speak("Olá! Como posso ajudar? Você pode me dizer seu nome dizendo 'meu nome é' seguido do seu nome")
    
    while True:
        text = assistant.get_audio()
        if text == 'testar voz':
            assistant.test_voice_features()
        elif text:
            assistant.respond(text)

if __name__ == "__main__":
    main()

# Assistente Virtual em Python

Este é um assistente virtual desenvolvido em Python que oferece funcionalidades de conversão de texto para voz (text-to-speech) e voz para texto (speech-to-text), além de diversos comandos automatizados.

## Funcionalidades

1. **Conversão de Voz**
   - Text-to-Speech: Converte texto em voz usando Google Text-to-Speech
   - Speech-to-Text: Reconhecimento de voz usando Google Speech Recognition (modo voz)
   - Suporte a português brasileiro

2. **Pesquisa de Informações**
   - Pesquisa na Wikipedia (em português e inglês)
   - Busca no YouTube
   - Pesquisa no Google (fallback quando não encontrado na Wikipedia)

3. **Entretenimento**
   - Contar piadas
   - Tocar música
   - Controle de reprodução musical

4. **Utilitários**
   - Mostrar hora atual
   - Esvaziar lixeira
   - Personalização do nome do usuário

## Requisitos

```bash
pip install -r requirements.txt
```

Os seguintes pacotes são necessários:
- SpeechRecognition: Para reconhecimento de voz
- gTTS (Google Text-to-Speech): Para síntese de voz
- playsound: Para reprodução de áudio
- pyjokes: Para geração de piadas
- wikipedia: Para pesquisas na Wikipedia
- PyAudio: Para captura de áudio do microfone
- pygame: Para reprodução de música
- winshell: Para operações do sistema

## Como Usar

1. Execute o assistente:
```bash
python virtual_assistant.py
```

2. Escolha o modo de interação:
   - Opção 1: Entrada por texto (digitando)
   - Opção 2: Entrada por voz (usando microfone)

3. Testando as funcionalidades de voz:
   - Digite ou fale "testar voz"
   - Para text-to-speech: O assistente reproduzirá uma mensagem de teste
   - Para speech-to-text (modo voz): Fale algo quando solicitado

4. Comandos disponíveis:

### Pesquisar informações:
- "pesquise sobre [tema]"
- "quem foi [pessoa]"
- "o que é [conceito]"
- "me fale sobre [assunto]"

### YouTube:
- "youtube" (para iniciar uma busca)

### Entretenimento:
- "conte uma piada"
- "tocar música"
- "parar música"

### Utilitários:
- "que horas são"
- "esvaziar lixeira"

### Personalização:
- "meu nome é [seu nome]"
- "corrigir nome"

### Outros:
- "ajuda" (mostra o menu de comandos)
- "testar voz" (testa as funcionalidades de voz)
- "sair" ou "tchau" (encerra o assistente)

## Características

- Interface completamente em português
- Síntese de voz natural usando Google Text-to-Speech
- Reconhecimento de voz preciso com Google Speech Recognition
- Pesquisa em português com fallback automático para inglês
- Sistema de tratamento de erros robusto
- Interface de linha de comando amigável
- Sugestão de comandos alternativos
- Modo de teste para funcionalidades de voz

## Estrutura do Projeto

- `virtual_assistant.py`: Código principal do assistente
  - Classe VirtualAssistant: Implementa todas as funcionalidades
  - Métodos de conversão de voz (speak, listen)
  - Gerenciamento de comandos e respostas
  - Sistema de teste de voz integrado

- `requirements.txt`: Lista de dependências do projeto
  - Pacotes necessários para funcionalidades de voz
  - Bibliotecas para recursos adicionais

- `README.md`: Documentação completa do projeto

## Funcionalidades de Voz

### Text-to-Speech (TTS)
- Utiliza Google Text-to-Speech para síntese de voz
- Suporte nativo ao português brasileiro
- Voz clara e natural
- Cache automático para melhor performance

### Speech-to-Text (STT)
- Reconhecimento de voz via Google Speech Recognition
- Suporte a comandos em português
- Ajuste automático para ruído ambiente
- Timeout configurável para melhor usabilidade

## Tratamento de Erros

O assistente inclui tratamento robusto para:
- Falhas de conexão
- Erros de reconhecimento de voz
- Comandos não reconhecidos
- Problemas de reprodução de áudio
- Erros de acesso a recursos

## Contribuição

Sinta-se à vontade para contribuir com o projeto através de Pull Requests ou reportando issues. Áreas para melhoria:
- Adicionar novos comandos
- Melhorar o reconhecimento de voz
- Implementar novos recursos
- Otimizar o desempenho
- Expandir a documentação

## Licença

Este projeto está sob a licença MIT.

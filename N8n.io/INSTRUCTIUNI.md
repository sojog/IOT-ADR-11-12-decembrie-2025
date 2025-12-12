# Ghid de instalare și utilizare n8n

Un ghid vizual pas cu pas pentru instalarea Docker Desktop și n8n, și crearea primului workflow cu AI.

---

## 📋 Cuprins

1. [Instalare Docker Desktop](#1-instalare-docker-desktop)
2. [Instalare n8n cu Docker](#2-instalare-n8n-cu-docker)
3. [Configurare inițială n8n](#3-configurare-inițială-n8n)
4. [Primul workflow](#4-primul-tău-workflow)
5. [Lucrul cu MQTT](#5-lucrul-cu-mqtt)
6. [Lucrul cu AI Agent](#6-lucrul-cu-ai-agent)

---

## 1. Instalare Docker Desktop

### Pasul 1.1: Descarcă și instalează Docker Desktop

Accesează [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop) și descarcă versiunea pentru sistemul tău de operare.

![Instalare Docker Desktop](Images/00.download_docker.png) 

Apoi alege versiunea aferenta sistemului tau de operare

![Instalare Docker Desktop](Images/00.download_docker_specific.png) 

**Figura 1**: Procesul de instalare Docker Desktop. Urmează pașii din wizard pentru a finaliza instalarea.


### Pasul 1.2: Exploreaza interfata

![Interfata Docker Desktop](Images/01.docker_desktop_install.png) 


---

## 2. Instalare n8n cu Docker

### Pasul 2.1: Caută Imaginea n8n

După ce Docker Desktop este instalat și pornit, deschide aplicația Docker Desktop și caută imaginea oficială n8n.

![Căutare imagine n8n](Images/02.docker_n8n_image.png)

**Figura 2**: În Docker Desktop, mergi la secțiunea Images și caută "n8n" pentru a găsi imaginea oficială.

---

### Pasul 2.2: Descarcă Imaginea

![Descărcare imagine n8n](Images/03.docker_image_download.png)

**Figura 3**: Click pe butonul "Pull" pentru a descărca imaginea n8n pe calculatorul local.

---

### Pasul 2.3: Rulează Imaginea

![Rulare imagine n8n](Images/04.docker_run_image.png)

**Figura 4**: După descărcare, click pe butonul "Run" pentru a crea un container nou din imaginea n8n.

---

### Pasul 2.4: Configurează Containerul

![Configurare container](Images/05.docker_run_container.png)

**Figura 5**: Configurează portul (ex: 5678) și alte setări opționale pentru container. Click "Run" pentru a porni containerul.

---

### Pasul 2.5: Verifică Containerul Activ

![Container activ](Images/07.docker_container.png)

**Figura 6**: Verifică în secțiunea "Containers" că containerul n8n rulează corect (status: Running).

---

## 3. Configurare Inițială n8n

### Pasul 3.1: Accesează Interfața n8n

Deschide browser-ul și navighează la `http://localhost:5678`

![Login n8n](Images/08.n8n_login.png)

**Figura 7**: Ecranul de autentificare n8n. Aici vei crea contul de owner pentru prima dată.

---

### Pasul 3.2: Personalizează Setările

![Personalizare n8n](Images/09.n8n_customize.png)

**Figura 8**: Completează informațiile despre profilul tău - nume, rol, tipul de utilizare.

---

### Pasul 3.3: Cheia de Activare (Opțional)

![Cheie de activare](Images/10.activation_key.png)

**Figura 9**: Dacă ai o cheie de activare pentru funcționalități premium, o poți introduce aici. Pentru versiunea self-hosted de bază, poți sări peste acest pas.

---

### Pasul 3.4: Activare prin Email (Opțional)

![Formular email activare](Images/11.activation_email_form.png)

**Figura 10**: Completează formularul cu email-ul tău pentru a primi notificări și update-uri.

---

![Email primit](Images/12.activation_email_received.png)

**Figura 11**: Confirmarea că email-ul de activare a fost trimis cu succes.

---

## 4. Primul workflow

### Pasul 4.1: Începe un workflow nou

![Start workflow](Images/13.start_workflow.png)

**Figura 12**: Din dashboard, click pe "New workflow" sau folosește unul din template-urile disponibile.

---

### Pasul 4.2: Adaugă Primul Pas

![Adaugă pas](Images/14.add_step.png)

**Figura 13**: Click pe "+" pentru a adăuga un nod în workflow. Aici începe construcția automatizării tale.

---

### Pasul 4.3: Alege un Trigger

![Triggers disponibile](Images/15.triggers.png)

**Figura 14**: Selectează un trigger care va porni workflow. Opțiunile includ webhook-uri, schedule, email trigger, etc.

---

### Pasul 4.4: Configurează Schedule Trigger

![Schedule trigger](Images/16.schedule_trigger.png)

**Figura 15**: Exemplu de configurare a unui Schedule Trigger care rulează workflow-ul la intervale regulate (zilnic, săptămânal, custom cron).

---

### Pasul 4.5: Explorează Aplicațiile Disponibile

![Exemplu aplicații](Images/17.app_example.png)

**Figura 16**: n8n oferă sute de integrări pre-construite cu diverse aplicații și servicii populare.

---

### Pasul 4.6: Caută Aplicația Dorită

![Căutare aplicație](Images/18.search_app.png)

**Figura 17**: Folosește bara de căutare pentru a găsi rapid aplicația sau serviciul cu care vrei să te conectezi.

---

## 5. Lucrul cu MQTT

### Pasul 5.1: Trigger MQTT

![On Chat Message](Images/24.mqtt_trigger.heic)

**Figura 18**: Triggerul mqtt functionează ca celelalte trigger (click etc).

---

### Pasul 5.2: Setarea Triggerului

![AI Agent](Images/25.mqtt_setup.heic)

---

### Pasul 5.3: Setarea Topicului

![Model AI](Images/26.mqtt_setup2.heic)


---

## 6. Lucrul cu AI Agent (Opțional)

### Pasul 6.1: Nodul On Chat Message

![On Chat Message](Images/19.on_chat.png)

**Figura 18**: Nodul "When chat message received" - trigger pentru aplicații conversaționale și chatbot-uri.

---

### Pasul 6.2: Adaugă AI Agent

![AI Agent](Images/20.ai_agent.png)

**Figura 19**: Nodul AI Agent permite crearea de agenți inteligenți care pot folosi diverse tool-uri pentru a rezolva task-uri complexe.

---

### Pasul 6.3: Configurează Modelul AI

![Model AI](Images/21.ai_model.png)

**Figura 20**: Configurează modelul AI (OpenAI, Anthropic Claude, etc.) și setările acestuia - temperatura, max tokens, system prompt.


### Pasul 6.4: Configurează Ollama

![Model AI](Images/22.ollama_model.png)

**Figura 21**: Alege ollama.


### Pasul 6.3: Trebuie sa setezi linkul catre ollama

![Model AI](Images/23.ollama_point.png)

**Figura 22**: Alege ollama cu setarea http://host.docker.internal:11434.

---


## ⚡ Comenzi Rapide Docker

```bash
# Verifică status container
docker ps

# Vezi logs n8n
docker logs -f <container_id>

# Oprește container
docker stop <container_id>

# Pornește container
docker start <container_id>

# Restart container
docker restart <container_id>
```

---

## 🔧 Configurare Avansată (Opțional)

Pentru o configurare mai avansată cu PostgreSQL și volume persistente, creează un fișier `docker-compose.yml`:

```yaml
version: '3.8'

services:
  n8n:
    image: n8nio/n8n:latest
    container_name: n8n
    restart: unless-stopped
    ports:
      - "5678:5678"
    environment:
      - N8N_HOST=localhost
      - N8N_PORT=5678
      - N8N_PROTOCOL=http
      - NODE_ENV=production
      - WEBHOOK_URL=http://localhost:5678/
      - GENERIC_TIMEZONE=Europe/Bucharest
    volumes:
      - n8n_data:/home/node/.n8n

volumes:
  n8n_data:
    driver: local
```

Apoi rulează:

```bash
docker-compose up -d
```

---

## 📚 Resurse Suplimentare

- **Documentație Completă**: Consultă fișierul `INSTRUCTIONS_RO.md` pentru ghidul complet
- **Documentație Oficială**: [https://docs.n8n.io](https://docs.n8n.io)
- **Comunitate**: [https://community.n8n.io](https://community.n8n.io)
- **Video Tutorials**: [https://www.youtube.com/@n8n-io](https://www.youtube.com/@n8n-io)

---

## ✅ Checklist Post-Instalare

- [ ] Docker Desktop instalat și pornit
- [ ] Container n8n rulează corect
- [ ] Accesat interfața la `http://localhost:5678`
- [ ] Creat cont owner n8n
- [ ] Creat primul workflow de test
- [ ] Testat un trigger simplu
- [ ] Explorat nodurile disponibile

---

## 🆘 Probleme Comune

### n8n nu pornește

```bash
# Verifică logs
docker logs <container_id>

# Verifică dacă portul 5678 este liber
netstat -an | grep 5678

# Restart container
docker restart <container_id>
```

### Nu pot accesa interfața

- Verifică că browserul accesează `http://localhost:5678`
- Verifică firewall-ul
- Verifică că containerul rulează: `docker ps`

### Workflow-ul nu se salvează

- Verifică că ai suficient spațiu pe disk
- Verifică permissions pentru volume
- Verifică logs pentru erori

---



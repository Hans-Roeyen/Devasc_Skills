# Devasc_Skills
## NETACAD-DEVASC SKILLS-BASED EXAM December 2020

### Task 1 Manage github scripts and documents

#### Task Preperation
1. Bestaande GitHub account online nakijken
2. Controleren of mijn Github user information aanwezig, actueel en correct is op lokale werkomgeving.
3. Remote repository aanmaken op Github.com voor deze opdracht.

#### Task implementation
1. De directory **"Devasc_Skills"** aanmaken
2. Git initialiseren
   1. "git init"
3. Testbestand **"Github-Test.txt"** in directory plaatsen
4. Staging the file
   1. git add Github-Test.txt
5. Tracking changes
   1. git commit -m "Task 1: Manage github scripts and documents"
   2. Het argument " -m " Laat toe om de wijziging te taggen
6. De lokale directory koppelen aan de remote repository
   1. git remote add origin `https://github.com/Hans-Roeyen/Devasc_Skills.git`
7. Wijzigingen naar remote repository uploaden
   1. git push origin master
8. Controle van status op Github

#### Task troubleshooting
1. De verandering op Github van Master naar Main heb ik proberen door te voeren. 
2. Dat gaf meer problemen dan ik op korte tijd kon oplossen.
3. Daarom blijf ik gebruik maken van Master als Default Branch.
  
#### Task verification
1. Afbeelding **Task1-Github.jpg** van Github repository met weergave van het bestand: **"Github-Test.txt"** in de Devasc_Skills repository
    1. https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task1-Github.jpg
2. Afbeelding **Task1-Github-ReadmeUpdate.jpg** van Github repository na **update van README**:
    1. https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task1-Github-ReadmeUpdate.jpg
  
### Task 2 Manage ansible scripts

#### Task Preperation
1. Download van bronbestand opgave naar VM
2. Installatie van **ansible-galaxy collection install cisco.ios** in VM
3. Bestanden aanmaken voor in de **Devasc_Skills directory**
   1. Ansible inventory file **hosts**
   2. Configuratiebestand **ansible.cfg**
   3. Ansible Playbook **IOS_COMMANDS_PB.yaml**
   4. Connectie tussen VM’s controleren met **PING**

#### Task implementation
1. Configuratie van het bestand: **hosts**
2. Configuratie van het bestand: **ansible.cfg**
3. Configuratie van het bestand: **IOS_COMMANDS_PB.yaml**
4. Uitvoeren Ansible Playbook
   1. devasc@labvm:~/Devasc_Skills$ ansible-playbook IOS_COMMANDS_PB.yaml

#### Task troubleshooting
1. De juiste configuratie van de Ansible Playbook gaf foutmeldingen:
   1. [WARNING]: Could not match supplied host pattern, ignoring: CSR1Kv
   2. De oorzaak was een foute configuratie in het bestand **IOS_COMMANDS_PB.yaml**
   3. In het bestand de configuratie **connection: local** eerst weggelaten maar later toegevoegd
  
#### Task verification
1. De configuratie bestanden van Task2 in de Github repository:
   1. **IOS_COMMANDS_PB.yaml** 
      1. https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/IOS_COMMANDS_PB.yaml
   2. **ansible.cfg**
      1. https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/ansible.cfg
   3. **hosts** met de "Tag" in de **Task 2: Manage ansible scripts**
      1. https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/hosts
2. Afbeelding **Task2-Ansible.jpg** is het resultaat van het uitvoeren van de Ansible Playbook:
   1. https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task2-Ansible.jpg)
3. Afbeelding **Task2-Ansible-Extra.jpg** is een alternatief resultaat van het uitvoeren van de Ansible Playbook na toevoegen van een Loopback interface op CSR1kv:
   1. https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task2-Ansible-Extra.jpg)
  
### Task 3 Manage Docker microservcies
  
#### Task Preperation
1. Documentatie van de beschikbare Docker voorbeelden van NTP servers onderzoeken op compatibiliteit met Linux Host VM
  
#### Task implementation
1. Creatie van Dockerfile:
   1. https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task3-CreateDockerfile.jpg
2. Docker image maken met: docker build
3. Docker container opstarten: docker run:
   1. https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task3-Docker-run.jpg
  
#### Task troubleshooting
1. Het was me niet onmiddellijk duidelijk hoe ik kon aantonen dat de NTP server actief was.
2. Na een korte zoektocht heb ik commands: **ntpq -pn** en **ntpq -p** gebruikt om de werking van de NTP server aan te tonen.
3. Hopelijk toont de output van de screenshot (Task3-NTP-server.jpg.) dit voldoende aan.
  
#### Task verification
1. Nakijken werking NTP server via toegang tot Docker container met command: docker exec
   1. https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task3-Docker-exec.jpg
2. Controle NTP server met "ntpq -pn" en "ntpq -p"
   1. https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task3-NTP-server.jpg
    
### Task 4 CI/CD Pipeline using jenkins
1. Door tijdsgebrek heb ik deze taak niet kunnen maken.   
      
### Task 5 Virtual router: curl => Python
  
#### Task Preperation
1. Alle cURL requests testen op virtuele router
2. Onderzoek van structuur Yang Model
3. Activeren "Logging Monitor" op virtuele router
  
#### Task implementation
1. OPTIONS
   1. Resultaat: https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task5-restconf-sol-01.py
2. POST
   1. Resultaat: https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task5-restconf-sol-02.py
3. PUT
   1. Resultaat: https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task5-restconf-sol-03-2.py
4. PATCH
   1. Resultaat: https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task5-restconf-sol-04.py
5. GET
   1. Resultaat: https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task5-restconf-sol-05.py
6. DELETE
   1. Resultaat: https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task5-restconf-sol-06.py
7. Extra: om het resultaat van een aantal opdrachten na te kijken heb ik een extra Python script gebruikt:
   1. Resultaat: https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task5-restconf-sol-06-controle.py
     
#### Task troubleshooting
1. Connectie met virtuele router (authentication) gaf plots een error: "Warning Remote Host Identification Has Changed"
   1. De snelste oplossing was een nieuwe versie van de virtuele router maken.
   2. Gevolg: een ander IP Adres (Oud IP: 192.168.41.128 - Nieuw IP: 192.168.41.129)
     
#### Task verification
1. Screenshot van Task 4 PATCH: https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task5-Resultaat.jpg
2. De Python scripts van Task5 staan bij de bestanden, met telkens de Tag "Task5 Python oplossingen".

### Task 6 Create Webex Teams API calls using a Python script
  
#### Task Preparation
1. Een Access-Token ophalen op Cisco Webex for Developers:
   1. https://developer.webex.com/docs/api/v1/people/get-my-own-details
2. Authentication met het opgehaalde Token testen via Python:
   1. https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task6-Access-Token.py
3. Resultaat:
   1. https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task6-Test-Access-Token.jpg

#### Task implementation
1. Een Room (space) aanmaken in Webex Teams via Python:
   1. https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task6-CreateRoom.py
2. Toevoegen van een Member aan de Room:
   1. https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task6-CreateRoomMembership.py
3. De URL publiceren van de GitHub repository in deze Room:
4. Bericht naar deze Room verzenden om indienen van de taak te melden:
   1. https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task6-SendMessage-Webex.py

#### Task troubleshooting
1. Geen specifieke problemen moeten oplossen
  
#### Task verification
1. Eindresultaat in Webex Teams
   1. https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task6-Resultaat-Webex-Einde.jpg

  

### Task 7 Web application security
1. Door tijdsgebrek heb ik deze taak niet kunnen maken. 

### Task 8 Unit testing
1. Door tijdsgebrek heb ik deze taak niet kunnen maken. 

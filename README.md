# Devasc_Skills
## NETACAD-DEVASC SKILLS-BASED EXAM December 2020

### Task 1 Manage github scripts and documents

#### Task Preperation
  1. Bestaande GitHub account online nakijken
  2. Controleren of mijn Github user information aanwezig, actueel en correct is op lokale werkomgeving.
  3. Remote repository aanmaken op Github.com voor deze opdracht.

#### Task implementation
  1. De directory *"Devasc_Skills"* aanmaken
  2. Git initialiseren met => *"git init"*
  3. Testbestand *"Github-Test.txt"* in directory plaatsen
  4. Staging the file met => *git add Github-Test.txt*
  5. Tracking changes met => *git commit -m "Task 1: Manage github scripts and documents"*
     Het argument " -m " Laat toe om de wijziging te taggen
  6. De lokale directory koppelen aan de remote repository => *git remote add origin https://github.com/Hans-Roeyen/Devasc_Skills.git*
  7. Wijzigingen naar remote repository uploaden => *git push origin master*
  8. Controle van status op Github

#### Task troubleshooting
  1. De verandering op Github van Master naar Main heb ik proberen door te voeren. Dat gaf meer problemen dan ik op korte tijd kon oplossen. Daarom blijf ik gebruik maken van Master als Default Branch.
  
#### Task verification
  1. Afbeelding *Task1-Github.jpg* van Github repository met weergave van het bestand: *"Github-Test.txt"* in de Devasc_Skills repository
  https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task1-Github.jpg
  2. Afbeelding *Task1-Github-ReadmeUpdate.jpg* van Github repository na *update van README*: https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task1-Github-ReadmeUpdate.jpg
  
### Task 2 Manage ansible scripts

#### Task Preperation
  1. Download van bronbestand opgave naar VM
  2. Installatie van *ansible-galaxy collection install cisco.ios* in VM
  3. Bestanden aanmaken voor in de *Devasc_Skills directory*
     A. Ansible inventory file *hosts*
     B. Configuratiebestand *ansible.cfg*
     C. Ansible Playbook *IOS_COMMANDS_PB.yaml*
     D. Connectie tussen VM’s controleren met *PING*

#### Task implementation
  1. Configuratie hosts: 
       *CSR1kv ansible_user=cisco ansible_password=cisco123! ansible_host=192.168.41.128* 
       (IP Address is op mijn lokaal netwerk)
  2. Configuratie ansible.cfg: 
       *inventory=./hosts*
       *host_key_checking = False # Don't worry about RSA Fingerprints*
       *retry_files_enabled = False # Do not create them*
       *deprecation_warnings = False # Do not show warning*
  3. Configuratie IOS_COMMANDS_PB.yaml:
       *---
        *- name: IOS_COMMANDS_PB*
        -hosts: CSR1kv-
        *gather_facts: false*
        *connection: local*
  4. Uitvoeren Ansible Playbook => *devasc@labvm:~/Devasc_Skills$ ansible-playbook IOS_COMMANDS_PB.yaml*

#### Task troubleshooting
  1. De juiste configuratie van de Ansible Playbook gaf foutmeldingen: *[WARNING]: Could not match supplied host pattern, ignoring: CSR1Kv*
     De oorzaak was een foute configuratie in het bestand *IOS_COMMANDS_PB.yaml* => *connection: local* eerst weggelaten maar later toegevoegd
  
#### Task verification
  1. Afbeelding met weergave van de configuratie bestanden in de Github repository:
  A. *IOS_COMMANDS_PB.yaml* met de "Tag" in de *Task 2: Manage ansible scripts*
  B. *ansible.cfg* met de "Tag" in de *Task 2: Manage ansible scripts*
  C. *hosts* met de "Tag" in de *Task 2: Manage ansible scripts*
  2. Afbeelding *Task2-Ansible.jpg* is het resultaat van het uitvoeren van de Ansible Playbook: https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task2-Ansible.jpg)
  3. Afbeelding *Task2-Ansible-Extra.jpg* is een alternatief resultaat van het uitvoeren van de Ansible Playbook na toevoegen van een Loopback interface op CSR1kv: https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task2-Ansible-Extra.jpg)
  
  
  ### Task 3 Manage Docker microservcies
  #### Task Preperation
  #### Task implementation
  #### Task troubleshooting
  #### Task verification
  
    
  ### Task 4 CI/CD Pipeline using jenkins
  #### Task Preperation
  #### Task implementation
  #### Task troubleshooting
  #### Task verification
  
      
  ### Task 5 Virtual router: curl => Python
  #### Task Preperation
  #### Task implementation
  #### Task troubleshooting
  #### Task verification

      
  ### Task 6 Create Webex Teams API calls using a Python script
  
  #### Task Preparation
  1. Een Access-Token ophalen op Cisco Webex for Developers: https://developer.webex.com/docs/api/v1/people/get-my-own-details
  2. Authentication met het opgehaalde Token testen via Python: https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task6-Access-Token.py
  3. Resultaat: https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task6-Test-Access-Token.jpg

  #### Task implementation
  1. Een Room (space) aanmaken in Webex Teams via Python: https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task6-CreateRoom.py
  2. Toevoegen van een Member aan de Room: https://github.com/Hans-Roeyen/Devasc_Skills/tree/master/Task6-CreateRoomMembership.py
  3. De URL publiceren van de GitHub repository in deze Room: nog uit te voeren
  3. Bericht deze Room verzenden: Testbericht gemaakt om schript te testen (is ok)

  #### Task troubleshooting
  1. Geen specifieke problemen moeten oplossen
  
  #### Task verification
  1. Definitief resultaat nog niet beschikbaar
  
  
  ### Task 7 Web application security
  #### Task Preperation
  #### Task implementation
  #### Task troubleshooting
  #### Task verification
  
  
  ### Task 8 Unit testing
  #### Task Preperation
  #### Task implementation
  #### Task troubleshooting
  #### Task verification

#Go to Igit Folder
#Start vitual enivorement
#Start Python Shell
from IGitt.GitLab.GitLabMilestone import GitLabMilestone #Import GitLabMilestone Class from the GitLabMilestone.py file
from IGitt import GitLab #Folder IGitt check Folder GitLab and import __init__.py
Token = GitLab.GitLabOAuthToken("sPYpZLhWQ2Mi4k7ppVxz") #Create a Token Instance
TestMilestone = GitLabMilestone(Token, "seblat/test-milestones", 42) #Create a Milestone Instance

#Debugen
TestMilestone.url #Url des Testmilestones ausgeben. --> Auf eine öffentliche anpassen
# URL im Browser aufrufen und schauen, ob ein JSON zurück kommt
# Auf den Ebenen immer weiter zurück gehen, bis es funktioniert:
## Spezifischer Milestone --> Alle Milestones
## Alle Milestones --> Projekt

#Weiterbauen
##Schritt für schritt das von der GitLab API Doku implementieren
###Dazwischen immer commiten!


#Versuch den Titel anhand der ID zu ziehen
## Getter nicht implementiert
###--> TODO Getter implementieren
#### "401, not authorized"
##### Lösung: Falsches TOken verweendet, statt OAuth das Private verwenden
#### Warum wird das nicht im Interface implementiert?
In [1]: from IGitt import GitLab

In [2]: from IGitt.GitLab.GitLabMilestone import GitLabMilestone

In [3]: Token = GitLab.GitLabPrivateToken("sPYpZLhWQ2Mi4k7ppVxz")

In [4]: TestMilestone = GitLabMilestone(Token, "seblat/test-milestones", 489327)

In [5]: TestMilestone.url
Out[5]: 'https://gitlab.com/api/v4/projects/seblat%2Ftest-milestones/milestones/489327'

In [6]: TestMilestone.title
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
<ipython-input-6-509591f791d1> in <module>()
----> 1 TestMilestone.title

~/code/IGitt/IGitt/Interfaces/Milestone.py in title(self)
     34         Retrieves the title of the milestone.
     35         """
---> 36         raise NotImplementedError
     37
     38     @title.setter

NotImplementedError:
"""

#Versuch einen Milestone zu erstellen
##Sollte eigentlich funktionieren, sagt aber nicht authorisiert
## Auch hier durch das Private Token gefixt
### Self fehlt nach get / put update auch --> Statt self, GItLab Miletsone

In [7]: TestMilestoneCreation = GitLabMilestone.create(Token, "seblat/test-milestones", "IGitt created milestone")
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
<ipython-input-7-a97b9e454c37> in <module>()
----> 1 TestMilestoneCreation = GitLabMilestone.create(Token, "seblat/test-milestones", "IGitt created milestone")

~/code/IGitt/IGitt/GitLab/GitLabMilestone.py in create(token, scope, title)
     61         """
     62         url = '/projects/{scope}/milestones'.format(scope=quote_plus(scope))
---> 63         milestone = post(token, url, {'title': title})
     64
     65         return GitLabMilestone(token, scope, milestone['iid'])

~/code/IGitt/IGitt/GitLab/__init__.py in post(token, url, data, headers)
    143         If the response indicates any problem.
    144     """
--> 145     return _fetch(BASE_URL, 'post', token, url, data, headers=headers)
    146
    147

~/code/IGitt/IGitt/Interfaces/__init__.py in _fetch(base_url, req_type, token, url, data, query_params, headers)
    138     }
    139     method = req_methods[req_type]
--> 140     resp = get_response(method, base_url + url, json=data)
    141
    142     # DELETE request returns no response

~/venv/igitt/lib/python3.6/site-packages/backoff/_sync.py in retry(*args, **kwargs)
     83
     84             try:
---> 85                 ret = target(*args, **kwargs)
     86             except exception as e:
     87                 if giveup(e) or tries == max_tries_:

~/venv/igitt/lib/python3.6/site-packages/backoff/_sync.py in retry(*args, **kwargs)
     83
     84             try:
---> 85                 ret = target(*args, **kwargs)
     86             except exception as e:
     87                 if giveup(e) or tries == max_tries_:

~/code/IGitt/IGitt/Interfaces/__init__.py in get_response(method, url, json)
    104         return _RESPONSES[url]
    105     elif response.status_code >= 300:
--> 106         raise RuntimeError(response.text, response.status_code)
    107     _RESPONSES[url] = response
    108     return response

RuntimeError: ('{"message":"401 Unauthorized"}', 401)

#Module vs. Klassen
##Die dateien (.py heißen module)
##Die Klassen innerhalb der Dateien heißen Klassen
##Bei einem import wird abhängig von der Pfdatiefe (im from) entweder die datei (modul) oder die Klasse importiert
###Wurde die Datei (Modul) importiert und möchte man eine Klasse daraus aufrufen, geht das mit Modul.Klasse()

#Module updaten
import imp
imp.reload(Modul) #Das Modul ohne Anführungszeichen (Ist ja ein Modul, kein String)

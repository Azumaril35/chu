### Prérequis

1. Installer python (Version utilisée en développement : 3.11.4)

2. Créer un environnement virtuel (python -m venv env) et l'activer (.\env\Scripts\activate sur Windows ou source env/bin/activate sur Linux et MacOs)

3. Installer les dépendances (pip install -r requirement.txt)

4. A la racine, au même niveau que requirement.txt ou manage.py, créer un fichier "db.sqlite3" si il n'existe pas déjà

5. Créer les migrations pour la base de donnée (python manage.py makemigrations)

6. Lancer ces migrations (python manage.py migrate)

7. Lancer le serveur de développement django (python manage.py runserver)

8. (Optionnel) Créer un identifiant pour se connecter à django admin en utilisant la commande python manage.py createsuperuser
   Cet identifiant permettra entre-autre de tester la page des conflits et ajoute la possibilité de supprimer les événements que je n'ai pas implémenté puisque non demandée par l'exercice

Les urls demandées sont accessibles à ces adresses :

- http://127.0.0.1:8000/list_events/ (GET) (Liste les événements et permet l'ajout de nouveaux évenements)
- http://127.0.0.1:8000/list_events/ (POST) (Liste les événements et permet l'ajout de nouveaux évenements)
- http://127.0.0.1:8000/list_conflicts/ (GET) (Liste les événements en conflit. Comme l'ajout d'événements en conflit est contrôlé par la méthode POST de la page list_events, vous devez créer les évenements via django admin http://127.0.0.1:8000/admin/event_planner/event/add/)

9. Pour lancer les tests, exécuter la commande python manage.py test
   Il y a 11 tests:
   - Tester la création d'un event
     Pour tester le model django sans passer par la fonction add_event
   - Tester la page qui affiche la liste des événements
   - Tester la création d'événements depuis cette même page avec une requête POST et vérifier la redirection vers la page list_events_view
   - Tester la liste des événements en conflit, vérifier dans un premier temps qu'elle ne revoit aucun résultat
   - Tester à nouveau la liste des événements en conflit en créant 2 événements en confit
   - Test de la fonction "add_event" demandé dans l'exercice pour l'ajout d'un événement sans conflit
   - Tester à nouveau cette fonction pour vérifier qu'elle renvoit une erreur si il y un confit entre l'événement en cours d'ajout et un événement déjà créé dans la base de donnée.
   - Tester la fonction list_events de l'exercice, vérifier qu'elle renvoi le bon nombre d'événements triés par heure de début
   - Tester la fonction find_conflicts sans conflit
   - Tester la fonction find_conflicts avec conflit
   - Tester le message d'erreur si l'heure de fin est avant l'heure de début

---

1. Install Python (Version used in development: 3.11.4)

2. Create a virtual environment (python -m venv env) and activate it (.\env\Scripts\activate on Windows or source env/bin/activate on Linux/MacOs)

3. Install dependencies pip install -r requirement.txt

4. At the project root, at the same level as requirement.txt or manage.py, create a file named db.sqlite3 if it does not already exist.

5. Create migrations for the database (python manage.py makemigrations)

6. Apply the migrations (python manage.py migrate)

7. Start the Django server (python manage.py runserver)

8. (Optional) Create a Superuser
   Create an admin user to access Django Admin (python manage.py createsuperuser)
   This account allows you to test the conflicts page and optionally delete events.

The requested URLs are accessible at:

- List Events (GET and POST): http://127.0.0.1:8000/list_events/
- List Conflicts (GET): http://127.0.0.1:8000/list_conflicts/
- Note: Event conflicts are managed by the list_events POST method. You can create conflicting events through Django Admin.

9. To run the tests: (python manage.py test)

The tests include:

- Testing event creation
- Testing event list page display
- Testing event creation via POST request
- Testing conflicts list display (initially empty, then adding conflicts)
- Testing the add_event function with non-conflicting and conflicting events
- Testing list_events for correct event sorting
- Testing find_conflicts without and with conflicts
- Testing form error message if end_time < start_time

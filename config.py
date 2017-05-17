DEBUG = True # Turns on debugging features in Flask
BCRYPT_LEVEL = 12 # Configuration for the Flask-Bcrypt extension
MAIL_FROM_EMAIL = "robert@example.com" # For use in application emails
SITE_STRUCT = {
    'Entreprise':'items',
    'Contexte.accroche':'texte',
    'Contexte.detail':'texte',
    'Combat.accroche':'texte',
    'Combat.raisons':'texte',
    'Combat.actions':'texte',
    'Combat.message':'texte',
    'Soutien.accroche':'texte',
    'Soutien.rdv':'dates',
    'Soutien.financier':'cartes',
    'Soutien.petitions':'cartes'
}

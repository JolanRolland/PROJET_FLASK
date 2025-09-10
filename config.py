import random, string, os
"".join([random.choice(string.printable) for _ in os.urandom(24)])
SECRET_KEY = "2lzUl{$*D6#`8uXqlU."

ABOUT = "Bienvenue sur la page à propos de Flask !"
CONTACT = "Page contact : vous pouvez nous écrire sur contact@tutoflask.fr"
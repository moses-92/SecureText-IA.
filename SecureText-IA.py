def crypter_message(texte, cle):
    texte_crypte = ""
    for caractere in texte:
        # On décale chaque caractère dans la table ASCII pour le rendre secret
        texte_crypte += chr(ord(caractere) + cle)
    return texte_crypte


def decrypter_message(texte_crypte, cle):
    texte_decrypte = ""
    for caractere in texte_crypte:
        # On fait l'opération inverse pour retrouver le vrai texte
        texte_decrypte += chr(ord(caractere) - cle)
    return texte_decrypte


# === ZONE DE TEST DU SCRIPT ===
print("🔐 --- LOGICIEL DE CRYPTOGRAPHIE IA --- 🔐\n")

# 1. Le message secret de départ
message_original = "Mon objectif est de gagner mes premiers dollars en ligne !"
cle_secrete = 7  # La clé de décalage (votre mot de passe)

print(f"📄 Message d'origine : {message_original}")

# 2. Phase de chiffrement
message_code = crypter_message(message_original, cle_secrete)
print(f"🛑 Message chiffré (illisible) : {message_code}")

# 3. Phase de déchiffrement
message_retrouve = decrypter_message(message_code, cle_secrete)
print(f"🔓 Message décrypté par l'IA   : {message_retrouve}")

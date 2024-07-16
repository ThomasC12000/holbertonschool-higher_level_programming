def generate_invitations(template, attendees):
    # Vérification des types d'entrée
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return
    
    # Vérification des entrées vides
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Traitement de chaque invité et génération des fichiers
    for index, attendee in enumerate(attendees, start=1):
        output_content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            output_content = output_content.replace(f"{{{key}}}", value if value else "N/A")
        
        # Nom du fichier de sortie
        output_filename = f"output_{index}.txt"
        
        # Écriture du contenu dans le fichier
        with open(output_filename, 'w') as output_file:
            output_file.write(output_content)

# Exemple d'utilisation
if __name__ == "__main__":
    # Lecture du modèle depuis un fichier
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # Liste des invités
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Appel de la fonction avec le modèle et la liste des invités
    generate_invitations(template_content, attendees)
def extract_article_info(text):
    # Dividi il testo in righe
    lines = text.split('\n')

    # Inizializza le variabili per titolo, abstract e parole chiave
    title = ''
    abstract = ''
    keywords = ''

    # Indica se stiamo attualmente analizzando l'abstract o le parole chiave
    in_abstract = False
    in_keywords = False

    # Scansiona le righe del testo
    for line in lines:
        # Se la riga inizia con "ABSTRACT", inizia l'analisi dell'abstract
        if line.lower().startswith('abstract'):
            in_abstract = True
            continue
        # Se la riga inizia con "KEYWORDS", inizia l'analisi delle parole chiave
        elif line.lower().startswith('keywords'):
            in_abstract = False
            in_keywords = True
            continue

        # Se siamo nell'abstract, aggiungi la riga all'abstract
        if in_abstract:
            abstract += line.strip() + '\n'
        # Se siamo nelle parole chiave, aggiungi la riga alle parole chiave
        elif in_keywords:
            keywords += line.strip()

        # Se non siamo né nell'abstract né nelle parole chiave, considera la riga come titolo
        else:
            title += line.strip()

    return title, abstract, keywords


def generate_article_html(title, abstract, keywords):
    html_template = """
    <b>{title}</b>

    <details style="background: #eee; margin-bottom: 2rem; padding: .5rem 1rem;">
    </br>
    <p>
    <b>ABSTRACT</b></br>
    {abstract}
    </p>
    <p>
    <b>KEYWORDS:</b> {keywords}
    </p>
    </details>
    """

    return html_template.format(title=title, abstract=abstract, keywords=keywords)




text = """
asdasdasdasdasdsadsa

ABSTRACT
dfdfdfdfdfdfdfdfdf
KEYWORDS: dfdfdfdfdfdfdfdfd
"""

title, abstract, keywords = extract_article_info(text)

# Stampa i risultati
print("Titolo:", title)
print("\n")
print("Abstract:", abstract)
print("\n")
print("Parole chiave:", keywords)



# Esempio di utilizzo
article_title = title
article_abstract = abstract
article_keywords = keywords

html_output = generate_article_html(article_title, article_abstract, article_keywords)
print(html_output)

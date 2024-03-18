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
La potenza marittima e i suoi limiti: un punto di vista teorico
Federico Bordonaro
Vision & Global Trends. International Institute for Global Analyses
(Progetto Società Italiana di Geopolitica)

ABSTRACT
This article investigates the limits of maritime power, by critically analyzing the theorizations of Jakub Grygiel, Saul B. Cohen and Randall Collins in light of the new phase of geopolitical competition marked by both warlike (Ukraine) and potentially military (Taiwan) conflicts having, among the main issues at stake, the control of closed seas, straits, archipelagos, coastlines and maritime trade routes.
The impression is that the limits of maritime power inevitably emerge in the event that states lose their positional and comparative human resources advantages over their competitors, especially in phases of rapid diffusion of technological innovations. Therefore, the key to global geopolitical dominance does not lie simply in dominating the seas or, on the contrary, the continental mass, but in having the aforementioned advantages over rivals, not only by force, but also through a diplomatic strategy capable of co-opting allies.
KEYWORDS: Maritime Power, Geopolitical Theory, NATO
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

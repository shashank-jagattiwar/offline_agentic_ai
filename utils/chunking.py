def chunk_text(text, chunk_size=200):
    """
    Splits text into chunks of roughly 'chunk_size' words.
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i + chunk_size]))
    return chunks

#! python3
import docx


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for paragraph in doc.paragraphs:
        fullText.append("  " + paragraph.text)
    return "\n\n".join(fullText)

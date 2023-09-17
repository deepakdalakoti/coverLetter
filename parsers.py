from typing import Any
import logging
import fitz
import docx


logger = logging.getLogger(__name__)


class Parser:
    def __init__(self) -> None:
        pass

    def parse(self, filename: str, file):
        extension = filename.split(".")[-1]
        print(extension)
        logger.debug(f"Received extension {extension}")
        if extension == "pdf":
            print("parsing pdf")
            return self._parse_pdf(file)
        elif extension == "docx":
            return self._parse_word(file)
        else:
            raise NotImplementedError(
                f"This file format is not implemented! {extension}"
            )

    def _parse_pdf(self, filename):
        doc = fitz.open(filename)
        text = []
        print(doc)
        for page in doc:
            # print(page)
            # print(page.get_text())
            text.append(
                page.get_text(sort=True).encode("utf8").decode("ascii", errors="ignore")
            )
        return "\n".join(text)

    def _parse_word(self, filename):
        doc = docx.Document(filename)
        text = ""
        for element in doc.element.body:
            if isinstance(element, docx.text.paragraph.Paragraph):
                # Append the text of each paragraph to the document_text string
                text += element.text + "\n"
            elif isinstance(element, docx.table.Table):
                # Iterate through rows and cells in each table
                for row in element.rows:
                    for cell in row.cells:
                        # Append the text of each cell to the document_text string
                        text += (
                            cell.text + "\t"
                        )  # You can use a tab or another separator

        return text

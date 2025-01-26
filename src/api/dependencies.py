import json
import uuid
from datetime import datetime
from typing import List, Optional
from src.api.schema import Flashcard

class JSONDatabase:
    def __init__(self, filename: str = 'flashcards.json'):
        self.filename = filename
        self._ensure_file()

    def _ensure_file(self):
        try:
            with open(self.filename, 'r') as f:
                json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            with open(self.filename, 'w') as f:
                json.dump([], f)

    def _read(self) -> List[dict]:
        with open(self.filename, 'r') as f:
            return json.load(f)

    def _write(self, data: List[dict]):
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)

    def create(self, flashcard: Flashcard) -> Flashcard:
        cards = self._read()
        flashcard.id = str(uuid.uuid4())
        flashcard.created_at = datetime.now().isoformat()
        flashcard.updated_at = flashcard.created_at
        cards.append(flashcard.dict())
        self._write(cards)
        return flashcard

    # Other methods remain the same as in previous example
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

app = FastAPI(title="DistilBERT Intent Classifier API")

MODEL_PATH = "./model"

# Label mapping from config
LABELS = {
    0: "greeting",
    1: "inquiry",
    2: "info",
    3: "transaction_confirm",
    4: "unknown"
}

# Load tokenizer + model once at startup
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()  # Set to evaluation mode


class TextRequest(BaseModel):
    text: str


@app.get("/")
def health():
    return {"status": "Model API is running"}


@app.post("/predict")
def predict(req: TextRequest):
    inputs = tokenizer(
        req.text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    probabilities = F.softmax(logits, dim=1)[0]
    predicted_class = torch.argmax(probabilities).item()
    confidence = probabilities[predicted_class].item()

    return {
        "input": req.text,
        "predicted_class": predicted_class,
        "predicted_label": LABELS.get(predicted_class, "unknown"),
        "confidence": round(confidence, 4),
        "all_scores": {
            LABELS[i]: round(prob.item(), 4)
            for i, prob in enumerate(probabilities)
        }
    }

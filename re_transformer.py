from transformers import pipeline

fill_mask = pipeline("fill-mask", model="bert-base-uncased")
result = fill_mask("Barcelona will face against [MASK] in the Champions League final.")

print("Predictions for the masked token:")
for prediction in result:
    print(prediction['sequence'], f"{prediction['score']}")
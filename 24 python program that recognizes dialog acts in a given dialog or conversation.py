import re
def recognize_dialog_acts(dialog):
    dialog_acts = []
    for sentence in dialog.split('.'):
        sentence = sentence.strip().lower()
        if re.search(r'\b(hi|hello|hey)\b', sentence):
            dialog_acts.append((sentence, "Greeting"))
        elif re.search(r'\?$', sentence):
            dialog_acts.append((sentence, "Question"))
        elif re.search(r'thank', sentence):
            dialog_acts.append((sentence, "Thanking"))
        else:
            dialog_acts.append((sentence, "Statement"))
    return dialog_acts

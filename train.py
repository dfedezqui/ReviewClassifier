from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer


def cargar_datos(ruta, tope=None):
    textos = []
    labels = []
    contador = 0
    
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:

                if tope is not None and contador >= tope:
                    break

                linea = linea.strip()

                if not linea or "#" not in linea:
                    continue

                texto, opinion = linea.split("#", 1)

                textos.append(texto)
                labels.append(0 if opinion.lower() == "malo" else 1)

                contador += 1

    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta}")

    return textos, labels


def preparar_dataset(textos, etiquetas, tokenizer):

    tokenizados = tokenizer(
        textos,
        padding=True,
        truncation=True,
        max_length=256
    )

    dataset_final = []

    for i in range(len(etiquetas)):

        item = {clave: valores[i] for clave, valores in tokenizados.items()}
        item["labels"] = etiquetas[i]

        dataset_final.append(item)

    return dataset_final

if __name__ == '__main__':

    model_name = "distilbert-base-uncased"
    ruta_datos = "dataset/review.txt"

    textos, labels = cargar_datos(ruta_datos)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    modelo = AutoModelForSequenceClassification.from_pretrained(
        model_name,
        num_labels=2
    )

    train_dataset = preparar_dataset(textos, labels, tokenizer)

    args = TrainingArguments(

        output_dir="modelo/resultados",

        num_train_epochs=2,

        per_device_train_batch_size=16,

        logging_steps=100,

        report_to="none"
    )

    trainer = Trainer(

        model=modelo,

        args=args,

        train_dataset=train_dataset,

    )

    trainer.train()


    trainer.save_model("modelo/trainer_model")

    tokenizer.save_pretrained("modelo/trainer_model")
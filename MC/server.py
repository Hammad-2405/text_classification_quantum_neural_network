# coding=utf-8
# import numpy as np
from flask import Flask, jsonify, request
from flask_cors import CORS
# from quantum.tokenizer.ngram import get_tokenizer
# from quantum.filter.stw import stw_filter
# from quantum.embedding.onehot import embedding as onehot_embedding
# from quantum.embedding.tf import embedding as tf_embedding
# from quantum.model import QDConvNet, QConvNet
# from quantum.const import *
# from pyvqnet.utils import storage
# import pickle as pkl
import MC_q_eval

app = Flask(__name__)
CORS(app)

# # Model and dataset configurations
# dataset_name = 'MC'
# vocab_path = './data/' + dataset_name + '/vocab.quantum.pkl'
# idf_path = './data/' + dataset_name + '/idf.quantum.pkl'
# model_prefix = './model/' + dataset_name + '/msff-qconv'  # Example model
# batch_size = 1  # Single instance
# seq_len = 6
# emb_rep = 1
# kernel_size = 3
# depth = 1
# stride = 1
# num_class = 2

# # Load tokenizer, vocab, and IDF data
# tokenizer = get_tokenizer(ngram=[1], token_filter=stw_filter, la='en')

# with open(vocab_path, "rb") as f:
#     vocab = pkl.load(f)

# with open(idf_path, "rb") as f:
#     idf = pkl.load(f)

# # Initialize model
# num_qubits = int(np.ceil(np.log2(len(vocab))))
# model = QConvNet(len(vocab), num_qubits, num_class, kernel_size, depth, stride, emb_rep)
# model_para = storage.load_parameters(f'{model_prefix}.best.model')
# model.load_state_dict(model_para)


# def tokenize_and_embed(sentence):
#     """Tokenize and embed a single sentence."""
#     tokens = tokenizer([sentence], seq_len, need_pad=True)
#     word_embeddings = onehot_embedding(tokens, len(vocab))
#     sentence_embeddings = tf_embedding(tokens, len(vocab), idf)
#     return word_embeddings, sentence_embeddings


# def classify_sentence(sentence):
#     """Classify a single sentence."""
#     we, se = tokenize_and_embed(sentence)
#     logits = model.forward(np.expand_dims(we, axis=0), np.expand_dims(se, axis=0))
#     prediction = np.argmax(logits, axis=1)[0]
#     return prediction


# @app.route("/api/classify-text", methods=["POST"])
# def classify_text():
#     """API endpoint for classifying text."""
#     data = request.get_json()
#     if not data or "sentence" not in data:
#         return jsonify({"error": "Invalid request, 'sentence' is required"}), 400

#     sentence = data["sentence"]
#     prediction = classify_sentence(sentence)
#     category = "positive" if prediction == 1 else "negative"

#     return jsonify({"sentence": sentence, "category": category})


@app.route("/", methods=["GET"])
def main_page():
    return jsonify({
        "message": "Main Page"
    })

@app.route("/api/run", methods=["GET"])
def run():
    ans = MC_q_eval.run()
    return jsonify(ans)
    
    
    


if __name__ == "__main__":
    app.run(debug=True, port=8080)

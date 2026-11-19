import numpy as np
from sentence_transformers import SentenceTransformer


MODEL_NAME = "intfloat/multilingual-e5-small"


def test_e5_model_smoke():
    model = SentenceTransformer(MODEL_NAME)

    queries = ["query: \u091c\u0932\u0935\u093e\u092f\u0941 \u092a\u0930\u093f\u0935\u0930\u094d\u0924\u0928 \u0915\u093e \u0915\u094d\u092f\u093e \u092a\u094d\u0930\u092d\u093e\u0935 \u0939\u0948?"]
    passages = [
        "passage: Climate change affects global temperatures and weather patterns."
    ]

    query_embeddings = model.encode(
        queries,
        normalize_embeddings=True,
    )

    passage_embeddings = model.encode(
        passages,
        normalize_embeddings=True,
    )

    assert query_embeddings.shape == (1, 384)
    assert passage_embeddings.shape == (1, 384)

    assert np.isfinite(query_embeddings).all()
    assert np.isfinite(passage_embeddings).all()

    similarity = np.dot(query_embeddings[0], passage_embeddings[0])

    assert np.isfinite(similarity)
    assert -1.0 <= similarity <= 1.0

    print(f"\nCross-lingual similarity: {similarity:.4f}")
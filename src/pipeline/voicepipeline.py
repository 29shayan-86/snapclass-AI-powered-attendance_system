import io
import librosa
import numpy as np
from resemblyzer import VoiceEncoder, preprocess_wav
import soundfile as sf
import streamlit as st


@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder()


def get_voice_embedding(audio_bytes):
    if not audio_bytes:
        print("DEBUG: audio_bytes is empty or None")
        return None

    encoder = load_voice_encoder()

    # Stream bytes into soundfile
    audio_stream = io.BytesIO(audio_bytes)
    audio, sr = sf.read(audio_stream)

    # Convert stereo to mono
    if len(audio.shape) > 1:
        audio = np.mean(audio, axis=1)

    # Convert float64 to float32 (resemblyzer requirement)
    audio = audio.astype(np.float32)

    # Resample to 16kHz
    if sr != 16000:
        audio = librosa.resample(audio, orig_sr=sr, target_sr=16000)

    wav = preprocess_wav(audio)
    embedding = encoder.embed_utterance(wav)

    return embedding.tolist()


def identify_speaker(new_embedding, candidates_dict, threshold=0.65):
    if new_embedding is None or not candidates_dict:
        return None, 0.0

    best_sid = None
    best_score = -1.0

    for sid, stored_embedding in candidates_dict.items():
        if stored_embedding:
            similarity = np.dot(new_embedding, stored_embedding)
            if similarity > best_score:
                best_score = similarity
                best_sid = sid

    if best_score >= threshold:
        return best_sid, float(best_score)

    return None, float(best_score)


def process_bulk_audio(audio_bytes, candidates_dict, threshold=0.65):
    if not audio_bytes:
        return {}

    try:
        encoder = load_voice_encoder()

        audio_stream = io.BytesIO(audio_bytes)
        audio, sr = sf.read(audio_stream)

        if len(audio.shape) > 1:
            audio = np.mean(audio, axis=1)

        if sr != 16000:
            audio = librosa.resample(audio, orig_sr=sr, target_sr=16000)
            sr = 16000

        segments = librosa.effects.split(audio, top_db=30)
        identified_results = {}

        for start, end in segments:
            if (end - start) < sr * 0.5:
                continue

            segment_audio = audio[start:end]
            wav = preprocess_wav(segment_audio)
            embedding = encoder.embed_utterance(wav)

            sid, score = identify_speaker(embedding, candidates_dict, threshold)

            if sid:
                if sid not in identified_results or score > identified_results[sid]:
                    identified_results[sid] = score

        return identified_results

    except Exception as e:
        print(f"DEBUG Bulk Process Exception: {repr(e)}")
        st.error(f"Bulk process error: {e}")
        return {}
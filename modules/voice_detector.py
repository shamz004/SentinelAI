import numpy as np
import librosa
import noisereduce as nr
from sklearn.preprocessing import StandardScaler


class VoiceDetector:

    def __init__(self):
        self.scaler = StandardScaler()

    def load_audio(self, file_path):
        audio, sr = librosa.load(file_path, sr=16000)
        return audio, sr

    def reduce_noise(self, audio, sr):
        return nr.reduce_noise(y=audio, sr=sr)

    def extract_features(self, audio, sr):
        mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
        return np.mean(mfcc.T, axis=0)

    def classify(self, score):
        if score > 0.7:
            return "HIGH RISK (Possible Fraud Voice)"
        elif score > 0.4:
            return "MEDIUM RISK"
        else:
            return "LOW RISK (Likely Real Voice)"

    def analyze(self, file_path):
        try:
            audio, sr = self.load_audio(file_path)
            audio = self.reduce_noise(audio, sr)

            features = self.extract_features(audio, sr)

            energy = np.mean(np.abs(audio))
            mfcc_var = np.var(features)

            score = (energy * 0.6) + (mfcc_var * 0.4)
            score = float(np.clip(score / 5.0, 0, 1))

            risk = self.classify(score)

            return {
                "score": round(score, 3),
                "risk_level": risk
            }

        except Exception as e:
            return {
                "error": str(e)
            }